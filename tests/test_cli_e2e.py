import subprocess
import tempfile
import os
import shutil
import unittest
import stat

class TestRadfirstCLI(unittest.TestCase):

    def setUp(self):
        self.repo_dir = tempfile.mkdtemp()
        subprocess.run(["git", "init"], cwd=self.repo_dir, check=True)
        with open(os.path.join(self.repo_dir, "README.md"), "w") as f:
            f.write("# Test Repo")
        subprocess.run(["git", "add", "README.md"], cwd=self.repo_dir, check=True)
        subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=self.repo_dir, check=True)

    def tearDown(self):
        def on_rm_error(func, path, exc_info):
            os.chmod(path, stat.S_IWRITE)
            func(path)
        shutil.rmtree(self.repo_dir, onerror=on_rm_error)

    def run_rad(self, args):
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        env = os.environ.copy()
        env["PYTHONPATH"] = project_root

        return subprocess.run(
            ["python", os.path.join(project_root, "rad.py")] + args,
            cwd=self.repo_dir,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

    def test_create_and_list_branch(self):
        result_create = self.run_rad(["create", "test-branch"])
        self.assertIn("Switched to a new branch", result_create.stdout)

        result_list = self.run_rad(["list"])
        self.assertIn("test-branch", result_list.stdout)

    def test_commit(self):
        with open(os.path.join(self.repo_dir, "file.txt"), "w") as f:
            f.write("hello")
        subprocess.run(["git", "add", "file.txt"], cwd=self.repo_dir, check=True)

        result_commit = self.run_rad(["commit", "Add file.txt"])
        self.assertIn("Add file.txt", result_commit.stdout)

if __name__ == '__main__':
    unittest.main()