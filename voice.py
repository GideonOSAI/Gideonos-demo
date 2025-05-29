import asyncio
import edge_tts
import playsound
import uuid
import os

# Asynchronous voice speaking function
async def speak_async(text):
    filename = f"voice_{uuid.uuid4().hex}.mp3"
    communicate = edge_tts.Communicate(text=text, voice="en-US-GuyNeural")
    await communicate.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

# Synchronous wrapper
def say(text):
    asyncio.run(speak_async(text))