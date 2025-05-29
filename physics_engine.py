import re

def answer_physics_question(question: str) -> str:
    question = question.lower()

    # Numerical calculation for F = m * a
    match = re.search(r'force.*mass\s*=?\s*([\d.]+)\s*(kg)?\s*.*acceleration\s*=?\s*([\d.]+)\s*(m/s\^?2)?', question)
    if match:
        mass = float(match.group(1))
        acceleration = float(match.group(3))
        force = mass * acceleration
        return f"Using F = m * a: Force = {mass} kg * {acceleration} m/s² = {force} N."

    # Classical Mechanics
    if re.search(r'\b(classical mechanics|mechanics|motion|kinematics|dynamics|statics)\b', question):
        return (
            "Classical mechanics studies the motion of objects and the forces that cause them. "
            "Kinematics describes motion (displacement, velocity, acceleration) without regard to forces. "
            "Dynamics relates motion to forces (Newton's laws). Statics studies forces in equilibrium. "
            "Key equations: v = u + at, s = ut + 0.5at², F = m * a. "
            "It forms the foundation for engineering, astronomy, and everyday physics."
        )

    # Gravity
    if re.search(r'\b(gravity|gravitational)\b', question):
        return (
            "Gravity is a fundamental force attracting masses. Newton's law: F = G * (m1 * m2) / r², where G ≈ 6.674×10⁻¹¹ N·m²/kg². "
            "On Earth, gravity accelerates objects downward at 9.8 m/s². "
            "Einstein's general relativity describes gravity as spacetime curvature, explaining phenomena like black holes and gravitational waves."
        )

    # Newton's Laws
    if re.search(r"newton'?s?\s+first\s+law|inertia", question):
        return (
            "Newton's first law (inertia): An object remains at rest or in uniform motion unless acted on by an external force. "
            "This explains why seatbelts are important in cars and why objects don't move unless pushed."
        )
    if re.search(r"newton'?s?\s+second\s+law", question):
        return (
            "Newton's second law: Force equals mass times acceleration (F = m * a). "
            "This law allows calculation of how objects move under applied forces."
        )
    if re.search(r"newton'?s?\s+third\s+law", question):
        return (
            "Newton's third law: For every action, there is an equal and opposite reaction. "
            "This explains rocket propulsion and why you move backward when jumping off a boat."
        )

    # Conservation Laws
    if re.search(r'conservation of (energy|momentum|angular momentum|charge)', question):
        return (
            "Conservation laws: Energy, momentum, angular momentum, and electric charge are conserved in isolated systems. "
            "These principles are fundamental to all physics and apply from atomic to cosmic scales."
        )

    # Speed of light
    if re.search(r'speed\s+of\s+light|c\s*=', question):
        return (
            "The speed of light in vacuum is about 299,792,458 m/s (c). It's the universal speed limit. "
            "Light speed is central to relativity and affects time, space, and causality."
        )

    # Energy
    if re.search(r'\benergy\b|\bwork\b|\bjoule\b', question):
        return (
            "Energy is the ability to do work. Forms include kinetic (E_k = 0.5*m*v²), potential (E_p = mgh), thermal, chemical, and nuclear. "
            "Work is force applied over distance (W = F * d). The SI unit is the joule (J). "
            "Energy can be transformed but not created or destroyed (conservation of energy)."
        )

    # Power
    if re.search(r'\bpower\b|\bwatt\b', question):
        return (
            "Power is the rate of doing work or transferring energy (P = W/t). The SI unit is the watt (W). "
            "High power means more energy is transferred in less time."
        )

    # Momentum
    if re.search(r'\bmomentum\b|\bimpulse\b', question):
        return (
            "Momentum (p) is mass times velocity (p = m * v). Impulse changes momentum (Impulse = F * t). "
            "Momentum is conserved in isolated systems, explaining collisions and rocket motion."
        )

    # Rotational Motion
    if re.search(r'(rotational|angular|torque|moment of inertia|centripetal)', question):
        return (
            "Rotational motion involves angular displacement, velocity, and acceleration. "
            "Torque (τ = r × F) causes rotation. Moment of inertia (I) is rotational mass, depending on mass distribution. "
            "Centripetal force keeps objects moving in circles (F = m*v²/r). Angular momentum is conserved in closed systems."
        )

    # Thermodynamics
    if re.search(r'thermodynamics|entropy|heat|temperature|first law|second law|third law|zeroth law', question):
        return (
            "Thermodynamics studies heat, energy, and work. Zeroth law: defines temperature and thermal equilibrium. "
            "First law: energy conservation (ΔU = Q - W). Second law: entropy increases, heat flows from hot to cold. "
            "Third law: absolute zero is unattainable. Thermodynamics explains engines, refrigerators, and the arrow of time."
        )

    # Waves and Optics
    if re.search(r'(wave|sound|light|optics|frequency|wavelength|interference|diffraction|reflection|refraction)', question):
        return (
            "Waves transfer energy without transferring matter. Key properties: frequency, wavelength, amplitude, speed. "
            "Optics studies light: reflection, refraction (Snell's law), diffraction, and interference. "
            "Sound is a mechanical wave; light is an electromagnetic wave."
        )

    # Electricity and Magnetism
    if re.search(r'(electric|magnetic|electromagnetic|coulomb|current|voltage|resistance|ohm|faraday|maxwell|induction|capacitor|inductor)', question):
        return (
            "Electricity and magnetism: Charges interact via Coulomb's law. Current is charge flow (I = Q/t). "
            "Ohm's law: V = I*R. Magnetic fields exert forces on moving charges. "
            "Maxwell's equations unify electricity and magnetism, predicting electromagnetic waves (light)."
        )

    # Quantum Physics
    if re.search(r'quantum|photon|uncertainty|wave-particle|planck|schr[oö]dinger|heisenberg|quantization|superposition|entanglement', question):
        return (
            "Quantum physics explores matter and energy at atomic scales. Key ideas: quantization, wave-particle duality, uncertainty principle, superposition, entanglement. "
            "Schrödinger's equation describes quantum systems. Quantum mechanics underlies semiconductors, lasers, and modern technology."
        )

    # Atomic and Nuclear Physics
    if re.search(r'(atom|nucleus|proton|neutron|electron|radioactivity|fission|fusion|alpha|beta|gamma)', question):
        return (
            "Atomic physics studies electrons and atoms. Nuclear physics studies nuclei, radioactivity (alpha, beta, gamma decay), fission, and fusion. "
            "These processes power stars and nuclear reactors."
        )

    # Relativity
    if re.search(r'relativity|einstein|spacetime|time dilation|length contraction|mass-energy|e=mc\^?2', question):
        return (
            "Relativity (Einstein): Special relativity covers constant-speed motion, time dilation, length contraction, and E=mc² (mass-energy equivalence). "
            "General relativity explains gravity as spacetime curvature, predicting black holes and gravitational lensing."
        )

    # Particle Physics
    if re.search(r'(particle physics|standard model|quark|lepton|boson|higgs|neutrino|gluon|muon|tau)', question):
        return (
            "Particle physics studies fundamental particles: quarks, leptons, bosons. The Standard Model explains their interactions via fundamental forces. "
            "The Higgs boson gives particles mass. Particle accelerators probe these building blocks of matter."
        )

    # Cosmology and Astrophysics
    if re.search(r'(cosmology|big bang|universe|galaxy|star|black hole|dark matter|dark energy|expansion|redshift)', question):
        return (
            "Cosmology studies the universe's origin, structure, and fate. The Big Bang theory describes its beginning. "
            "Astrophysics covers stars, galaxies, black holes, dark matter, and dark energy. "
            "Observations like redshift show the universe is expanding."
        )

    # Units conversion
    if re.search(r'convert\s+([\d.]+)\s*(kg|g|lb|m|cm|mm|km|mi|ft|in)\s+to\s+(kg|g|lb|m|cm|mm|km|mi|ft|in)', question):
        return "Unit conversion is not yet implemented, but you can use online converters or specify the values."

    # General fallback
    return (
        "Physics is the study of matter, energy, space, and time. It covers classical mechanics, gravity, thermodynamics, waves, optics, electricity, magnetism, quantum physics, relativity, particle physics, and cosmology. "
        "Ask about any topic or calculation, such as Newton's laws, energy, momentum, thermodynamics, quantum mechanics, relativity, or the universe. "
        "Physics principles explain everything from atoms to galaxies, and underlie all modern technology."
    )
