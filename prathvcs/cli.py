# prathvcs/cli.py

import argparse
from prathvcs.repository import Repository
from prathvcs.commit import Commit
from prathvcs.status import Status
from prathvcs.help import show_help

def main():
    """Main function to parse arguments and execute commands."""
    parser = argparse.ArgumentParser(description='prathvcs - A Simplified Version Control System', add_help=False)
    subparsers = parser.add_subparsers(dest='command')

    # Define subparsers for each command
    subparsers.add_parser('init')
    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('filename')

    commit_parser = subparsers.add_parser('commit')
    commit_parser.add_argument('-m', '--message', required=True)

    subparsers.add_parser('log')
    subparsers.add_parser('status')

    checkout_parser = subparsers.add_parser('checkout')
    checkout_parser.add_argument('commit_id')

    subparsers.add_parser('help')

    args = parser.parse_args()

    repo = Repository()

    if args.command == 'init':
        repo.init()
    elif args.command == 'add':
        repo.add(args.filename)
    elif args.command == 'commit':
        commit = Commit(args.message, repo)
        commit.make_commit()
    elif args.command == 'status':
        status = Status(repo)
        status.show_status()
    elif args.command == 'log':
        # Implement log functionality here
        pass
    elif args.command == 'checkout':
        # Implement checkout functionality here
        pass
    elif args.command == 'help' or args.command is None:
        show_help()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
