makefile' in block:
                            extension = 'makefile'
                            folder = 'Makefiles'
                        else:
                            continue

                        # Lag mappe hvis den ikke eksisterer
                        output_folder = os.path.join(output_dir, folder)
                        if not os.path.exists(output_folder):
                            os.makedirs(output_folder)

                        output_file_path = os.path.join(output_folder, f"{os.path.splitext(file)[0]}.{extension}")
                        with open(output_file_path, 'w', encoding='utf-8') as code_file:
                            code_file.write(block.strip('`').strip())

                        # Opprett README.md for koden
                        readme_path = os.path.join(output_folder, 'README.md')
                        with open(readme_path, 'w', encoding='utf-8') as readme_file:
                            readme_content = (
                                f"# {file}\n\n"
                                f"**Original Location**: {file_path}\n\n"
                                f"**Link in Wiki**: [{file}](https://github.com/itnett/FTD02N/wiki/{os.path.splitext(file)[0]})\n"
                            )
                            readme_file.write(readme_content)

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
def git_operations(directory, commit_message):
    os.chdir(directory)
    
    # Legg til filer i staging
    subprocess.run(["git", "add", "."])
    
    # Commit med en beskrivelse
    subprocess.run(["git", "commit", "-m", commit_message])
    
    # Oppdaterer (puller) siste endringer
    subprocess.run(["git", "pull", "--rebase"])
    
    # Pusher til remote repository
    subprocess.run(["git", "push", "-u", "origin", "main"])

# Funksjon for å generere en commit-melding med tidsstempel
def generate_commit_message():
    return f"Automatisk oppdatering - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# Hovedløp
# Klon den originale Wiki-repoen
if not os.path.exists(dump_directory):
    subprocess.run(["git", "clone", wiki_repo_url, dump_directory])

# Migrer kodeblokker til ny repo
migrate_code_blocks(dump_directory, code_repo_directory)

# Oppdater URL-er i den nye Wiki-repoen
old_base_url = 'https://github.com/itnett/FTD02N/blob/main/'
new_base_url = 'https://github.com/itnett/FTD02N/blob/main/'
update_wiki_urls(dump_directory, old_base_url, new_base_url)

# Git-operasjoner med logging og commit-melding
commit_message_code_repo = generate_commit_message()
commit_message_wiki_repo = generate_commit_message()

git_operations(code_repo_directory, commit_message_code_repo)
git_operations(dump_directory, commit_message_wiki_repo)