# prathvcs/repository.py

import os
import json
import shutil

class Repository:
    def __init__(self, path='.'):
        self.repo_path = os.path.join(path, '.prathvcs')
        self.staging_area = os.path.join(self.repo_path, 'staging_area')
        self.commits_dir = os.path.join(self.repo_path, 'commits')
        self.index_file = os.path.join(self.repo_path, 'index.json')

    def init(self):
        """Initializes a new repository by creating necessary directories and files."""
        if not os.path.exists(self.repo_path):
            os.makedirs(self.repo_path)
            os.makedirs(self.staging_area)
            os.makedirs(self.commits_dir)
            with open(self.index_file, 'w') as f:
                json.dump({'tracked_files': [], 'commits': []}, f, indent=4)
            print(f"Initialized empty prathvcs repository in {self.repo_path}")
        else:
            print("Repository already initialized.")

    def add(self, filename):
        """Adds a file to the staging area for tracking."""
        if not os.path.exists(filename):
            print(f"File '{filename}' does not exist.")
            return
        if not os.path.exists(self.repo_path):
            print("Not a prathvcs repository. Run 'prathvcs init' first.")
            return
        shutil.copy2(filename, self.staging_area)
        with open(self.index_file, 'r') as f:
            index = json.load(f)
        if filename not in index['tracked_files']:
            index['tracked_files'].append(filename)
        with open(self.index_file, 'w') as f:
            json.dump(index, f, indent=4)
        print(f"Added '{filename}' to staging area.")