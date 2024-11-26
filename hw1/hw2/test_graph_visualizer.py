import unittest
from graph_visualizer import load_config, get_commits, build_mermaid_graph

class TestGraphVisualizer(unittest.TestCase):
    
    def test_load_config(self):
        config = load_config("config.toml")
        self.assertIn("repository_path", config)
        self.assertIn("branch_name", config)

    def test_get_commits(self):
        # Пример использования временного репозитория для теста
        repo_path = "/path/to/test/repo"
        branch_name = "main"
        commits = get_commits(repo_path, branch_name)
        self.assertIsInstance(commits, list)
        if commits:
            self.assertIn("hash", commits[0])
            self.assertIn("parents", commits[0])
            self.assertIn("author", commits[0])
            self.assertIn("date", commits[0])

    def test_build_mermaid_graph(self):
        commit_data = [
            {"hash": "a1b2c3", "parents": ["d4e5f6"], "author": "Alice", "date": "2024-11-01 12:00:00"},
            {"hash": "d4e5f6", "parents": [], "author": "Bob", "date": "2024-10-30 08:00:00"}
        ]
        mermaid_graph = build_mermaid_graph(commit_data)
        self.assertIn("a1b2c3", mermaid_graph)
        self.assertIn("d4e5f6", mermaid_graph)
        self.assertIn("a1b2c3 --> d4e5f6", mermaid_graph)

if __name__ == "__main__":
    unittest.main()
