import subprocess
import yaml
import sys
from packaging.requirements import Requirement
from pip._internal.resolution.resolvelib.resolver import Resolver
from pip._internal.req.constructors import install_req_from_line
from pip._internal.resolution.base import InstallRequirement
import logging

# Настройка логгирования (полезно для отладки)
logging.basicConfig(level=logging.INFO)


def load_config(filename):
    """Загружает конфигурацию из YAML файла."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        return config
    except FileNotFoundError:
        logging.error(f"Ошибка: Файл конфигурации '{filename}' не найден.")
        return None
    except yaml.YAMLError as e:
        logging.error(f"Ошибка в формате YAML файла '{filename}': {e}")
        return None


def get_dependencies(package_name, max_depth):
    """Получает зависимости Python-пакета с заданной глубиной."""
    try:
        resolver = Resolver(
            finder=None,  # We don't use this
            preparer=None,  # We don't use this
            make_install_req=install_req_from_line,
            session=None,  # We don't use this
            wheel_cache=None,  # We don't use this
            use_user_site=False
        )
        req = install_req_from_line(package_name)
        result = resolver.resolve([req])

        dependencies = {}

        def traverse(req, depth):
            if depth == 0:
                return
            dependencies[req.name] = []
            for dep in result:
                if isinstance(dep, InstallRequirement) and dep.name != req.name:
                    dependencies[req.name].append(dep.name)
                    traverse(dep, depth - 1)

        traverse(req, max_depth)
        return dependencies

    except Exception as e:
        logging.error(f"Ошибка при получении зависимостей: {e}")
        return None


def build_mermaid_graph(dependencies):
    """Создает граф в формате Mermaid."""
    graph = "graph LR\n"
    for package, deps in dependencies.items():
        graph += f"    {package}[{package}]\n"
        for dep in deps:
            graph += f"    {package} --> {dep}\n"
    return graph


def visualize_graph(mermaid_graph, visualization_tool_path):
    """Визуализирует граф."""
    if visualization_tool_path:
        try:
            subprocess.run([visualization_tool_path, "-i", "text", "-o", "graph.png"], input=mermaid_graph, text=True, check=True)
            print("Граф сохранен в graph.png")
        except FileNotFoundError:
            logging.warning("Программа для визуализации не найдена. Выводится текстовое представление.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Ошибка визуализации: {e}")
    else:
        logging.info("Программа для визуализации не указана. Выводится текстовое представление.")
    print(mermaid_graph)


def main():
    config = load_config("config.yaml")
    if config is None:
        return

    package_name = config.get("package_name")
    max_depth = config.get("max_depth", 2)  # Установка значения по умолчанию
    visualization_tool_path = config.get("visualization_tool_path")

    if not package_name:
        logging.error("Ошибка: Ключ 'package_name' отсутствует в конфигурационном файле.")
        return

    dependencies = get_dependencies(package_name, max_depth)
    if dependencies is None:
        return

    mermaid_graph = build_mermaid_graph(dependencies)
    visualize_graph(mermaid_graph, visualization_tool_path)


if __name__ == "__main__":
    main()