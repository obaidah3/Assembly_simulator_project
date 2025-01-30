# Assembly_simulator_project
# Two-Pass Assembler Simulator

This project is a **Two-Pass Assembler** that converts assembly language instructions into machine code. It simulates how an assembler processes assembly programs by generating a **Symbol Table** and then translating instructions into **binary machine code**.

## 🚀 Features

- **Two-Pass Assembly Process** (First Pass & Second Pass)
- **Symbol Table Generation**
- **Instruction Encoding to Machine Code**
- **Support for Decimal (DEC) and Hexadecimal (HEX) Values**
- **Indirect Addressing Mode Support**

## 🛠 How It Works

The assembler follows a **two-pass approach**:

### 🔹 First Pass: Symbol Table Creation

1. Reads the assembly source code.
2. Identifies **labels (variables/constants)** and assigns their addresses.
3. Builds a **Symbol Table**.
4. Skips instruction encoding in this step.

### 🔹 Second Pass: Machine Code Generation

1. Reads the code again.
2. Converts each instruction into **binary machine code**.
3. Uses the **Symbol Table** to replace labels with addresses.
4. Outputs the **final machine code**.

---

## 📜 Example Assembly Code

Below is a sample assembly program processed by the assembler:

```assembly
ORG 100
LDA SUB
CMA
INC
ADD MIN
STA DIF
HLT
MIN, DEC 83
SUB, DEC -23
DIF, DEC 0
END
```

### ✅ Symbol Table (After First Pass)

```
MIN: 106
SUB: 107
DIF: 108
```

### ✅ Generated Machine Code (After Second Pass)

```
100 001010011011
101 011100000000
102 011100100000
103 000100110101
104 001110011100
105 011100000001
106 000000001010011
107 1111111111101001
108 0000000000000000
```

---

## 📷 Flowcharts

### **1️⃣ First Pass - Symbol Table Generation**



### **2️⃣ Second Pass - Machine Code Generation**



### **3️⃣ Full Assembler Process**



---

## ⚙️ How to Run

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/assembler-simulator.git
   cd assembler-simulator
   ```
2. Run the Python script:
   ```sh
   python assembler.py
   ```
3. Check the generated **Symbol Table** and **Machine Code Output**.

---

## 📝 To-Do List

-

## 🤝 Contributing

Feel free to submit **pull requests** or report any issues. Let's improve this assembler together! 🚀

## 📜 License

This project is licensed under the MIT License.

---

🔥 **Happy Coding!**

