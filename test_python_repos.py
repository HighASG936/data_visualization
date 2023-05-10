import unittest
from python_repos import PythonRepos

class TestPythonRepos(unittest.TestCase):
    """Test to python_repos.py"""
    
    def setUp(self):
        """ """
        self.pyr = PythonRepos()
    
    def test_status_code(self):
        status = self.pyr.get_status_code()
        self.assertEqual(status, 200)
    
    def test_get_total_repos(self):
        total_repos = self.pyr.get_total_repos()
        self.assertGreater(total_repos, 500)
    
    def test_get_first_repo_len_dict(self):
        dict_len = self.pyr.get_first_repo_len_dict()
        self.assertEqual(dict_len, 80)
    
    def test_get_responce_keys(self):
        keys = ['total_count', 'incomplete_results', 'items']
        rk = self.pyr.get_responce_keys()
        self.assertListEqual(rk, keys)
    
if __name__ == '__main__':
    unittest.main()