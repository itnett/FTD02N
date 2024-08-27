makefile' in block:
                            extension = 'makefile'
                            folder = 'Makefiles'
                        else:
                            continue

                        # Opprett mappe hvis den ikke finnes
                        folder_path = os.path.join(output_dir, folder)
                        if not os.path.exists(folder_path):
                            os.makedirs(folder_path)

                        output_file_path = os.path.join(folder_path, f"{os.path.splitext(file)[0]}.{extension}")
                        with open(output_file_path, 'w', encoding='utf-8') as code_file:
                            code_file.write(block.strip('`').strip())

                        # Lag en README.md for hver fil
                        readme_file_path = os.path.join(folder_path, "README.md")
                        with open(readme_file_path, 'a', encoding='utf-8') as readme_file:
                            readme_file.write(f"- {os.path.splitext(file)[0]}.{extension} er hentet fra {file_path}\n")

                        print(f"Kode blokk eksportert til {output_file_path}")

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

# Funksjon for å generere en commit-melding med tidsstempel
def generate_commit_message():
    return f"Automatisk oppdatering - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# Hovedløp
# Klon Wiki-repoet hvis ikke det allerede er klonet
if not os.path.exists(dump_directory):
    subprocess.run(["git", "clone", wiki_repo_url, dump_directory])
else:
    print("Wiki-repoet er allerede klonet.")

# Migrer kodeblokker fra klonet repo til kode-repo
migrate_code_blocks(dump_directory, code_repo_directory)

# Oppdatere URL-er i wiki-repoet
old_base_url = f'{code_repo_url}/blob/main/'
new_base_url = f'{code_repo_url}/blob/main/'
update_wiki_urls(dump_directory, old_base_url, new_base_url)

# Git-operasjoner med logging og commit-melding
commit_message_code_repo = generate_commit_message()
commit_message_wiki_repo = generate_commit_message()

# Pusher til 'main'-grenen for code_repo_directory
git_operations(code_repo_directory, commit_message_code_repo, branch='main')

# Pusher til 'master'-grenen for dump_directory (Wiki-repoet)
git_operations(dump_directory, commit_message_wiki_repo, branch='master')