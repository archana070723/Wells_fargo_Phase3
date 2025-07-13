# deferred circuit is built using ionq conventions and measured in the three bases
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
# X basis

def ionq_circuit_X(n_rounds):
    q = QuantumRegister(3, 'q')
    e = QuantumRegister(n_rounds, 'e')
    c = ClassicalRegister(n_rounds + 2, 'c')
    qc = QuantumCircuit(q, e, c)

    
    def U(qc):
        qc.h(q[0])  
        qc.cx(q[0], q[1])  
        qc.cx(q[0], q[2])

    for i in range(n_rounds):
        U(qc)
        qc.cx(q[2], e[i])  
        qc.cx(e[i], q[2]) 
        qc.barrier()
    
    for k in range(n_rounds):
        qc.h(q[0])
        qc.h(q[1])
        qc.h(e[k])
    
    # Measurements must be at the end
    qc.measure(q[0], c[0])
    qc.measure(q[1], c[1])
    
    for k in range(n_rounds):
        qc.measure(e[k], c[k+2])
  

    
    return qc


# Y basis

def ionq_circuit_Y(n_rounds):
    q = QuantumRegister(3, 'q')
    e = QuantumRegister(n_rounds, 'e')
    c = ClassicalRegister(n_rounds + 2, 'c')
    qc = QuantumCircuit(q, e, c)

    
    def U(qc):
        qc.h(q[0])  
        qc.cx(q[0], q[1])  
        qc.cx(q[0], q[2])

    for i in range(n_rounds):
        U(qc)
        qc.cx(q[2], e[i])  
        qc.cx(e[i], q[2])  
        qc.barrier()
    
    for k in range(n_rounds):
        qc.sdg(q[0])
        qc.h(q[0])
        qc.sdg(q[1])
        qc.h(q[1])
        qc.sdg(e[k])
        qc.h(e[k])
    
    qc.sdg(q[0])
    qc.h(q[0])
    qc.sdg(q[1])
    qc.h(q[1])
    
    # Measurements must be at the end
    for k in range(n_rounds):
        qc.measure(e[k], c[k+2])
  
    qc.measure(q[0], c[0])
    qc.measure(q[1], c[1])
    
    return qc


# Z basis

def ionq_circuit_Z(n_rounds):
    q = QuantumRegister(3, 'q')
    e = QuantumRegister(n_rounds, 'e')
    c = ClassicalRegister(n_rounds + 2, 'c')
    qc = QuantumCircuit(q, e, c)

    
    def U(qc):
        qc.h(q[0])  
        qc.cx(q[0], q[1])  
        qc.cx(q[0], q[2])

    for i in range(n_rounds):
        U(qc)
        qc.cx(q[2], e[i])  
        qc.cx(e[i], q[2])  
        qc.barrier()

    for k in range(n_rounds):
        qc.measure(e[k], c[k+2])
  
    qc.measure(q[0], c[0])
    qc.measure(q[1], c[1])
    
    return qc