# Prodigal Trig Engine – 3-Axis Bloch Sphere Controller

Analog, radiation-hardened, arbitrary single-qubit rotation engine.  
Three identical 32.768 kHz + BB135 varactor channels → full SU(2) coverage in <180 µs at <600 µW total power.  
Zero flip-flops, zero registers → inherently SEU-immune and cryo-compatible.

Room-temperature breadboard already rotating states.  
Cryo validation scheduled Q1 2026.

**Provisional Patents**  
63/917293 – Core trig engine  
63/920694 – Interaural cue & Bloch sphere controller (filed Nov 2025)

Quantum licensing table open 

## Simulation (QuTiP 5.x)
Starts at |0⟩ → RX(π/2) → RY(π/3) → RZ(π/4)  
Trajectory: |0⟩ (north pole) → X(π/2) arc to equator (| + ⟩) → Y(π/3) lift to ~58° latitude → Z(π/4) phase at final state. Fidelity 1.000000.  
Run `simulate.py` to generate bloch_3axis.png.

MIT License – fork, build, fly.
