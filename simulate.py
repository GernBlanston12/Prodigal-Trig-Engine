# Prodigal Trig Engine – 3-axis Bloch sphere controller simulation
# James Leroy Dietrich — 63/917293 · 63/920694
# Run in QuTiP 5.x

from qutip import *
import numpy as np
import matplotlib.pyplot as plt

# 200 µs total evolution
tlist = np.linspace(0, 200e-6, 1000)

# Example rotation angles
theta_x = np.pi/2
theta_y = np.pi/3
theta_z = np.pi/4

# Time-dependent Hamiltonians (60 µs per axis)
def H_x(t, args):
    return theta_x / 60e-6 * sigmax() if t < 60e-6 else 0

def H_y(t, args):
    return theta_y / 60e-6 * sigmay() if 60e-6 <= t < 120e-6 else 0

def H_z(t, args):
    return theta_z / 60e-6 * sigmaz() if 120e-6 <= t < 180e-6 else 0

H = [H_x, H_y, H_z]

# Initial state |0⟩
psi0 = basis(2, 0)

# Solve (ideal case)
result = mesolve(H, psi0, tlist, [], [])

# Bloch sphere plot
b = Bloch()
b.add_states(result.states)
b.make_sphere()
b.save("bloch_3axis.png")  # saves directly

# Fidelity check
target = (rx(theta_x) * ry(theta_y) * rz(theta_z) * basis(2, 0)).unit()
print(f"Final state fidelity: {fidelity(result.states[-1], target):.6f}")
