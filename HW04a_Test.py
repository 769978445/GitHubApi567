import unittest

from HW04a import get_repo_info
from unittest.mock import Mock,patch


class TestGetRepo(unittest.TestCase):
    @patch('requests.get')
    def test_get_repo_info(self,mockedReq):
        mock_data = '[{"name": "567HW2"}, {"name": "810Project"}]'
        expected = ['User: 769978445',
                    'Repo: 567HW2 Number of commits: 2',
                    'Repo: 810Project Number of commits: 2']
        mockedReq.return_value.text = mock_data
        self.assertEqual(get_repo_info("769978445"), expected)

    # def test_bad_user_name(self):
    #     self.assertEqual(get_repo_info('123456'), 'unable to fetch repos from user')
    #     self.assertEqual(get_repo_info('XiangyuWang'), 'unable to fetch repos from user')
    #     self.assertEqual(get_repo_info(''), 'unable to fetch repos from user')


if __name__ == '__main__':
    unittest.main()
