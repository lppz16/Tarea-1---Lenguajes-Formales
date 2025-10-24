# ST0270 - Formal Languages and Compilers  
## Assignment 2: Left Recursion Elimination  

**Authors:** Yan Frank Ríos López & Diego Alejandro Angarita Arboleda
**Class:** SI2002-5730 – Formal Languages and Compilers  
**Institution:** Universidad EAFIT  
**Professor:** César Guerra
**Date:** 23/10/2025  

---

### 📘 Description  

This program implements the algorithm for eliminating **direct and indirect left recursion** from context-free grammars, as described in  
*Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D. (2006). Compilers: Principles, Techniques, and Tools (2nd Edition), Section 4.3.3.*

The program reads one or more grammars from the standard input and outputs equivalent grammars **without left recursion**, following the exact format required by the assignment.

---

### 🧠 Algorithm Explanation  

The algorithm eliminates both **indirect** and **immediate** left recursion from a given grammar.  

**Steps:**  

1. For each nonterminal `Ai` in the input order:
   - For every previously processed nonterminal `Aj (j < i)`, replace any production of the form `Ai → Ajγ` by expanding `Aj`’s productions (`Aj → δ`), resulting in `Ai → δγ`.
2. After indirect recursion is handled, remove **immediate left recursion** by transforming rules of the form:

A → Aα | β
becomes
A → βZ
Z → αZ | e

### 🧰 System Information
- **Operating System:** Ubuntu 22.04 / Windows 10  
- **Python Version:** 3.11  
- **Editor:** Visual Studio Code  
- **Execution Environment:** GitHub Classroom


Here, **`e`** represents the empty string (ε).  

This algorithm ensures the resulting grammar is **equivalent** to the original but free of left recursion, making it suitable for top-down parsing techniques such as LL(1).

---

### ⚙️ Input Format  

The program reads from the **standard input (stdin)** with the following structure:

1. A number `n > 0` — the number of cases (grammars).  
2. For each case:
- A number `k > 0` — the number of nonterminals.  
- Then `k` lines, each representing a production rule in the format:
  ```
  <Nonterminal> -> <derivations separated by spaces>
  ```

**Notes:**  
- Nonterminals are uppercase letters (A–Z).  
- Terminals are lowercase letters (a–z).  
- `e` represents ε (the empty string).  
- The input contains no cycles or ε-productions.  

---

### 🖥️ Output Format  

For each grammar, the program prints an **equivalent grammar without left recursion**, preserving the same structure and order.  
Each case is separated by a **blank line**.

Example:
S -> bZ
Z -> aZ e

### ▶️ How to Run
1. Save your grammar in a text file named `input.txt`.  
2. Run the program from the terminal:

   ```bash
   python3 main.py < input.txt > output.txt

#### Example command:
python3 main.py < examples/input1.txt > examples/output1.txt


### Example Input

3

1
S -> Sa b

2
S -> Aa b
A -> Ac Sd m

2
S -> Sa Ab
A -> Ac Sc c

### Example output

S -> bA
A -> aA e

S -> Aa b
A -> bdB mB
B -> cB adB e

S -> AbB
B -> aB e
A -> cC
C -> cC bBcC e



