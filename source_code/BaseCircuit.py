# base circuit with mid-circuit measurements is built using IBM Aer conventions and measured in the three bases
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
# X basis

def midcircuit_X(n_rounds):
    q = QuantumRegister(3, 'q')
    c = ClassicalRegister(n_rounds + 2, 'c')  
    qc = QuantumCircuit(q, c)

    for i in range(n_rounds):
        qc.h(q[0])
        qc.cx(q[0], q[1])
        qc.cx(q[0], q[2])
        qc.h(q[2])
        qc.measure(q[2], c[i+2])                    
        qc.reset(q[2])
        #qc.barrier()        
    qc.h(q[0])
    qc.h(q[1])
    qc.measure(q[0], c[0])
    qc.measure(q[1], c[1])
    
    return qc

# Y basis

def midcircuit_Y(n_rounds):
    q = QuantumRegister(3, 'q')
    c = ClassicalRegister(n_rounds + 2, 'c')  
    qc = QuantumCircuit(q, c)

    for i in range(n_rounds):
        qc.h(q[0])
        qc.cx(q[0], q[1])
        qc.cx(q[0], q[2])
        qc.sdg(q[2])
        qc.h(q[2])
        qc.measure(q[2], c[i+2])                    
        qc.reset(q[2])
        #qc.barrier()        
    qc.sdg(q[0])
    qc.h(q[0])
    qc.sdg(q[1])
    qc.h(q[1])
    qc.measure(q[0], c[0])
    qc.measure(q[1], c[1])
    
    return qc

# Z basis

def midcircuit_Z(n_rounds):
    q = QuantumRegister(3, 'q')
    c = ClassicalRegister(n_rounds + 2, 'c')  
    qc = QuantumCircuit(q, c)

    for i in range(n_rounds):
        qc.h(q[0])
        qc.cx(q[0], q[1])
        qc.cx(q[0], q[2])
        qc.measure(q[2], c[i+2])                    
        qc.reset(q[2])
        #qc.barrier()        
    
    qc.measure(q[0], c[0])
    qc.measure(q[1], c[1])
    
    return qc
