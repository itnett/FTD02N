bash
# Initialize a new Git repository
git init

# Add LaTeX files to the repository
git add *.tex

# Commit the changes
git commit -m "Initial commit"

# Create a new branch
git checkout -b draft

# Push to a remote repository
git remote add origin https://github.com/yourusername/yourrepository.git
git push -u origin master