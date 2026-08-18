"""
Problem: A2 - Generate State 1/sqrt(2)(|0> -|3>)
Platform: QCoder
Score: 200 points
Time Limit: 3.0s | Memory Limit: 512 MiB

[Objective]
Implement the operation of preparing the state ∣ψ⟩=1/sqrt(2)(|0> -|3>) from the zero state on a quantum circuit qc with 2 qubits.

"""


import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    # Write your code here:
    qc.x(1)
    qc.h(1)
    qc.cx(1,0)
    return qc
 

if __name__ == "__main__":
    qc = solve()
    print("Circuit:")
    print(qc.draw(output="text"))

    # Local Verification
    target_state = np.array(([1.0, 0.0,0.0,-1.0])/np.sqrt(2), dtype=complex)
    final_sv = Statevector.from_instruction(qc).data

    print("\n--- Output Check ---")
    print(f"Target statevector : {target_state}")
    print(f"Actual statevector : {final_sv}")

    if np.allclose(final_sv, target_state):
        print("Status: PASS (Exact phase and amplitudes match)")
    else:
        print("Status: FAIL (Mismatch in phase or amplitude)")