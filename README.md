

# 🌐 Global Industry Challenge — Wells Fargo Challenge – Phase 3

**Team Name**: Feynman Prodigies  
## QBraid Launch 
[<img src="https://qbraid-static.s3.amazonaws.com/logos/Launch_on_qBraid_white.png" width="150">](https://account.qbraid.com?gitHubUrl=https://github.com/archana070723/Wells_fargo_Phase3.git)
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

---
---
## 🚀 How to Run the Project
```bash
├── docs/
│   └── docs.md                # Project documentation
├── AriaNoiseModel.py         # the Aria-1 noise model
├── BaseCircuit.py            #  baseline
├── DeferredCircuit.py        # Implements deferred measurement version
├── Depth.py                  # Measures circuit depth
├── Efficiency.py             # Tracks qubit reuse efficiency
├── Fidelity.py               # Fidelity calculation utilities
├── GateCount.py              # Gate count benchmarking
├── MemoryLoad.py             # Memory tracking utilities
├── Simulation.py             # Runs simulations with given circuits and noise
├── approach.ipynb            # Colab-style notebook explaining the methodology
├── main.ipynb                # Main experimental notebook
├── README.md                 # Overview and instructions
└── requirements.txt          # Required Python packages
```

Install all required dependencies using:
```
pip install -r requirements.txt

```
Alternatively, install essential packages manually:
```
pip install pennylane qiskit qiskit-ionq qiskit-aer matplotlib numpy

```
- ▶️ Running the Project
Option 1: Use Jupyter/Colab Notebooks
Open and run either of the following notebooks:

`approach.ipynb` — for understanding the methodology
- 📊 What This File Contains
This notebook demonstrates the equivalence between mid-circuit measurement and deferred measurement using PennyLane. It constructs two quantum circuits:

`node` — Implements mid-circuit measurement with postselection and reset.

`node_defer` — Implements the deferred measurement version using entanglement with ancilla qubits followed by a final projector.

-  Key Features and Functionalities
State Initialization:
Prepares qubits using qml.StatePrep with non-uniform amplitudes.

Circuit Execution:

Repeats a Hadamard + CNOT unitary sequence for n=3 rounds.

In node, mid-circuit measurements are used with reset=True and postselect.

In node_defer, measurements are deferred by entangling with ancilla qubits and applying a final qml.Projector.

Validation:

Compares output probability distributions across all 2ⁿ postselection branches.

Uses `qml.specs()` to report gate counts, depth, and wire usage for benchmarking.

Ensures functional equivalence with:
```
np.allclose(node(state, select[i]), node_defer(state, select[i]))
```
- 📈 Plots Generated
Fidelity Comparison Plot
A bar plot comparing fidelities between the mid-circuit and deferred measurement final states across all possible measurement outcomes (2ⁿ branches).

Each bar represents fidelity for a specific bitstring outcome Yn (e.g., '000', '001', ..., '111').

`main.ipynb` — for executing simulations and generating plots

You can use Google Colab or a local Jupyter environment.

- Option 2: Run via Python Scripts
Execute any module directly for benchmarking or analysis:

✅ Ensure your terminal or IDE working directory is set to the root of the repository.
---

## 🧭 6. Reflections and Extensions

- Extend to deeper feedback loops 
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

1. Y. Gurevich and A. Blass, *Quantum circuits with classical channels and the principle of deferred measurements*,   
2. D. A. Puente et al., *Quantum state preparation via engineered ancilla resetting*, [arXiv:2305.08641](https://arxiv.org/abs/2305.08641)  
3. R. Iten et al., *Quantum Circuits for Isometries*, [arXiv:1501.06911](https://arxiv.org/abs/1501.06911)  
4. R. Nagai et al., *Quantum channel decomposition with pre- and post-selection*, 

---



