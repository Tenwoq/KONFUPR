import sys
import xml.etree.ElementTree as ET

class ConfigGenerator:
    def __init__(self, xml_data):
        try:
            self.root = ET.fromstring(xml_data)
        except ET.ParseError as e:
            raise ValueError(f"XML синтаксическая ошибка: {e}")

    def convert(self):
        print("Начинаем преобразование XML в конфигурацию...")
        result = self._process_element(self.root, indent_level=0)
        print("Преобразование завершено.\n")
        return result

    def _process_element(self, element, indent_level):
        indent = '    ' * indent_level
        print(f"Обрабатываем элемент: {element.tag}")  # Отладочное сообщение для каждого элемента

        # Обработка корневого элемента или любых других контейнеров
        if element.tag == "config":
            result = ""
            for child in element:
                result += self._process_element(child, indent_level) + "\n"
            return result
        
        # Прочие теги
        elif element.tag == "dict":
            return self._process_dict(element, indent_level)
        elif element.tag == "array":
            return self._process_array(element, indent_level)
        elif element.tag == "string":
            return f"q({element.text})" if element.text else ""
        elif element.tag == "number":
            return element.text
        elif element.tag == "def":
            return self._process_def(element, indent_level)
        elif element.tag == "eval":
            return f"{indent}|{element.text}|"
        elif element.tag == "comment":
            return self._process_comment(element)
        elif element.tag == "entry":
            return self._process_entry(element, indent_level + 1)
        else:
            print(f"Неизвестный тег: {element.tag}")
            return ""

    def _process_dict(self, element, indent_level):
        indent = '    ' * indent_level
        result = f"{indent}@{{\n"
        for child in element:
            if child.tag == "entry":
                result += self._process_entry(child, indent_level + 1) + "\n"
        result += f"{indent}}}"
        return result

    def _process_entry(self, element, indent_level):
        indent = '    ' * indent_level
        name = element.get('name')
        value = self._process_element(element[0], indent_level) if len(element) > 0 else ""
        return f"{indent}{name} = {value};"

    def _process_array(self, element, indent_level):
        indent = '    ' * indent_level
        result = f"{indent}[" + " ".join(self._process_element(child, indent_level) for child in element) + "]"
        return result

    def _process_def(self, element, indent_level):
        indent = '    ' * indent_level
        name = element.get('name')
        value = self._process_element(element[0], indent_level)
        return f"{indent}def {name} := {value};"

    def _process_comment(self, element):
        text = element.text.strip() if element.text else ""
        return f"(* {text} *)"

if __name__ == "__main__":
    # Чтение XML данных с явной установкой кодировки UTF-8
    xml_data = sys.stdin.read().encode('utf-8').decode('utf-8')
    
    generator = ConfigGenerator(xml_data)
    result = generator.convert()
    
    # Явная запись вывода в файл или консоль с кодировкой UTF-8
    sys.stdout.buffer.write(result.encode('utf-8'))
