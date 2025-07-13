# 🚀 Wells Fargo Global Industry Challenge – Phase 3  
**Team: Feynman Prodigies**

## 🧠 1. Final Circuit Execution and Output Validation

### ✅ Mid-Circuit Measurement Logic: Mathematical Modeling

We begin by analyzing the **conditional evolution** of an ideal mid-circuit measurement circuit. The goal is to demonstrate the **mathematical equivalence** between mid-circuit measurements and our **deferred measurement** implementation.

---

### 📐 Initial State Preparation

- Two data qubits:  
  \[
  |x_0⟩ = α|0⟩ + β|1⟩,\quad |\alpha|^2 + |\beta|^2 = 1
  \]
- Ancilla initialized as \(|0⟩\)
- Joint input:  
  \[
  |Ψ_{in}⟩ = |x_0⟩_1 \otimes |x_0⟩_2 \otimes |0⟩_3
  \]
- Unitary used:  
  \[
  U = \text{CNOT}_{1→3} \cdot \text{CNOT}_{1→2} \cdot (H_1 \otimes I_2 \otimes I_3)
  \]

### 🔁 Conditional Evolution Through Rounds

- The recursive relationship is:
  \[
  (q_n, r_n) = 
  \begin{cases}
  (0, r_{n-1}) & \text{if } y_n = 0 \\
  (1, \tilde{r}_{n-1}) & \text{if } y_n = 1
  \end{cases}
  \]

---

## 🧪 2. Deferred Measurement: Implementation and Equivalence

### 🔁 Protocol Overview

Using ancilla registers \( E_1, \dots, E_n \), we replicate the measurement logic without explicit mid-circuit resets:

\[
U_{123} |q_{k-1}, r_{k-1}, 0⟩ \rightarrow |q'_k, r'_k, q_k⟩
\]

### 🧾 Deferred Measurement Sequence

1. Apply unitary `U`
2. Store the result in ancilla via:
   - `CNOT_3→Ek`
   - `CNOT_Ek→3`

Final ancilla states hold coherent record of classical outcomes. Measuring ancillas retrieves identical results to the original mid-circuit protocol.

### ✅ **Proof of Equivalence**:  
Both mid-circuit and deferred approaches produce the same output state on qubits 1 and 2.

---

### 📊 Fidelity Validation

![Fidelity Plot](./images/fidelity_plot.png)

- **Figure 1a**: Circuit for input \( y_1y_2y_3 = 001 \)  
- **Figure 1b**: Fidelity across all 3-bit combinations for \( n = 3 \) on Aer simulator  
- **Result**: Fidelity remains **1.0**, matching theoretical predictions.

---

## ⚙️ 3. Performance & Scalability Benchmarks

Benchmarked on the **IonQ simulator** (Aria-1 noise model):

### 📈 Complexity Metrics

- **Circuit Depth** (Figure 2a): Linear scaling with \( n \)
- **Gate Count** (Figure 2b): Increases linearly due to ancilla control logic

### 🧠 Resource Usage

- **Memory Load** (Figure 3a): Increases with ancilla count
- **Qubit Reuse** (Figure 3b): Efficient despite lack of mid-circuit resets

![Circuit Stats](./images/circuit_scaling.png)

---

## 🌍 4. Connection to Real-World Feedback Systems

- Supports **fault-tolerant feedback** using redundant ancilla registers.
- Enables **majority voting** across ancillas to mitigate single-qubit noise.
- Bridges to:
  - **Quantum Error Correction**
  - **Quantum Sensing**
  - **Variational Algorithms (VQAs)**
  - **Hybrid QML Feedback Loops**

---

## 🛡️ 5. Error Analysis and Mitigation

### 🔬 Noise Model: Aria-1 Simulator

- Depolarizing channel with:
  - \( r_y: p = 0.0005 \)
  - \( r_{xx}: p = 0.0133 \)

### 🧪 Results

- Gradual fidelity decline with increasing \( n \)
- Conditional logic is preserved via:
  - Explicit ancilla encoding
  - Classical post-processing
  - Strong CNOT control logic

---

## ✂️ Circuit Cutting (Planned Extension)

> A placeholder for incorporating **circuit-cutting strategies**:
- Divide large circuits into smaller subcircuits
- Enable parallelism and reduced simulation cost
- Maintain measurement-conditioned logic integrity

---

## 🔮 6. Reflections and Future Extensions

### 🔧 Generalization

- Scale to deeper feedback logic and more ancillas
- Add redundancy and error detection via majority voting

### 📊 Example

\[
U = \left( \prod_{j=1}^{m} \text{CNOT}_{1→a_j} \right) \cdot \text{CNOT}_{1→2} \cdot H_1
\]

\[
|Ψ⟩ = c_0 |0, x_0, 0^m⟩ + c_1 |1, \tilde{x}_0, 1^m⟩
\]

- Only \( y = 0^m \) or \( 1^m \) possible → supports **majority error correction**

### 🤖 Quantum-Classical Hybrid Feedback

- Supports real-time updates in applications like:
  - High-frequency trading
  - Adaptive quantum optimization

---

## ✅ Conclusion

We implemented a **deferred measurement protocol** using multiple ancillas, validated its **equivalence** to mid-circuit measurements, and benchmarked its **performance and scalability**.

> This work demonstrates practical feasibility for **feedback-enabled quantum systems** and sets the stage for **fault-tolerant, adaptive quantum computation**.

---

## 📁 Supporting Materials

📌 Source code and circuit files available here:  
**[GitHub Repository Link](https://github.com/your-repo-name)**

---

## 📚 References

1. Gurevich & Blass, *Quantum circuits and deferred measurements*, [arXiv:2107.08324](https://arxiv.org/abs/2107.08324)
2. Puente et al., *State preparation via ancilla resetting*, [arXiv:2305.08641](https://arxiv.org/abs/2305.08641)
3. Iten et al., *Quantum Circuits for Isometries*, [arXiv:1501.06911](https://arxiv.org/abs/1501.06911)
4. Nagai et al., *Quantum channel decomposition*, [arXiv:2401.09734](https://arxiv.org/abs/2401.09734)



