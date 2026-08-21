"""
Problem: B3 - SWAP Qubits
Platform: QCoder (Contest 002)
Score: 200 points
Time Limit: 3.0s | Memory Limit: 512 MiB

[Objective]
Implement the operation of swapping two qubit states on a quantum circuit qc with 2 qubits:
    a0|00> + a1|10> + a2|01> + a3|11>  -->  a0|00> + a2|10> + a1|01> + a3|11>
where ai represents arbitrary probability amplitudes.

[Constraints & Notes]
- You cannot use Qiskit's SwapGate (or qc.swap) in this problem.
- Global phase is ignored in judge.
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator, Statevector


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)

    #00 , 01 ,10 ,11
    #00 , 11 , 10 ,01
    #00 , 10, 11, 01
    #00 , 10, 01 ,11

    # Write your code here:
    #01

    qc.cx(1,0)
    qc.cx(0,1)
    qc.cx(1,0)


    
    return qc


if __name__ == "__main__":
    qc = solve()
    print("Circuit:")
    print(qc.draw(output="text"))

    # Expected SWAP Unitary matrix
    target_unitary = np.array(
        [
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
        ],
        dtype=complex,
    )

    print("\n--- Running Local Verification ---")
    try:
        actual_unitary = Operator(qc).data
        is_swap = np.allclose(actual_unitary, target_unitary)

        # Check constraint: Ensure SwapGate was not used
        gate_names = [inst.operation.name for inst in qc.data]
        no_swap_gate = "swap" not in gate_names

        print(f"Target Unitary Match : {is_swap}")
        print(f"No SwapGate Used     : {no_swap_gate}")

        if is_swap and no_swap_gate:
            print("Status: PASS (Correct SWAP implementation without SwapGate)")
        elif not no_swap_gate:
            print("Status: FAIL (SwapGate used; violates constraint)")
        else:
            print("Status: INCOMPLETE / FAIL (Unitary does not match SWAP)")
    except Exception as e:
        print(f"Verification Error: {e}")
