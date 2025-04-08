import subprocess

def run_git_command(args):
    try:
        result = subprocess.run(['git'] + args, check=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,  # 👈 Merge stderr into stdout
                                text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stdout.strip()}" if e.stdout else f"Error: {e.stderr.strip()}"
def create_branch(branch_name):
    return run_git_command(['checkout', '-b', branch_name])

def list_branches():
    return run_git_command(['branch'])

def merge_branch(source_branch):
    return run_git_command(['merge', source_branch])

def commit_changes(message):
    return run_git_command(['commit', '-m', message])
