# prathvcs/help.py

def show_help():
    """Displays help information for each command."""
    help_text = """
prathvcs - A Simplified Version Control System

Usage:
  prathvcs init                   Initialize a new repository
  prathvcs add <filename>         Add a file to the staging area
  prathvcs commit -m "message"    Commit staged changes with a message
  prathvcs log                    Display commit history
  prathvcs status                 Show the working tree status
  prathvcs checkout <id>          Switch to a specific commit
  prathvcs help                   Show this help message

Examples:
  prathvcs init
  prathvcs add example.txt
  prathvcs commit -m "Initial commit"
  prathvcs log
  prathvcs status
  prathvcs checkout a1b2c3d4
"""
    print(help_text)
