from qiskit_aer.noise import NoiseModel, ReadoutError, depolarizing_error ,pauli_error


#noise model that mimics aria-1 to be used with Aer simulator

def build_noise_aria1():
    noise = NoiseModel()
    # Aria‑1 error rates
    r1q = 0.0005      # 1-qubit gate depolarization
    r2q = 0.0133      # 2-qubit gate depolarization

    # Define gate sets
    one_q_gates = ['h', 'sdg', 's', 'x', 'y', 'z', 'sx', 'rz']
    two_q_gates = ['cx']

    # Add depolarizing errors after gates
    noise.add_all_qubit_quantum_error(depolarizing_error(r1q, 1), one_q_gates)
    noise.add_all_qubit_quantum_error(depolarizing_error(r2q, 2), two_q_gates)

    # Add reset error: small chance to flip reset qubit
    noise.add_all_qubit_quantum_error(pauli_error([('X', 0.001), ('I', 0.999)]), ['reset'])

    # Measurement (readout) error
    p_meas = 0.02  # ~2% readout error
    ro_error = ReadoutError([[1 - p_meas, p_meas], [p_meas, 1 - p_meas]])
    noise.add_all_qubit_readout_error(ro_error)

    return noise