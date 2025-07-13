from qiskit import transpile



def BaseXCounts(backend, sim, n_max, ionq_circuit_X, midcircuit_X):
 all_counts1_X = {}
 all_counts2_X = {}

 
 for n in range(1, n_max + 1):
    transpiled_qc = transpile(ionq_circuit_X(n), backend=backend, optimization_level=3)
    trans_qc = transpile(midcircuit_X(n), sim, optimization_level=3)
    result1 = backend.run(transpiled_qc, shots=1000)
    job = sim.run(trans_qc, shots=1000)
    #result1 = job_native.result()
    result2 = job.result()
    counts1 = result1.get_counts()
    counts2 = result2.get_counts()
    all_counts1_X[n] = counts1
    all_counts2_X[n] = counts2

 return all_counts1_X, all_counts2_X   

def BaseYCounts(backend, sim, n_max, ionq_circuit_Y, midcircuit_Y):
  all_counts1_Y = {}
  all_counts2_Y = {}
  for n in range(1, n_max + 1):
    transpiled_qc = transpile(ionq_circuit_Y(n), backend=backend, optimization_level=3)
    trans_qc = transpile(midcircuit_Y(n), sim, optimization_level=3)
    result1 = backend.run(transpiled_qc, shots=1000)
    job = sim.run(trans_qc, shots=1000)
    #result1 = job_native.result()
    result2 = job.result()
    counts1 = result1.get_counts()
    counts2 = result2.get_counts()
    all_counts1_Y[n] = counts1
    all_counts2_Y[n] = counts2

  return all_counts1_Y, all_counts2_Y 


def BaseZCounts(backend, sim, n_max, ionq_circuit_Z, midcircuit_Z):
  all_counts1_Z = {}
  all_counts2_Z = {}
  for n in range(1, n_max + 1):
    transpiled_qc = transpile(ionq_circuit_Z(n), backend=backend, optimization_level=3)
    trans_qc = transpile(midcircuit_Z(n), sim, optimization_level=3)
    result1 = backend.run(transpiled_qc, shots=1000)
    job = sim.run(trans_qc, shots=1000)
    #result1 = job_native.result()
    result2 = job.result()
    counts1 = result1.get_counts()
    counts2 = result2.get_counts()
    all_counts1_Z[n] = counts1
    all_counts2_Z[n] = counts2

  return all_counts1_Z, all_counts2_Z  