import unittest

from HW04a import get_repo_info


class TestGetRepo(unittest.TestCase):
    def test_normal_response(self):
        expected = ['User: 769978445',
                    'Repo: 567HW2 Number of commits: 8',
                    'Repo: 810Project Number of commits: 1',
                    'Repo: GitHubApi567 Number of commits: 14',
                    'Repo: MGR4Python Number of commits: 1',
                    'Repo: SSW567 Number of commits: 2']
        self.assertEqual(get_repo_info(), expected)

    def test_bad_user_name(self):
        self.assertEqual(get_repo_info('aaaabbbbcccc'), 'unable to fetch repos from user')
        self.assertEqual(get_repo_info(''), 'unable to fetch repos from user')


if __name__ == '__main__':
    unittest.main()
