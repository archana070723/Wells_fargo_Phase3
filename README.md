# Wells Fargo Challenge – Phase 3  
## Global Industry Challenge  
### Team: Feynman Prodigies  

---

## 🧠 Project Summary

We propose and implement a **deferred measurement circuit** as an alternative to mid-circuit measurement with reset. Our approach stores measurement outcomes in ancilla qubits using coherent control operations, enabling real-time conditional logic without requiring explicit mid-circuit resets — an advantage for quantum hardware lacking fast or noise-resilient reset capabilities.

---

## 📐 Theoretical Foundation

We mathematically demonstrate the equivalence between mid-circuit measurement logic and a deferred measurement scheme via unitary control. Specifically, we model the conditional evolution of two qubits through an entangling unitary `U`, applying resets or ancilla-driven transformations over multiple rounds.

We validate:
- Theoretical evolution rules over repeated rounds.
- Equivalence using ancilla registers with controlled-CNOT gates.
- Simulation fidelity across all outcome branches.

---

## ⚙️ Implementation and Benchmarks

All simulations are run using the **IonQ simulator** and **Qiskit Aer (Aria-1 noise model)**. Key metrics analyzed:
- ✅ **Fidelity validation** (ideal and noisy)
- 📏 **Circuit depth and gate count** as a function of rounds
- 🧠 **Memory overhead and qubit reuse efficiency**

The overhead scales linearly and remains feasible for moderate depths. Results confirm that the deferred circuit behaves identically to the mid-circuit measurement model.

---

## 🧪 Error Analysis & Mitigation

We simulate the deferred circuit with noise (IonQ + Aria-1 model), including depolarizing error channels. Results show:
- Gradual fidelity decay with increased rounds
- Effective suppression of gate error propagation
- Support for future **circuit cutting** strategies and **error detection** through ancilla redundancy

---

## 🌐 Real-World Relevance

This architecture enables:
- Feedback-based quantum logic
- Noise-tolerant ancilla management
- Adaptive update loops for quantum error correction
- Application in quantum sensing and hybrid quantum-classical systems

---

## 🔬 Extensions & Future Work

We explore scaling the architecture to:
- Multi-ancilla redundant encoding for **majority voting**
- Support for dynamic control flow and adaptive quantum algorithms
- Fault-tolerant conditional operations and error correction primitives

---

## ✅ Conclusion

The proposed deferred measurement scheme:
- Matches mid-circuit logic in fidelity
- Preserves conditional evolution under noise
- Offers practical scalability for near-term devices

---

## 📁 Repository Contents

- `circuits/`: Sample Qiskit circuits (deferred + mid-circuit)
- `simulations/`: Benchmarking notebooks and plots
- `analysis/`: Fidelity, memory, and qubit reuse evaluation
- `README.md`: This file

---

## 📚 References

1. Gurevich & Blass – *Deferred Measurement Principle*, [arXiv:2107.08324](https://arxiv.org/abs/2107.08324)  
2. Puente et al. – *Ancilla Resetting*, [arXiv:2305.08641](https://arxiv.org/abs/2305.08641)  
3. Iten et al. – *Quantum Isometries*, [arXiv:1501.06911](https://arxiv.org/abs/1501.06911)  
4. Nagai et al. – *Channel Decomposition*, [arXiv:2401.09734](https://arxiv.org/abs/2401.09734)  

---

> 🚀 For simulation results and circuit validation: See [`simulations/validation.ipynb`](simulations/validation.ipynb)


