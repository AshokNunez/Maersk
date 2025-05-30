# 📤 How to Push a Local Project to GitHub

This guide walks you through pushing your local code to a new GitHub repository.

---

## ✅ 1. Prerequisites

- Git must be installed. Check with:

  ```bash
  git --version
✅ 2. Create a GitHub Repository
Go to https://github.com

Click "New" repository.

Set a name like my-project.

Choose public or private.

Click Create repository.

Leave the page open — you'll need the repo URL.

✅ 3. Initialize Git in Your Local Project
If your project is already created locally:

cd path/to/your/project
git init
git add .
git commit -m "Initial commit"
✅ 4. Link Your GitHub Repository
Use the HTTPS or SSH URL provided by GitHub:

git remote add origin https://github.com/your-username/your-repo-name.git
