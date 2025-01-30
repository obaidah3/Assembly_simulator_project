'''
assembly_program version:1.8 by obaidah
CSE214:Computer Organization
'''
assembly_program = [
    "ORG 100",
    "LDA SUB I",
    "CMA",
    "INC",
    "ADD MIN",
    "STA DIF",
    "HLT",
    "MIN, DEC 83",
    "SUB, DEC -23",
    "DIF, HEX 0",
    "END"
]

symbol_table = {}  #dictionary Symbol table for labels and addresses

def firstpass(program):
    lc = 0
    for line in program:
        token = line.split()  # split the token to : token[0,1 or 2]
        if token[0] == "END":
            break
        if token[0] == "ORG":
            lc = int(token[1])  # get the address of ORG , convert it to integer and store it in location counter
            continue
        if "," in token[0]:  # check if label and handel it
            label = token[0].replace(",", "")
            symbol_table[label] = lc  # store the address with the label in the dict
            if token[1] in ["DEC", "HEX"]:
                lc += 1 # #If the line contains a label definition associated with a value (DEC or HEX):
                        #These values ​​are stored in memory as constant data.
                        # Therefore, one memory location (1 memory location) is allocated for this value.
                        # So, lc is incremented by one to reflect the reserved slot.
                continue
        lc += 1 #the reason is that each line (instruction or data) occupies one slot in memory by default.
                #If the line contains an instruction, this instruction also needs one place, so lc is incremented

firstpass(assembly_program)

print("Symbol Table:")
for label, address in symbol_table.items():
    print(f"{label}: {address}")

opcodes = {
        "AND": 0x0, "ADD": 0x1, "LDA": 0x2, "STA": 0x3,
        "BUN": 0x4, "BSA": 0x5, "ISZ": 0x6,
        "CLA": 0x7800, "CLE": 0x7400, "CMA": 0x7200, "CME": 0x7100,
        "CIR": 0x7080, "CIL": 0x7040, "INC": 0x7020,
        "SPA": 0x7010, "SNA": 0x7008, "SZA": 0x7004, "SZE": 0x7002,
        "HLT": 0x7001, "INP": 0xF800, "OUT": 0xF400,
        "SKI": 0xF200, "SKO": 0xF100, "ION": 0xF080, "IOF": 0xF040
}

indirectopcodes={
        "AND": 0x8 , "ADD": 0x9 , "LDA": 0xA, "STA": 0xB,
        "BUN": 0xC, "BSA": 0xD, "ISZ": 0xE
}

binary_output = []  # List of Final binary machine code


def secondpass(program):
    lc = 0
    for line in program:
        token = line.split() 

        if token[0] == "END":
            break

        if token[0] == "ORG":
            lc = int(token[1])  # store the address in the token[1]
            continue

        if token[0] in opcodes:  # Instruction without label
            opcode = opcodes[token[0]]  # Get opcode binary
            operand = token[1] if len(token) > 1 else ""
                #line = "LDA 45"  # مثال على سطر بلغة التجميع
                #token = line.split()  # token = ["LDA", "45"]
                #operand = token[1] if len(token) > 1 else ""  # operand = "45"

                # line = "LDA 45"  # مثال على سطر بلغة التجميع
                #token = line.split()  # token = ["LDA", "45"]
                # operand = token[1] if len(token) > 1 else ""  # operand = "45"


            if opcode < 0x7000: # check if Opcodes requiring operands memory reference
                                #all the instructions that has opcode < 0x7000 needs operand
                                #e.g.: (LDA),(STA),(ADD) needs memory address as an operand
                indirect = len(token) > 2 and token[2] == "I"  # Check for 'I' in token[2]
                address = operand
                if indirect:
                    opcode = indirectopcodes.get(token[0], opcode) if indirect else opcode
                address_binary = bin(int(str(symbol_table[address]), 16))[2:].zfill(12) 
                # Convert address(operand) to binary in 12bit , if dosn't exist it =0
                machine_code = f"{opcode:04b}{address_binary}"
                binary_output.append(f"{lc:03} {machine_code}")

            else:  # Immediate instructions (no operand required)
                machine_code = f"{opcode:016b}"
                binary_output.append(f"{lc:03} {opcode:016b}")

        elif "," in token[0]:  # #check if label
            label = token[0].replace(",", "")  # Extract label
            value_type = token[1] #hexa , decimal
            value = int(token[2], 16) if value_type == "HEX" else int(token[2]) #convert token[2] to decimal if it hexa , else concider it dec

            if value < 0:  # Handle negative values (two's complement)
                value = (1 << 16) + value
                #(1 << 16) = 2^16 = 65536 = maximum value of the 16-bit
                #2's comp = A negative number is converted by adding the value to 2^n (where n is the number of bits).
                # In this case: n = 16.

            data_binary = f"{value:016b}"  # Convert value to binary
            binary_output.append(f"{lc:03} {data_binary}")

        lc += 1  # Increment location counter

secondpass(assembly_program)

print("\nMachine Code:")
for code in binary_output:
    print(code)