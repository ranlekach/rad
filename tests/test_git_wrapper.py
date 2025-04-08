import unittest
from unittest.mock import patch
from radfirst import git_wrapper

class TestGitWrapper(unittest.TestCase):

    @patch('radfirst.git_wrapper.run_git_command')
    def test_create_branch(self, mock_run):
        mock_run.return_value = 'Switched to a new branch'
        result = git_wrapper.create_branch('feature-x')
        self.assertIn('Switched', result)

    @patch('radfirst.git_wrapper.run_git_command')
    def test_list_branches(self, mock_run):
        mock_run.return_value = '* main\n  dev'
        result = git_wrapper.list_branches()
        self.assertIn('main', result)

    @patch('radfirst.git_wrapper.run_git_command')
    def test_merge_branch(self, mock_run):
        mock_run.return_value = 'Merge made by the recursive strategy.'
        result = git_wrapper.merge_branch('dev')
        self.assertIn('Merge', result)

    @patch('radfirst.git_wrapper.run_git_command')
    def test_commit_changes(self, mock_run):
        mock_run.return_value = '[main abc1234] Initial commit'
        result = git_wrapper.commit_changes('Initial commit')
        self.assertIn('Initial commit', result)

if __name__ == '__main__':
    unittest.main()
