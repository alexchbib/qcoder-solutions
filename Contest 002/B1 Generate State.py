"""
Problem: B1 - Generate State e^(i*theta)|0>
Platform: QCoder
Score: 100 points
Time Limit: 3.0s | Memory Limit: 512 MiB

[Objective]
You are given a real number θ. Implement the operation of preparing the state |ψ⟩=e^iθ|0> from the zero state on a quantum circuit qc with 1 qubit.

[Constraints & Notes]
- 0 <= theta < 2*pi
- In this problem, the state with different global phase will not be considered correct.
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def solve(theta: float) -> QuantumCircuit:
    qc = QuantumCircuit(1)
    qc.rz(-2 * theta,0)
    return qc   


if __name__ == "__main__":
    # Test cases across diverse phase angles
    test_angles = [0.0, np.pi / 4, np.pi / 2, np.pi, 3 * np.pi / 2, 2.3456]

    print("--- Running Local Verification ---")
    all_passed = True

    for theta in test_angles:
        qc = solve(theta)
        target_state = np.array([np.exp(1j * theta), 0.0], dtype=complex)
        final_sv = Statevector.from_instruction(qc).data

        passed = np.allclose(final_sv, target_state)
        status = "PASS" if passed else "FAIL"
        if not passed:
            all_passed = False

        print(f"theta = {theta:6.4f} rad | Status: {status}")
        if not passed:
            print(f"  Target : {target_state}")
            print(f"  Actual : {final_sv}")

    if all_passed:
        print("\nResult: All angle checks passed successfully.")