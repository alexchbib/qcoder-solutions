"""
Problem: B5 - Quantum Arithmetic I
Platform: QCoder (Contest 002)
Score: 200 points
Time Limit: 3.0s | Memory Limit: 512 MiB

[Objective]
You are given integers n, m, and S = [S_0, S_1, ..., S_{n-1}].
For an integer x = sum_{k=0}^{n-1} x_k * 2^k (with x_k in {0, 1}), define:
    f(x) = sum_{k=0}^{n-1} S_k * x_k

Implement the n-qubit oracle O acting on computational basis states as:
    |x>_n  -->  exp(2*pi*i * f(x) / 2^m) |x>_n
for any integer 0 <= x < 2^n.

[Constraints & Notes]
- 1 <= n, m <= 10
- 0 <= S_k < 2^m
- Circuit depth must not exceed 10.
- Integers are encoded in little-endian notation.
- Global phase is ignored in judge.

[Sample]
n = 2, m = 2, S = [1, 3]
For |x> = |11> = |3>:
    f(3) = 1*1 + 3*1 = 4
    |11>  -->  exp(2*pi*i * 4 / 4) |11> = exp(2*pi*i) |11> = |11>
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def solve(n: int, m: int, S: list[int]) -> QuantumCircuit:
    qc = QuantumCircuit(n)

    # Write your code here:
    d= 2**m 
    for i in range(n):
        angle = (2*np.pi * S[i]/d)
        qc.p(angle ,i)


    return qc


if __name__ == "__main__":
    print("--- Running Local Verification ---")
    test_cases = [
        # (n, m, S)
        (2, 2, [1, 3]),
        (3, 4, [1, 5, 7]),
        (4, 5, [3, 0, 11, 25]),
        (1, 3, [5]),
    ]

    all_passed = True

    for n, m, S in test_cases:
        qc = solve(n, m, S)
        depth = qc.depth()

        # 1. Create equal superposition over all basis states |x>
        test_circuit = QuantumCircuit(n)
        test_circuit.h(range(n))
        test_circuit.compose(qc, inplace=True)

        final_sv = Statevector.from_instruction(test_circuit).data
        # 2. Compute expected statevector
        expected_sv = np.zeros(2**n, dtype=complex)
        for x in range(2**n):
            # Extract little-endian bits x_0, x_1, ..., x_{n-1}
            f_x = sum(S[k] * ((x >> k) & 1) for k in range(n))
            phase = np.exp(2j * np.pi * f_x / (2**m))
            expected_sv[x] = (1.0 / np.sqrt(2**n)) * phase

        # 3. Check equivalence (ignoring global phase)
        global_phase = final_sv[0] / expected_sv[0]
        matches = np.allclose(final_sv, expected_sv * global_phase)
        within_depth = depth <= 10

        print(f"\nTest Case (n={n}, m={m}, S={S}):")
        print(f"  Circuit Depth : {depth} (Limit <= 10)")
        print(f"  Unitary Match : {matches}")

        if matches and within_depth:
            print(f"  Status: PASS")
        elif not within_depth:
            print(f"  Status: FAIL (Depth {depth} > 10)")
            all_passed = False
        else:
            print(f"  Status: INCOMPLETE / FAIL")
            all_passed = False

    if all_passed:
        print("\nResult: All test cases passed successfully!")
    else:
        print("\nResult: Some tests are incomplete/failed.")
