# prathvcs/log.py

import os
import json

class Log:
    def __init__(self, repo):
        self.repo = repo

    def show_log(self):
        """Displays the commit history."""
        if not os.path.exists(self.repo.repo_path):
            print("Not a prathvcs repository. Run 'prathvcs init' first.")
            return
        with open(self.repo.index_file, 'r') as f:
            index = json.load(f)
        commits = index['commits']
        if not commits:
            print("No commits yet.")
            return
        for commit in reversed(commits):
            print(f"Commit ID: {commit['id']}")
            print(f"Timestamp: {commit['timestamp']}")
            print(f"Message: {commit['message']}")
            print("-" * 40)
