import argparse
from .git_wrapper import create_branch, list_branches, merge_branch, commit_changes, init_repo

def main():
    parser = argparse.ArgumentParser(description="RADFIRST Git Wrapper CLI")
    subparsers = parser.add_subparsers(dest='command')

    create_parser = subparsers.add_parser('create', help='Create a new branch')
    create_parser.add_argument('branch', help='Name of the branch to create')

    list_parser = subparsers.add_parser('list', help='List all branches')

    merge_parser = subparsers.add_parser('merge', help='Merge a branch into the current branch')
    merge_parser.add_argument('source_branch', help='Branch to merge into the current branch')

    commit_parser = subparsers.add_parser('commit', help='Commit staged changes with a message')
    commit_parser.add_argument('message', help='Commit message')

    init_parser = subparsers.add_parser('init', help='Initialize a new git repository')

    args = parser.parse_args()

    if args.command == 'create':
        print(create_branch(args.branch))
    elif args.command == 'list':
        print(list_branches())
    elif args.command == 'merge':
        print(merge_branch(args.source_branch))
    elif args.command == 'commit':
        print(commit_changes(args.message))
    elif args.command == 'init':
        print(init_repo())
    else:
        parser.print_help()
