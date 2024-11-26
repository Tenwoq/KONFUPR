import struct
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString

class Interpreter:
    def __init__(self, binary_file, memory_file, memory_range):
        self.binary_file = binary_file
        self.memory_file = memory_file
        self.memory_range = memory_range
        self.memory = [0] * 65536
        self.registers = [0] * 64

    def execute(self):
        with open(self.binary_file, "rb") as bf:
            while (instruction := bf.read(6)):
                print(self.format_instruction(instruction))  # Вывод инструкции
                self.decode_and_execute(instruction)

        self.save_memory()

    def decode_and_execute(self, instruction):
        op_code = instruction[0] & 0x3F
        if op_code == 40:
            b = (instruction[0] >> 6) | (instruction[1] & 0x3F)
            c = struct.unpack("<I", instruction[2:])[0]
            self.registers[b] = self.memory[c]
        elif op_code == 41:
            b = (instruction[0] >> 6) | (instruction[1] & 0x3F)
            c = struct.unpack("<I", instruction[2:])[0]
            self.registers[b] = c
        elif op_code == 22:
            b = (instruction[0] >> 6) | ((instruction[1] & 0x3FFF) << 6)
            c = (instruction[2] >> 4) & 0x3F
            d = instruction[2] & 0x3F
            addr = self.registers[c] + b
            self.memory[addr] = self.registers[d]
        elif op_code == 7:
            b = (instruction[0] >> 6) | (instruction[1] & 0x3F)
            c = (instruction[1] >> 6) & 0x3F
            d = struct.unpack("<H", instruction[2:4])[0]
            self.registers[b] = int(self.registers[b] >= self.memory[d])

    def save_memory(self):
        root = ET.Element("Memory")
        for addr in range(*self.memory_range):
            ET.SubElement(root, "Cell", Address=str(addr)).text = str(self.memory[addr])
        with open(self.memory_file, "w", encoding="utf-8") as xml_file:
            xml_file.write(self.prettify_xml(root))

    def format_instruction(self, instruction):
        return ', '.join(f'0x{byte:02X}' for byte in instruction)

    def prettify_xml(self, element):
        raw_string = ET.tostring(element, encoding="unicode")
        parsed = parseString(raw_string)
        return parsed.toprettyxml(indent="  ")

if __name__ == "__main__":
    interpreter = Interpreter("output.bin", "memory.xml", (0, 20))
    interpreter.execute()
