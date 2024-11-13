# prathvcs/status.py

import os
import json
import filecmp

class Status:
    def __init__(self, repo):
        self.repo = repo

    def show_status(self):
        """Displays the status of the repository."""
        if not os.path.exists(self.repo.repo_path):
            print("Not a prathvcs repository. Run 'prathvcs init' first.")
            return
        with open(self.repo.index_file, 'r') as f:
            index = json.load(f)

        tracked_files = index['tracked_files']
        staged_files = os.listdir(self.repo.staging_area)
        modified_files = []
        untracked_files = []

        # Identify modified files
        for filename in tracked_files:
            if os.path.exists(filename):
                latest_commit = index['commits'][-1]['id'] if index['commits'] else None
                if latest_commit:
                    commit_file = os.path.join(self.repo.commits_dir, latest_commit, filename)
                    if os.path.exists(commit_file):
                        if not filecmp.cmp(filename, commit_file):
                            if filename not in staged_files:
                                modified_files.append(filename)
                else:
                    if filename not in staged_files:
                        modified_files.append(filename)
            else:
                print(f"Warning: Tracked file '{filename}' has been deleted.")

        # Identify untracked files
        for filename in os.listdir('.'):
            if filename not in tracked_files and filename != '.prathvcs':
                if os.path.isfile(filename):
                    untracked_files.append(filename)

        # Display status
        print("Staged files:")
        if staged_files:
            for file in staged_files:
                print(f"  {file}")
        else:
            print("  (no files staged)")
        print("\nModified files:")
        if modified_files:
            for file in modified_files:
                print(f"  {file}")
        else:
            print("  (no modified files)")
        print("\nUntracked files:")
        if untracked_files:
            for file in untracked_files:
                print(f"  {file}")
        else:
            print("  (no untracked files)")
