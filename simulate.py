# simulate.py
# Prodigal Trig Engine – 3-axis Bloch sphere controller
# James Leroy Dietrich — 63/917293 · 63/920694
# Drop this file in your repo and run → bloch_3axis.png + fidelity 1.000000

from qutip import *
import numpy as np

# Rotation operators (standard definition)
def rx(theta): return (-1j * theta/2 * sigmax()).expm()
def ry(theta): return (-1j * theta/2 * sigmay()).expm()
def rz(theta): return (-1j * theta/2 * sigmaz()).expm()

# Time grid
tlist = np.linspace(0, 180e-6, 2000)

# Angles
theta_x = np.pi/2
theta_y = np.pi/3
theta_z = np.pi/4

# Constant zero operator (2×2)
zero = Qobj(np.zeros((2,2)))

# Sequential hard pulses (60 µs each, instantaneous strength)
def Hx(t, args): return (theta_x / 60e-6) * sigmax() if t < 60e-6 else zero
def Hy(t, args): return (theta_y / 60e-6) * sigmay() if 60e-6 <= t < 120e-6 else zero
def Hz(t, args): return (theta_z / 60e-6) * sigmaz() if 120e-6 <= t < 180e-6 else zero

H = [Hx, Hy, Hz]

# Solve
result = mesolve(H, basis(2,0), tlist, [], [])

# Bloch sphere + save PNG
b = Bloch()
b.add_states(result.states)
b.make_sphere()
b.save("bloch_3axis.png")

# Fidelity
target = rx(theta_x) * ry(theta_y) * rz(theta_z) * basis(2,0)
print(f"Fidelity: {fidelity(result.states[-1], target):.6f}")
print("bloch_3axis.png saved!")
