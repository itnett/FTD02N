makefile' in block:
                            extension = 'makefile'
                            folder = 'Makefiles'
                        else:
                            continue

                        script_dir = os.path.join(output_dir, folder)
                        if not os.path.exists(script_dir):
                            os.makedirs(script_dir)

                        script_file_name = f"{os.path.splitext(file)[0]}_{i + 1}.{extension}"
                        output_file_path = os.path.join(script_dir, script_file_name)
                        
                        with open(output_file_path, 'w', encoding='utf-8') as code_file:
                            code_file.write(block.strip('`').strip())

                        # Lag README.md for skriptet
                        readme_content = f"# {script_file_name}\n\n"
                        readme_content += f"Dette skriptet ble opprinnelig funnet i filen `{file}`.\n\n"
                        readme_content += f"## Beskrivelse\n\nSkriptet er av typen `{extension}` og ble funnet som en kodeblokk i en wiki-side.\n\n"
                        readme_content += f"## Lenker\n\n"
                        readme_content += f"- Opprinnelig wiki-side: [{file}](https://github.com/itnett/FTD02N.wiki.git/{file})\n"
                        readme_content += f"- Lenke til skriptet: [{script_file_name}](https://github.com/itnett/FTD02N/blob/main/{folder}/{script_file_name})\n"

                        readme_file_path = os.path.join(script_dir, 'README.md')
                        with open(readme_file_path, 'w', encoding='utf-8') as readme_file:
                            readme_file.write(readme_content)

                        print(f"Kode blokk eksportert til {output_file_path}")
                        print(f"README.md generert for {script_file_name}")

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
if __name__ == "__main__":
    # Kjør migreringen
    migrate_code_blocks(dump_directory, code_repo_directory)

    # Oppdatere URL-er i wiki-repoet
    old_base_url = 'https://github.com/itnett/FTD02N/blob/main/'
    new_base_url = f'https://github.com/itnett/FTD02N/blob/main/'
    update_wiki_urls(dump_directory, old_base_url, new_base_url)

    # Git-operasjoner med logging og commit-melding
    commit_message_code_repo = generate_commit_message()
    commit_message_wiki_repo = generate_commit_message()

    git_operations(code_repo_directory, commit_message_code_repo)
    git_operations(dump_directory, commit_message_wiki_repo)

    print("Skriptet er ferdig med å migrere og publisere koder og oppdaterte wiki-sider.")