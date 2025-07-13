# What:
# For simulators, this means how much RAM is needed to store the quantum state vector or density matrix.
# For hardware, memory usage is negligible because it’s physical qubits!

# How to estimate:

# For statevector simulation: you need 2ⁿ complex amplitudes for n qubits.

# Each amplitude ≈ 16 bytes (complex128). So, required RAM ≈ 2**n * 16 bytes.

# Example:

# 20 qubits: 2^20 ≈ 1 million amplitudes → ≈ 16 MB.

# 30 qubits: 2^30 ≈ 1 billion amplitudes → ≈ 16 GB.

# 50 qubits: 2^50 ≈ petabytes! (infeasible for classical simulation).
def memory_load(ionq_circuit_Z, midcircuit_Z, n_max):
  n_qubits1 = []
  statevector_MB1=[]
  n_qubits2 = []
  statevector_MB2=[]
  for n in range(1, n_max+1):
   qc1 = ionq_circuit_Z(n)
   qc2 = midcircuit_Z(n)
   n_qubits_1 = qc1.num_qubits
   statevector_bytes_1 = (2**n_qubits_1) * 16
   statevector_MB_1 = statevector_bytes_1 / (1024 ** 2)
   n_qubits_2 = qc2.num_qubits
   statevector_bytes_2 = (2**n_qubits_2) * 16
   statevector_MB_2 = statevector_bytes_2 / (1024 ** 2)
   statevector_MB1.append(statevector_MB_1)
   statevector_MB2.append(statevector_MB_2)

  return statevector_MB1, statevector_MB2