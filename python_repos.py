import requests

class PythonRepos:
    
    def __init__(self):
        #Set keyword to search
        keyword = 'python'
        
        #Make an API call and store the response.
        self.url = f"https://api.github.com/search/repositories?q=language:{keyword}&sort=stars"                        
        self.headers = {'Accept': 'application/vnd.github.v3+json'}
        self.r = requests.get(self.url, headers=self.headers)
        
        #Store API response in a variable.        
        self.response_dict = self.r.json()
        
        #Explore information about the repositories.
        self.repo_dicts = self.response_dict['items']
        
        #Examine the first repository.
        self.first_repo_dict = self.repo_dicts[0]

    def get_status_code(self):
        """ """
        return self.r.status_code
        
    def get_total_repos(self):
        """ """
        return self.response_dict['total_count']

    def get_responce_keys(self):
        """ """
        return list(self.response_dict.keys())

    def get_repositories_returned(self):
        """ """
        return len(self.repo_dicts)

    def get_first_repo_len_dict(self):
        """ """
        return len(self.first_repo_dict)
    
    def display_first_repo_info(self):
        """ """        
        for key in sorted(self.first_repo_dict.keys()):
            print(key)

    def get_all_repos_info(self):
        print("\nSelected information about each repository:")
        for repo_dict in self.repo_dicts:
            print(f"\nName: {repo_dict['name']}")
            print(f"Owner: {repo_dict['owner']['login']}")
            print(f"Stars: {repo_dict['stargazers_count']}")
            print(f"Repository: {repo_dict['html_url']}")
            print(f"Created: {repo_dict['created_at']}")
            print(f"Updated: {repo_dict['updated_at']}")
            print(f"Description: {repo_dict['description']}")

