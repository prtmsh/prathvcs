# prathvcs/checkout.py

import os
import shutil
import json

class Checkout:
    def __init__(self, repo, commit_id):
        self.repo = repo
        self.commit_id = commit_id

    def checkout_commit(self):
        """Checks out a specific commit."""
        if not os.path.exists(self.repo.repo_path):
            print("Not a prathvcs repository. Run 'prathvcs init' first.")
            return
        with open(self.repo.index_file, 'r') as f:
            index = json.load(f)
        commits = index['commits']
        commit_ids = [commit['id'] for commit in commits]
        if self.commit_id not in commit_ids:
            print(f"Commit ID '{self.commit_id}' does not exist.")
            return
        # Restore files from the commit
        commit_path = os.path.join(self.repo.commits_dir, self.commit_id)
        for filename in os.listdir(commit_path):
            src_file = os.path.join(commit_path, filename)
            dst_file = os.path.join('.', filename)
            shutil.copy2(src_file, dst_file)
        print(f"Checked out commit {self.commit_id}.")
