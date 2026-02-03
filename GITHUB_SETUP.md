# Push this repo to GitHub

Repo name: **delib-ethics-evals** (public, same as folder).

1. **Create the repo on GitHub**
   - Go to [github.com/new](https://github.com/new)
   - Repository name: `delib-ethics-evals`
   - Public
   - Leave "Add a README", ".gitignore", and "license" **unchecked** (we already have them)
   - Click **Create repository**

2. **Point your local repo at your GitHub repo**
   Replace `YOUR_GITHUB_USERNAME` with your actual GitHub username, then run:

   ```bash
   cd /Users/nihal/Desktop/delib-ethics-evals
   git remote set-url origin https://github.com/YOUR_GITHUB_USERNAME/delib-ethics-evals.git
   git push -u origin main
   ```

   If you use SSH:  
   `git remote set-url origin git@github.com:YOUR_GITHUB_USERNAME/delib-ethics-evals.git`  
   then `git push -u origin main`.

3. **Done.** The repo will be at `https://github.com/YOUR_GITHUB_USERNAME/delib-ethics-evals`.
