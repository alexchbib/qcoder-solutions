"""
Problem: A4 - Generate State 1/sqrt(2)(|0> -|2^n -1>) II
Platform: QCoder
Score: 400 points
Time Limit: 3.0s | Memory Limit: 512 MiB

[Objective]
You are given an integer n. Implement the operation of preparing the state |ψ⟩= 1/sqrt(2)(|0> -|2^n -1>) from the zero state on a quantum circuit qc with n qubits.

[Constraints]
2≤n≤15
Circuit depth must be O(log n) (depth <= 10).
Global phase is ignored in judge.
"""


import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


 
def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    qc.x(0)
    qc.h(0)
    flipped=1
    while flipped <n:
        for i in range (flipped):
            if i+ flipped<n:
                qc.cx(i,i +flipped )
                
        flipped = flipped *2 #doubles each round
    return qc

if __name__ == "__main__":
    all_passed = True
    for n in range(2,16):
        qc = solve(n)
        print(f"Number of qubits: {n}")
        print("Circuit:")
        print(qc.draw(output="text"))

        target_state = np.zeros(2**n,dtype=complex)
        target_state[0] = 1/np.sqrt(2)
        target_state[2**n -1] = -1/np.sqrt(2)
        final_sv = Statevector.from_instruction(qc).data

        print("\n--- Output Check ---")
        print(f"Target statevector : {target_state}")
        print(f"Actual statevector : {final_sv}")

        if np.allclose(final_sv, target_state) and qc.depth()<=10:
            print("Status: PASS (Exact phase and amplitudes match and circuit depth less than 10)")
        else:
            print("Status: FAIL (Mismatch in phase or amplitude or depth is greater than 10)")
            all_passed = False
            break
        
    
    if all_passed:
        print("ALL TESTS PASSED!")
    else:
        print("SOME TESTS FAILED")