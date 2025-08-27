# 📘 Assignment 1 – DFA Minimization

**Course:** ST0270 – Formal Languages  
**Assignment:** #1  
**Students:**  
- Diego Alejandro Angarita Arboleda  
- Yan Frank Ríos López  
**Class number:** C2566-SI2002-5730  
**Operating System:** Windows 11  
**Programming Language:** Python 3  

---

## 📌 Description  
This project implements the **deterministic finite automata (DFA) minimization algorithm** presented in *Kozen (1997), Lecture 14*.  
The program takes as input the definition of a DFA (without unreachable states) and determines the **equivalent states** that can be merged.  
Finally, it prints the pairs of equivalent states in lexicographic order.  

---

## 📥 Input Format  
1. One line with a number `c > 0` indicating the number of test cases.  
2. For each case:  
   - One line with `n > 0`, the number of DFA states.  
   - One line with the alphabet symbols separated by spaces.  
   - One line with the final states separated by spaces.  
   - `n` lines, each describing a row of the transition table for a state.  
     The symbols appear in the same order as they were listed in the alphabet line.  

---

## 📤 Output Format  
For each case, the program prints the **pairs of equivalent states** in lexicographic order.  
- The pairs are printed as `(p,q)` separated by spaces.  
- If there are no equivalent pairs, a blank line is printed.  

---

## ▶️ Execution Instructions  
To make running the program easier, it is recommended to download PyCharm (https://www.jetbrains.com/pycharm/download/?section=windows) or use online tools such as Replit (https://replit.com/).  

### 1. Clone the repository  
```bash
git clone <your-repo-url>
cd <repo-folder>

