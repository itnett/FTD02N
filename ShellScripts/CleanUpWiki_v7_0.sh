bash
#!/bin/bash

# Konfigurerer Git-repositoriet
REPO_DIR="C:/WikiMigration/git/code_repo"
WIKI_REPO_DIR="C:/WikiMigration/git/code_repo_wiki"
MAIN_REPO_URL="https://github.com/itnett/FTD02N.git"
WIKI_REPO_URL="https://github.com/itnett/FTD02N.wiki.git"
COMMIT_MSG="Automatisk commit etter migrasjon"

# Gå til hoved-repo directory
cd "$REPO_DIR" || exit

# Initialiser git hvis det ikke allerede er gjort
if [ ! -d ".git" ]; then
    git init
    git branch -M main
fi

# Legg til remote og sjekk om det allerede eksisterer
git remote remove origin 2>/dev/null
git remote add origin "$MAIN_REPO_URL"

# Legg til filer, commit og push
git add .
git commit -m "$COMMIT_MSG"
git push -u origin main

# Gå til wiki-repo directory (hvis det er separert)
if [ -d "$WIKI_REPO_DIR" ]; then
    cd "$WIKI_REPO_DIR" || exit

    if [ ! -d ".git" ]; then
        git init
        git branch -M main
    fi

    git remote remove origin 2>/dev/null
    git remote add origin "$WIKI_REPO_URL"

    git add .
    git commit -m "$COMMIT_MSG"
    git push -u origin main
fi

echo "Kode er pushet til GitHub."