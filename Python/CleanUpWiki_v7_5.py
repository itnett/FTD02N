python
print("Vennligst oppgi ditt GitHub Personal Access Token (PAT) med nødvendige rettigheter.")
github_pat = getpass("GitHub PAT: ")

authenticated_main_repo_url = main_repo_url.replace('https://', f'https://{github_pat}@')
authenticated_wiki_repo_url = wiki_repo_url.replace('https://', f'https://{github_pat}@')