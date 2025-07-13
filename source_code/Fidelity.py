from itertools import product
from qiskit.quantum_info import DensityMatrix, state_fidelity
import numpy as np

def fidelity(qiskit_counts_Z, qiskit_counts_X, qiskit_counts_Y, ionq_counts_Z, ionq_counts_X, ionq_counts_Y, n_max):

 # Pauli operators
 pauli_labels = ['I', 'X', 'Y', 'Z']
 pauli_ops = {
    'I': np.array([[1, 0], [0, 1]]),
    'X': np.array([[0, 1], [1, 0]]),
    'Y': np.array([[0, -1j], [1j, 0]]),
    'Z': np.array([[1, 0], [0, -1]])}

 def get_parity(bits):
    return (-1) ** (bits.count('1') % 2)

 def estimate_expectation(counts, system_idxs):
    total = sum(counts.values())
    if total == 0:
        return 0.0
    acc = 0.0
    for bitstring, count in counts.items():
        bits = ''.join(bitstring[i] for i in system_idxs)
        acc += get_parity(bits) * count
    return acc / total

 def filter_counts_for_ancilla(counts_dict, ancilla_bits):
    return {k: v for k, v in counts_dict.items() if k.endswith(ancilla_bits)}

 def reconstruct_density_matrix(counts_Z, counts_X, counts_Y, n, ancilla_bits, system_idxs=[0, 1]):
    rho = np.zeros((4, 4), dtype=complex)
    for p1, p2 in product(pauli_labels, repeat=2):
        if p1 == 'I' and p2 == 'I':
            coeff = 1.0
        else:
            if 'Y' in (p1, p2):
                counts_basis = filter_counts_for_ancilla(counts_Y.get(n, {}), ancilla_bits)
            elif 'X' in (p1, p2):
                counts_basis = filter_counts_for_ancilla(counts_X.get(n, {}), ancilla_bits)
            else:
                counts_basis = filter_counts_for_ancilla(counts_Z.get(n, {}), ancilla_bits)
            coeff = estimate_expectation(counts_basis, system_idxs)
        op = np.kron(pauli_ops[p1], pauli_ops[p2])
        rho += coeff * op
    rho /= 4
    # Force to physical
    rho = (rho + rho.conj().T) / 2
    eigvals, eigvecs = np.linalg.eigh(rho)
    eigvals = abs(eigvals) #np.clip(eigvals, 0, None)
    rho = eigvecs @ np.diag(eigvals) @ eigvecs.conj().T
    rho /= np.trace(rho)
    return DensityMatrix(rho)

 def compute_avg_fidelity(counts_Z_q, counts_X_q, counts_Y_q,
                         counts_Z_i, counts_X_i, counts_Y_i,
                         n, system_idxs=[0,1]):
    ancilla_set = set(k[-n:] for k in counts_Z_q[n])
    total_shots = sum(counts_Z_q[n].values())
    avg_fid = 0.0
    details = []

    for a in ancilla_set:
        p_a = sum(v for k, v in counts_Z_q[n].items() if k.endswith(a)) / total_shots
        if p_a == 0:
            continue
        try:
            rho_q = reconstruct_density_matrix(counts_Z_q, counts_X_q, counts_Y_q, n, a, system_idxs)
            rho_i = reconstruct_density_matrix(counts_Z_i, counts_X_i, counts_Y_i, n, a, system_idxs)
            f = state_fidelity(rho_q, rho_i)
        except:
            f = 0.0
        avg_fid += p_a * f
        details.append((a, f, p_a))

    return avg_fid, details


 fidelity_per_round = {}
 all_details = {}

 for n in range(1, n_max+1):
    fid, details = compute_avg_fidelity(
        qiskit_counts_Z, qiskit_counts_X, qiskit_counts_Y,
        ionq_counts_Z, ionq_counts_X, ionq_counts_Y,
        n, system_idxs=[0, 1]
    )
    fidelity_per_round[n] = fid
    all_details[n] = details

 return fidelity_per_round 

