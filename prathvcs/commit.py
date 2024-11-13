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
        """Creates a commit by saving the state of all tracked files and updating the index."""
        if not os.path.exists(self.repo.repo_path):
            print("Not a prathvcs repository. Run 'prathvcs init' first.")
            return

        with open(self.repo.index_file, 'r') as f:
            index = json.load(f)

        tracked_files = index['tracked_files']

        if not tracked_files:
            print("No files to commit. Use 'prathvcs add <file>' to track files.")
            return

        commit_path = os.path.join(self.repo.commits_dir, self.commit_id)
        os.makedirs(commit_path)

        # Copy files to the commit directory
        for filename in tracked_files:
            # Determine the source of the file:
            # - If the file is in the staging area, use the version from the staging area.
            # - Otherwise, use the version from the latest commit.
            staged_file = os.path.join(self.repo.staging_area, filename)
            if os.path.exists(staged_file):
                src_file = staged_file
            else:
                # Get the file from the latest commit
                if index['commits']:
                    latest_commit_id = index['commits'][-1]['id']
                    latest_commit_path = os.path.join(self.repo.commits_dir, latest_commit_id)
                    src_file = os.path.join(latest_commit_path, filename)
                    if not os.path.exists(src_file):
                        print(f"Error: File '{filename}' not found in the latest commit.")
                        continue
                else:
                    # File is not in staging area or any previous commit
                    print(f"Error: File '{filename}' not found in staging area or previous commits.")
                    continue

            dst_file = os.path.join(commit_path, filename)
            os.makedirs(os.path.dirname(dst_file), exist_ok=True)
            shutil.copy2(src_file, dst_file)

        # Update index.json with the new commit
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
