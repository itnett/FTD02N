python
import os
from git import Repo, GitCommandError
from getpass import getpass

# ---------------------------- Konfigurasjon ---------------------------- #

# Sti til lokale kataloger
main_repo_local_path = r'C:\WikiMigration\git\FTD02N'
wiki_repo_local_path = r'C:\WikiMigration\git\FTD02N.wiki'

# GitHub URLer
main_repo_url = 'https://github.com/itnett/FTD02N.git'
wiki_repo_url = 'https://github.com/itnett/FTD02N.wiki.git'

# Commit-meldinger
main_repo_commit_message = 'Oppdatering av hovedrepo med siste endringer'
wiki_repo_commit_message = 'Oppdatering av wiki-repo med siste endringer'

# Filstier å legge til i hvert repo
main_repo_files = [
    # Legg til fulle filstier eller bruk os.path.join for å dynamisk lage stier
    r'C:\WikiMigration\git\code_repo\file1.py',
    r'C:\WikiMigration\git\code_repo\file2.py',
    # Legg til flere filer etter behov
]

wiki_repo_files = [
    r'C:\WikiMigration\git\code_dump\page1.md',
    r'C:\WikiMigration\git\code_dump\page2.md',
    # Legg til flere filer etter behov
]

# ------------------------- Autentisering ------------------------- #

# Be om GitHub Personal Access Token fra bruker
print("Vennligst oppgi ditt GitHub Personal Access Token (PAT) med nødvendige rettigheter.")
github_pat = getpass("GitHub PAT: ")

# Legg til PAT i URLene for autentisering
authenticated_main_repo_url = main_repo_url.replace('https://', f'https://{github_pat}@')
authenticated_wiki_repo_url = wiki_repo_url.replace('https://', f'https://{github_pat}@')

# ------------------------ Funksjoner ------------------------ #

def clone_or_pull_repo(local_path, repo_url):
    if not os.path.exists(local_path):
        try:
            print(f"Kloner repo fra {repo_url} til {local_path}...")
            Repo.clone_from(repo_url, local_path)
            print("Kloning fullført.")
        except GitCommandError as e:
            print(f"Feil under kloning: {e}")
    else:
        try:
            print(f"Oppdaterer eksisterende repo i {local_path}...")
            repo = Repo(local_path)
            origin = repo.remotes.origin
            origin.pull()
            print("Oppdatering fullført.")
        except GitCommandError as e:
            print(f"Feil under oppdatering: {e}")

def add_and_commit(repo_path, files, commit_message):
    try:
        repo = Repo(repo_path)
        print(f"Legger til filer i {repo_path}...")
        repo.index.add(files)
        if repo.is_dirty():
            print("Lager commit...")
            repo.index.commit(commit_message)
            print("Commit fullført.")
        else:
            print("Ingen endringer å kommitere.")
    except GitCommandError as e:
        print(f"Feil under adding/committing: {e}")

def push_changes(repo_path):
    try:
        repo = Repo(repo_path)
        print(f"Pusher endringer fra {repo_path}...")
        origin = repo.remotes.origin
        origin.push()
        print("Push fullført.")
    except GitCommandError as e:
        print(f"Feil under pushing: {e}")

# ------------------------ Hovedprosess ------------------------ #

if __name__ == "__main__":
    # Håndtere hovedrepo
    clone_or_pull_repo(main_repo_local_path, authenticated_main_repo_url)
    add_and_commit(main_repo_local_path, main_repo_files, main_repo_commit_message)
    push_changes(main_repo_local_path)

    # Håndtere wiki-repo
    clone_or_pull_repo(wiki_repo_local_path, authenticated_wiki_repo_url)
    add_and_commit(wiki_repo_local_path, wiki_repo_files, wiki_repo_commit_message)
    push_changes(wiki_repo_local_path)