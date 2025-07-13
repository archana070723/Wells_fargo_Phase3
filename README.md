# 🚀 Wells Fargo Global Industry Challenge – Phase 3  
**Team: Feynman Prodigies**

# 🌐 Global Industry Challenge — Wells Fargo Challenge – Phase 3

**Team Name**: Feynman Prodigies  

---

## 🧮 1. Final Circuit Execution and Output Validation

We begin with a mathematical analysis of an ideal **mid-circuit measurement circuit** and prove its equivalence with our **deferred measurement** approach.

### 📐 Mathematical Modeling of Conditional Evolution

Let both data qubits be initialized to:

$$\[
|x_0\rangle = \alpha |0\rangle + \beta |1\rangle, \quad |\alpha|^2 + |\beta|^2 = 1
\]$$

The ancilla is in $$\(|0\rangle\)$$, and the total input is:

$$\[
|\Psi_{\text{in}}\rangle = |x_0\rangle_1 \otimes |x_0\rangle_2 \otimes |0\rangle_3
\]$$

We define the unitary operation:

\[
U = \mathrm{CNOT}_{1 \rightarrow 3} \cdot \mathrm{CNOT}_{1 \rightarrow 2} \cdot (H_1 \otimes I_2 \otimes I_3)
\]


After application:

$$\[
|\Psi_1\rangle = c_0 |0, x_0, 0\rangle + c_1 |1, \tilde{x}_0, 1\rangle
\]$$

Where:
- $$\(c_0 = \frac{\alpha + \beta}{\sqrt{2}}, \quad c_1 = \frac{\alpha - \beta}{\sqrt{2}}\)$$
- $$\(|\tilde{x}_0\rangle = X|x_0\rangle\)$$

### 🔁 Recursive Update Rule

Each round performs:

$$\[
|\Psi_n\rangle = \frac{1}{\sqrt{2}} \left( |0, r_{n-1}, 0\rangle + (-1)^{q_{n-1}} |1, \tilde{r}_{n-1}, 1\rangle \right)
\]$$

Measurement of qubit 3 yields outcome \(y_n\), with the update:

$$\[
(q_n, r_n) =
\begin{cases}
(0, r_{n-1}) & \text{if } y_n = 0 \\
(1, \tilde{r}_{n-1}) & \text{if } y_n = 1
\end{cases}
\]$$

---

## 🌀 2. Deferred Measurement Circuit Equivalence

### 🧠 Equivalence Construction

Using ancilla registers \(E_1, \dots, E_n\), we perform the following per round:

1. Apply:  
   $$\[
   U_{123} |q_{k-1}, r_{k-1}, 0\rangle \rightarrow |q_k, r_k, q_k\rangle
   \]$$
2. Copy:  
   $$\[
   \text{CNOT}_{3 \rightarrow E_k}
   \]$$
3. Reset:  
   $$\[
   \text{CNOT}_{E_k \rightarrow 3}
   \]$$

### ✅ Equivalence Proof

Final state after these steps is:


$$\[
\frac{1}{\sqrt2}\Bigl(
\ket{0,r_{n-1},0}\ket0_{E_n}
+(-1)^{q_{n-1}}\ket{1,\widetilde r_{n-1},0}\ket1_{E_n}
\Bigr).
\]$$







Post-measurement of \(E_n\) yields identical state evolution as mid-circuit measurement. Commutation ensures all future operations remain valid.


---

## 📊 3. Performance and Scalability Benchmarks

Simulated using **IonQ backend** with **Aria-1 noise model**.

### 🔧 Circuit Complexity

| Metric             | Observation                        |
|--------------------|-------------------------------------|
| Depth              | Linear scaling with rounds \(n\)    |
| Gate Count         | Linear scaling due to ancilla ops   |
| Memory Overhead    | Increases with number of ancillas   |
| Qubit Reuse        | Efficient, avoids mid-circuit reset |



---

## 🔁 4. Real-World Feedback System Relevance

This architecture:

- Mimics real-time feedback for quantum error correction
- Supports **majority voting** for fault tolerance
- Enables **modular quantum-classical hybrid control**
- Is useful for quantum sensing and QML applications

---

## ⚠️ 5. Error Analysis and Noise Mitigation

Simulated under realistic **depolarizing noise**:

- \(r_y: p = 0.0005\)
- \(r_{xx}: p = 0.0133\)



### 🔨 Mitigation Techniques

- Use of ancilla registers for coherent outcome tracking
- Post-processing for validating outcome consistency
- Explicit CNOT structures for fault isolation
- Plans for **circuit cutting** for modular simulation

---

## 🧭 6. Reflections and Extensions

- Extend to deeper feedback loops using:
  \[
  U = \left( \prod_{j=1}^{m} \text{CNOT}_{1 \rightarrow a_j} \right) \cdot \text{CNOT}_{1 \rightarrow 2} \cdot H_1
  \]
- Use of **redundant ancilla registers** for noise mitigation
- Dynamic classical updates possible with measurement-conditioned parameters

---

## ✅ Conclusion

We demonstrate:

- A **deferred measurement circuit** architecture
- Fidelity equivalence to mid-circuit measurement
- Robustness to realistic noise and hardware constraints

The results provide a blueprint for scalable, feedback-enabled quantum systems in NISQ-era hardware.


---

## 📚 References

1. Y. Gurevich and A. Blass, *Quantum circuits with classical channels and the principle of deferred measurements*, [arXiv:2107.08324](https://arxiv.org/abs/2107.08324.)  
2. D. A. Puente et al., *Quantum state preparation via engineered ancilla resetting*, [arXiv:2305.08641](https://arxiv.org/abs/2305.08641)  
3. R. Iten et al., *Quantum Circuits for Isometries*, [arXiv:1501.06911](https://arxiv.org/abs/1501.06911)  
4. R. Nagai et al., *Quantum channel decomposition with pre- and post-selection*, [arXiv:2401.09734](https://arxiv.org/abs/2401.09734)

---



