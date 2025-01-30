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
100 1010000100000111
101 0111001000000000
102 0111000000100000
103 0001000100000110
104 0011000100001000
105 0111000000000001
106 0000000001010011
107 1111111111101001
108 0000000000000000
```

---

## 📷 Flowcharts

### **1️⃣ First Pass - Symbol Table Generation**
![Screenshot 2025-01-30 164124](https://github.com/user-attachments/assets/dd01fe6e-e8a0-4d23-b073-f4416b470810)


### **2️⃣ Second Pass - Machine Code Generation**
![Screenshot 2025-01-30 164141](https://github.com/user-attachments/assets/fbd85ac0-7c25-43fd-8698-446e8145645f)


### **3️⃣ Example**
![Screenshot 2025-01-30 164306](https://github.com/user-attachments/assets/dcd4aca0-d896-400f-ad85-2d067dc509ee)
![Screenshot 2025-01-30 164528](https://github.com/user-attachments/assets/56496ca9-8900-42c9-8d8c-c421fe3e2ee3)




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

## 🤝 Contributing

Feel free to submit **pull requests** or report any issues. Let's improve this assembler together! 🚀

## 📜 License

This project is licensed under the MIT License.

---

🔥 **Happy Coding!**

