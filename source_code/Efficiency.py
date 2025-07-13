def efficiency(qc):
    resets = qc.count_ops().get("reset", 0)
    return (resets + qc.num_qubits) / qc.num_qubits

def reuse_efficiency(ionq_circuit_Z, midcircuit_Z, n_max):
  deferred_ones = []
  measured_ones = []
  for n in range(1, n_max+1):
   qc1 = ionq_circuit_Z(n)
   qc2 = midcircuit_Z(n)
   deferred_efficiency = efficiency(qc1)
   midcircuit_efficiency = efficiency(qc2)
   deferred_ones.append(deferred_efficiency)
   measured_ones.append(midcircuit_efficiency)

  return deferred_ones, measured_ones