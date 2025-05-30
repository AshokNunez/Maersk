# 📤 How to Push a Local Project to GitHub

This guide walks you through pushing your local code to a new GitHub repository.

---

## ✅ 1. Prerequisites

- Git must be installed. Check with:

  ```bash
  git --version
  ```

- A GitHub account: [https://github.com](https://github.com)

---

## ✅ 2. Create a GitHub Repository

1. Go to [https://github.com](https://github.com)
2. Click **"New"** repository.
3. Set a name like `my-project`.
4. Choose **public** or **private**.
5. Click **Create repository**.
6. Leave the page open — you'll need the repo URL.

---

## ✅ 3. Initialize Git in Your Local Project

If your project is already created locally:

```bash
cd path/to/your/project
git init
git add .
git commit -m "Initial commit"
```

---

## ✅ 4. Link Your GitHub Repository

Use the HTTPS or SSH URL provided by GitHub:

```bash
git remote add origin https://github.com/your-username/your-repo-name.git
```

You can confirm with:

```bash
git remote -v
```

---

## ✅ 5. Push to GitHub

First time push:

```bash
git branch -M main
git push -u origin main
```

Next time you want to push changes:

```bash
git add .
git commit -m "Your message here"
git push
```

---

## 🔐 Authentication Tips

- GitHub **no longer supports password authentication**.
- Use a **personal access token** or set up **SSH**.
- [GitHub Authentication Guide](https://docs.github.com/en/authentication)

---

## 🧪 Example

```bash
cd myproject/
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/myproject.git
git branch -M main
git push -u origin main
```

---

Happy coding! 🚀
