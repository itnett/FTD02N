makefile' in block:
                            extension = 'makefile'
                            folder = "Makefiles"
                        else:
                            continue

                        output_folder = os.path.join(output_dir, folder)
                        if not os.path.exists(output_folder):
                            os.makedirs(output_folder)

                        output_file_path = os.path.join(output_folder, f"{os.path.splitext(file)[0]}_{index}.{extension}")
                        with open(output_file_path, 'w', encoding='utf-8') as code_file:
                            code_file.write(block.strip('`').strip())

                        # Opprett README.md-fil for hver eksportert kode
                        readme_file_path = os.path.join(output_folder, f"{os.path.splitext(file)[0]}_{index}_README.md")
                        with open(readme_file_path, 'w', encoding='utf-8') as readme_file:
                            readme_file.write(f"# README for {os.path.splitext(file)[0]}_{index}\n")
                            readme_file.write(f"Denne koden ble eksportert fra {file_path}\n")
                            readme_file.write(f"Link til denne koden: {output_file_path}\n")
                        
                        print(f"Kode blokk eksportert til {output_file_path} med README {readme_file_path}")

# Funksjon for å oppdatere URL-er i wiki-sidene
def update_wiki_urls(directory, old_base_url, new_base_url):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                updated_content = re.sub(old_base_url, new_base_url, content)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"Oppdatert URL-er i {file_path}")

# Funksjon for å utføre Git-operasjoner
def git_operations(directory, commit_message, remote="origin", branch="main"):
    os.chdir(directory)
    
    # Legg til filer i staging
    subprocess.run(["git", "add", "."])
    
    # Commit med en beskrivelse
    subprocess.run(["git", "commit", "-m", commit_message])
    
    # Oppdaterer (puller) siste endringer
    subprocess.run(["git", "pull", "--rebase", remote, branch])
    
    # Pusher til remote repository
    subprocess.run(["git", "push", remote, branch])

# Funksjon for å generere en commit-melding med tidsstempel
def generate_commit_message():
    return f"Automatisk oppdatering - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# Hovedløp
repo_directory = dump_directory
output_directory = code_repo_directory

# Kjør migreringen
migrate_code_blocks(repo_directory, output_directory)

# Oppdatere URL-er i wiki-repoet
old_base_url = 'https://github.com/itnett/FTD02H-N.wiki.git'
new_base_url = 'https://github.com/itnett/FTD02N/blob/main/'  # Juster etter behov
update_wiki_urls(repo_directory, old_base_url, new_base_url)

# Git-operasjoner med logging og commit-melding
commit_message_code_repo = generate_commit_message()
commit_message_wiki_repo = generate_commit_message()

git_operations(output_directory, commit_message_code_repo)
git_operations(repo_directory, commit_message_wiki_repo, remote="origin", branch="master")