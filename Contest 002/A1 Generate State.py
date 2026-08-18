"""
Problem: A1 - Generate State -|0>
Platform: QCoder
Score: 100 points
Time Limit: 3.0s | Memory Limit: 512 MiB

[Objective]
Transform the standard ground state into a negative phase state:
    |0>  -->  -|0>


[Constraints & Notes]
- In this problem, the state with different global phase will not be considered correct.
"""

import sys
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(1)

    # Write your code here:
    #qc.ry(2* np.pi,0)

    #or
    qc.x(0)
    qc.z(0)
    qc.x(0)


    return qc


if __name__ == "__main__":
    qc = solve()
    print("Circuit:")
    print(qc.draw(output="text"))

    # Local Verification
    target_state = np.array([-1.0, 0.0], dtype=complex)
    final_sv = Statevector.from_instruction(qc).data

    print("\n--- Output Check ---")
    print(f"Target statevector : {target_state}")
    print(f"Actual statevector : {final_sv}")

    if np.allclose(final_sv, target_state):
        print("Status: PASS (Exact phase and amplitudes match)")
    else:
        print("Status: FAIL (Mismatch in phase or amplitude)")