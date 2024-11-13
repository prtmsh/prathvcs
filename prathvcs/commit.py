# prathvcs/commit.py

import os
import json
import shutil
from datetime import datetime
import uuid

class Commit:
    def __init__(self, message, repo):
        self.message = message
        self.repo = repo
        self.commit_id = str(uuid.uuid4())[:8]  # Generate a unique ID
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def make_commit(self):
        """Creates a commit by saving staged files and updating the index."""
        if not os.path.exists(self.repo.repo_path):
            print("Not a prathvcs repository. Run 'prathvcs init' first.")
            return
        if not os.listdir(self.repo.staging_area):
            print("No changes added to commit. Use 'prathvcs add <file>' to track files.")
            return
        commit_path = os.path.join(self.repo.commits_dir, self.commit_id)
        os.makedirs(commit_path)
        # Copy files from staging area to the commit directory
        for filename in os.listdir(self.repo.staging_area):
            src_file = os.path.join(self.repo.staging_area, filename)
            dst_file = os.path.join(commit_path, filename)
            shutil.copy2(src_file, dst_file)
        # Update index.json with the new commit
        with open(self.repo.index_file, 'r') as f:
            index = json.load(f)
        index['commits'].append({
            'id': self.commit_id,
            'timestamp': self.timestamp,
            'message': self.message
        })
        with open(self.repo.index_file, 'w') as f:
            json.dump(index, f, indent=4)
        # Clear the staging area
        shutil.rmtree(self.repo.staging_area)
        os.makedirs(self.repo.staging_area)
        print(f"[{self.commit_id}] {self.message}")