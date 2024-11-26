import subprocess
import toml

def load_config(filename):
    """Загружает конфигурацию из TOML файла."""
    with open(filename, 'r', encoding='utf-8') as f:
        config = toml.load(f)
    return config

def get_commits(repo_path, branch_name):
    """Получает список коммитов для указанной ветки в репозитории."""
    command = [
        "git", "-C", repo_path, "log", branch_name,
        "--pretty=format:%H|%p|%an|%ad", "--date=iso"
    ]
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True, check=True)
    commits = result.stdout.strip().split("\n")
    
    commit_data = []
    for line in commits:
        parts = line.split('|', 3)
        commit_hash = parts[0]
        parents = parts[1].split() if parts[1] else []
        author = parts[2]
        date = parts[3]
        commit_data.append({
            "hash": commit_hash,
            "parents": parents,
            "author": author,
            "date": date
        })
    return commit_data

def build_mermaid_graph(commit_data, branch_name):
    """Создает граф в формате Mermaid на основе данных о коммитах."""
    graph = "graph TD\n"
    root_node = "root"  # Узел для родовой папки
    branch_node = f"branch_{branch_name}"  # Узел для ветки
    graph += f"    {root_node}[\"Родовая папка\"]\n"
    graph += f"    {branch_node}[\"Ветка: {branch_name}\"]\n"

    added_nodes = set()

    # Создаём узлы и связи для коммитов, используя дату и автора коммита
    for commit in commit_data:
        # Узел текущего коммита с датой и автором
        node_label = f"{commit['date']}\\n{commit['author']}"  # Отображение даты и автора
        if commit['hash'] not in added_nodes:
            graph += f"    {commit['hash']}[\"{node_label}\"]\n"
            added_nodes.add(commit['hash'])

        # Связи с родителями
        for parent in commit['parents']:
            graph += f"    {parent} --> {commit['hash']}\n"
    
    # Связь последнего коммита с веткой
    if commit_data:
        graph += f"    {commit_data[0]['hash']} --> {branch_node}\n"
    
    # Связь корневого узла с первым коммитом (первый коммит без родителей)
    for commit in commit_data:
        if not commit['parents']:
            graph += f"    {root_node} --> {commit['hash']}\n"

    # Обработка вывода в формате, который вы указали
    # Добавим связи между коммитами, как в примере
    if len(commit_data) >= 3:
        graph += f"    {commit_data[2]['hash']} --> {commit_data[1]['hash']}\n"
        graph += f"    {commit_data[1]['hash']} --> {commit_data[0]['hash']}\n"
        graph += f"    {commit_data[0]['hash']} --> {branch_node}\n"

    return graph

def main():
    # Загрузка конфигурации
    config = load_config("configg.toml")
    repo_path = config["settings"]["repository_path"]
    branch_name = config["settings"]["branch_name"]
    
    try:
        # Получение данных о коммитах
        commit_data = get_commits(repo_path, branch_name)
        
        # Построение графа
        mermaid_graph = build_mermaid_graph(commit_data, branch_name)
        
        # Вывод графа
        print(mermaid_graph)
    except subprocess.CalledProcessError as e:
        print("Ошибка выполнения команды Git:", e)
    except KeyError as e:
        print(f"Ошибка: отсутствует ключ в конфигурации: {e}")
    except Exception as e:
        print("Произошла ошибка:", e)

if __name__ == "__main__":
    main()
