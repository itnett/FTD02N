makefile' in code_block:
        return 'makefile'
    else:
        return None

# Funksjon for å migrere kodeblokker og generere README-filer
def migrate_code_blocks(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                code_blocks = re.findall(r'