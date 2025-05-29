import sounddevice as sd
import numpy as np
import queue
import threading
import time
import sys
import os
from scipy.signal import butter, lfilter

class WakeWordDetector:
    def __init__(self, samplerate=16000, duration=1, threshold=0.02, wakeword="gideon"):
        self.samplerate = samplerate
        self.duration = duration
        self.threshold = threshold
        self.q = queue.Queue()
        self.running = False
        self.audio_buffer = []
        self.max_buffer_size = int(self.samplerate * self.duration)
        self.wakeword = wakeword
        self.detected_callback = None

    def set_detected_callback(self, callback):
        self.detected_callback = callback

    def audio_callback(self, indata, frames, time_info, status):
        if status:
            print(status, file=sys.stderr)
        self.q.put(indata.copy())

    def butter_bandpass(self, lowcut, highcut, fs, order=5):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        return b, a

    def bandpass_filter(self, data, lowcut=300.0, highcut=3400.0, order=6):
        b, a = self.butter_bandpass(lowcut, highcut, self.samplerate, order=order)
        y = lfilter(b, a, data, axis=0)
        return y

    def detect_wakeword(self, audio_chunk):
        # Enhanced: bandpass filter + energy + zero-crossing rate
        filtered = self.bandpass_filter(audio_chunk.flatten())
        energy = np.linalg.norm(filtered) / len(filtered)
        zero_crossings = np.mean(np.abs(np.diff(np.sign(filtered))))
        # Simple heuristic: both energy and zero-crossing must be above thresholds
        return energy > self.threshold and zero_crossings > 0.05

    def listen_for_wakeword(self, timeout=None):
        print(f"Listening for wake word ('{self.wakeword}')...")
        self.running = True
        start_time = time.time()
        with sd.InputStream(channels=1, samplerate=self.samplerate, callback=self.audio_callback):
            while self.running:
                if timeout and (time.time() - start_time) > timeout:
                    print("Timeout reached. Stopping wake word detection.")
                    self.running = False
                    return False
                try:
                    audio_chunk = self.q.get(timeout=1)
                    self.audio_buffer.append(audio_chunk)
                    # Keep buffer size manageable
                    if len(self.audio_buffer) > self.max_buffer_size:
                        self.audio_buffer = self.audio_buffer[-self.max_buffer_size:]
                    if self.detect_wakeword(audio_chunk):
                        print("Wake word detected!")
                        self.running = False
                        if self.detected_callback:
                            self.detected_callback()
                        return True
                except queue.Empty:
                    continue
        return False

    def save_last_audio(self, filename="wakeword_audio.wav"):
        try:
            import soundfile as sf
            audio_data = np.concatenate(self.audio_buffer, axis=0)
            sf.write(filename, audio_data, self.samplerate)
            print(f"Saved audio to {filename}")
        except ImportError:
            print("soundfile module not installed. Cannot save audio.")

if __name__ == "__main__":
    detector = WakeWordDetector()
    def on_detected():
        print("Callback: Wake word event triggered!")
        detector.save_last_audio()
    detector.set_detected_callback(on_detected)
    detector.listen_for_wakeword(timeout=30)