python
# Funksjon for å utføre Git-operasjoner
def git_operations(directory, commit_message, branch='main'):
    os.chdir(directory)
    
    # Legg til filer i staging
    subprocess.run(["git", "add", "."])
    
    # Commit med en beskrivelse
    subprocess.run(["git", "commit", "-m", commit_message])
    
    # Oppdaterer (puller) siste endringer
    subprocess.run(["git", "pull", "--rebase"])
    
    # Pusher til remote repository
    subprocess.run(["git", "push", "-u", "origin", branch])

# Hovedløp
# Git-operasjoner med logging og commit-melding
commit_message_code_repo = generate_commit_message()
commit_message_wiki_repo = generate_commit_message()

# Pusher til 'main'-grenen for code_repo_directory
git_operations(code_repo_directory, commit_message_code_repo, branch='main')

# Pusher til 'master'-grenen for dump_directory (Wiki-repoet)
git_operations(dump_directory, commit_message_wiki_repo, branch='master')