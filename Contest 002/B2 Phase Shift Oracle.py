"""
Problem: B2 - Phase Shift Oracle
Platform: QCoder
Score: 200 points
Time Limit: 3.0s | Memory Limit: 512 MiB

[Objective]
You are given integers n, L, and a real number θ. Implement the oracle O on a quantum circuit qc with n qubits acting on computational basis states as:

∣y⟩n →
-e^{iθ}|y>n if y = L
-|y>n if y != L 

for any integer y such that  0<= y < 2^n

[Constraints & Notes]
1≤n≤10
0≤L<2^n
0≤θ<2π
Integers must be encoded by little-endian.
Global phase is ignored in judge.
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector



def solve(n: int, L: int, theta: float) -> QuantumCircuit:
    qc = QuantumCircuit(n)

    # Convert L to an n-bit binary string and reverse it for little-endian

    bits = bin(L)[2:].zfill(n)[::-1]

    # 1. Flip qubits where the bit is '0'
    for j, bit in enumerate(bits):
        if bit == "0":
            qc.x(j)

    if n == 1:
        qc.p(theta, 0)
    else:
        qc.mcp(theta, list(range(n - 1)), n - 1)

    # 3. Uncompute the X gates
    for j, bit in enumerate(bits):
        if bit == "0":
            qc.x(j)

    return qc
    
if __name__ == "__main__":
  test_angles = [0.0, np.pi / 4, np.pi / 2, np.pi, 3 * np.pi / 2, 2.3456]
  all_passed = True

  print("--- Running Local Verification ---")

  for n in range(1, 7):
    # Test key basis indices (0, 1, middle, max) within [0, 2^n - 1]
    test_L_values = sorted(list({0, 1, 2 ** (n - 1), 2**n - 1}))

    for L in test_L_values:
      for theta in test_angles:
        # 1. Create an equal superposition of all states using Hadamard gates
        test_circuit = QuantumCircuit(n)
        test_circuit.h(range(n))

        # 2. Append your oracle to the test circuit
        oracle = solve(n, L, theta)
        test_circuit.compose(oracle, inplace=True)

        # 3. Compute the output statevector
        final_sv = Statevector.from_instruction(test_circuit).data

        # 4. Expected statevector: 1/sqrt(2^n) everywhere, with e^(i*theta) phase on index L
        expected_sv = np.ones(2**n, dtype=complex) / np.sqrt(2**n)
        expected_sv[L] *= np.exp(1j * theta)

        # 5. Compare
        passed = np.allclose(final_sv, expected_sv)
        if not passed:
          all_passed = False
          print(f"FAIL -> n={n}, L={L}, theta={theta:.4f}")

  if all_passed:
    print("\nResult: All statevector checks passed successfully.")