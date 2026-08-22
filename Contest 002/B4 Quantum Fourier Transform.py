"""
Problem: B4 - Quantum Fourier Transform
Platform: QCoder (Contest 002)
Score: 200 points
Time Limit: 3.0s | Memory Limit: 512 MiB

[Objective]
Given an integer n, implement the Quantum Fourier Transform (QFT) for n qubits:
    |j>_n  -->  (1 / sqrt(2^n)) * sum_{k=0}^{2^n - 1} exp(2*pi*i*j*k / 2^n) |k>_n
for any integer 0 <= j < 2^n.

[Constraints & Notes]
- 1 <= n <= 10
- Circuit depth must not exceed 25.
- Integers are encoded in little-endian notation (|100> = 1, |001> = 4).
- Global phase is ignored in judge.

[Sample]
For n = 2:
    |10>  -->  (1/2) * (|00> + e^(i*pi/2)|10> + e^(i*pi)|01> + e^(i*3*pi/2)|11>)
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator


def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)

    # Write your code here:
    for i in reversed(range(n)):
        qc.h(i)
        for j in reversed(range(i)):
            angle = np.pi / 2**(i-j)
            qc.cp(angle ,i,j)
    
    for i in range(n//2):
        qc.swap(i,n-1-i)

    return qc


if __name__ == "__main__":
    print("--- Running Local Verification ---")
    all_passed = True

    for n in range(1, 6):
        qc = solve(n)
        depth = qc.depth()
        print(f"\n[n = {n}] Circuit Depth: {depth} (Limit <= 25)")
        print("Circuit:")
        print(qc.draw(output="text"))

        # Construct target QFT unitary matrix: F[k, j] = exp(2*pi*i*j*k / 2^n) / sqrt(2^n)
        N = 2**n
        target_unitary = np.zeros((N, N), dtype=complex)
        for j in range(N):
            for k in range(N):
                target_unitary[k, j] = np.exp(2j * np.pi * j * k / N) / np.sqrt(N)

        try:
            actual_unitary = Operator(qc).data

            # Check equivalence up to global phase
            # Find phase offset from first non-zero element
            phase = actual_unitary[0, 0] / target_unitary[0, 0]
            matches_unitary = np.allclose(actual_unitary, target_unitary * phase)
            within_depth = depth <= 25

            if matches_unitary and within_depth:
                print(f"Status: PASS (Correct QFT and depth {depth} <= 25)")
            elif not within_depth:
                print(f"Status: FAIL (Depth {depth} exceeds limit 25)")
                all_passed = False
            else:
                print("Status: INCOMPLETE / FAIL (Unitary does not match QFT)")
                all_passed = False
        except Exception as e:
            print(f"Verification Error: {e}")
            all_passed = False

    if all_passed:
        print("\nResult: All test cases passed successfully!")
    else:
        print("\nResult: Some tests are incomplete/failed.")
