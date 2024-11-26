import struct
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString

class Assembler:
    def __init__(self, input_file="", output_file="", log_file=""):
        self.input_file = input_file
        self.output_file = output_file
        self.log_file = log_file

    def assemble(self):
        binary_data = []
        root = ET.Element("Log")

        with open(self.input_file, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):  # Игнорируем комментарии и пустые строки
                    continue
                
                cmd, *args = line.split()
                if cmd == "LOAD_CONST":
                    a, b, c = map(int, args)
                    instruction = self.encode_load_const(a, b, c)
                    binary_data.append(instruction)
                    self.log_instruction(root, cmd, a=a, b=b, c=c)
                elif cmd == "READ_MEM":
                    a, b, c = map(int, args)
                    instruction = self.encode_read_mem(a, b, c)
                    binary_data.append(instruction)
                    self.log_instruction(root, cmd, a=a, b=b, c=c)
                elif cmd == "WRITE_MEM":
                    a, b, c, d = map(int, args)
                    instruction = self.encode_write_mem(a, b, c, d)
                    binary_data.append(instruction)
                    self.log_instruction(root, cmd, a=a, b=b, c=c, d=d)
                elif cmd == "BINARY_OP":
                    a, b, c, d = map(int, args)
                    instruction = self.encode_binary_op(a, b, c, d)
                    binary_data.append(instruction)
                    self.log_instruction(root, cmd, a=a, b=b, c=c, d=d)

        with open(self.output_file, "wb") as bf:
            bf.write(b"".join(binary_data))

        with open(self.log_file, "w", encoding="utf-8") as xml_file:
            xml_file.write(self.prettify_xml(root))

    def encode_load_const(self, a, b, c):
        instruction = (a & 0x3F) | ((b & 0x3F) << 6) | (c << 12)
        return struct.pack("<Q", instruction)[:6]

    def encode_read_mem(self, a, b, c):
        instruction = (a & 0x3F) | ((b & 0x3F) << 6) | (c << 12)
        return struct.pack("<Q", instruction)[:6]

    def encode_write_mem(self, a, b, c, d):
        instruction = (a & 0x3F) | ((b & 0x3FFF) << 6) | ((c & 0x3F) << 20) | ((d & 0x3F) << 26)
        return struct.pack("<Q", instruction)[:6]

    def encode_binary_op(self, a, b, c, d):
        instruction = (a & 0x3F) | ((b & 0x3F) << 6) | ((c & 0x3F) << 12) | ((d & 0x3FFF) << 18)
        return struct.pack("<Q", instruction)[:6]

    def log_instruction(self, root, cmd, **kwargs):
        instr = ET.SubElement(root, "Instruction", Command=cmd)
        for key, value in kwargs.items():
            ET.SubElement(instr, key).text = str(value)

    def prettify_xml(self, element):
        raw_string = ET.tostring(element, encoding="unicode")
        parsed = parseString(raw_string)
        return parsed.toprettyxml(indent="  ")

if __name__ == "__main__":
    assembler = Assembler("program.txt", "output.bin", "log.xml")
    assembler.assemble()
