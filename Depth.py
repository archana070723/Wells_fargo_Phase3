
def depth(ionq_circuit_Z, midcircuit_Z, n_max):
  depths1 = []
  depths2 = []

  for n in range(1, n_max+1):
   qc1 = ionq_circuit_Z(n)
   qc2 = midcircuit_Z(n)
   depth1 = qc1.depth()
   depth2 = qc2.depth()
   depths1.append(depth1)
   depths2.append(depth2)

  return depths1, depths2 