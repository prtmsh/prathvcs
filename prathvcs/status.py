# prathvcs/status.py

import os
import json
import filecmp

class Status:
    def __init__(self, repo):
        self.repo = repo

    def show_status(self):
        """Displays the status of the repository."""
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
                print("Warning: Tracked file '{}' has been deleted.".format(filename))

        # Identify untracked files
        for filename in os.listdir('.'):
            if filename not in tracked_files and filename != '.prathvcs':
                untracked_files.append(filename)

        # Display status
        print("Staged files:")
        for file in staged_files:
            print("  {}".format(file))
        print("\nModified files:")
        for file in modified_files:
            print("  {}".format(file))
        print("\nUntracked files:")
        for file in untracked_files:
            print("  {}".format(file))