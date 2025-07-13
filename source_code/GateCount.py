

def gate_count(ionq_circuit_Z, midcircuit_Z, n_max):
  gate_counts1 = []
  gate_counts2 = []
  for n in range(1, n_max+1):
   qc1 = ionq_circuit_Z(n)
   qc2 = midcircuit_Z(n)
   gate_count1 = sum(qc1.count_ops().values())
   gate_count2 = sum(qc2.count_ops().values())
   gate_counts1.append(gate_count1)
   gate_counts2.append(gate_count2)

  return gate_counts1, gate_counts2