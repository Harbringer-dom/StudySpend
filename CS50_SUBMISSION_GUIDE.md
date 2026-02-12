# CS50 Final Project Submission Guide

## Step 1: Verify Your GitHub Repo

1. Go to your GitHub repo: `https://github.com/Harbringer-dom/cs50-Final-Project`
2. Make sure it's **public** (Settings → Visibility)
3. Push any final changes:
   ```bash
   cd "cs50 Finall Project"
   git add .
   git commit -m "Final submission for CS50"
   git push origin main
   ```

## Step 2: Create Your Video Demo

1. **Choose a recording tool:**
   - **Loom** (easiest): Go to loom.com, sign in, click "Start Recording"
   - **OBS Studio**: Download from obsproject.com
   - **Windows 11**: Use Snip & Sketch (Win + Shift + S)

2. **Follow the script** in `VIDEO_SCRIPT.md` (or create your own)

3. **Keep it under 10 minutes** - aim for 4-5 minutes

4. **Demo these features:**
   - Registration/Login
   - Add and filter expenses
   - Add and complete study tasks
   - Show the dashboard
   - Briefly explain your tech choices

5. **Upload your video:**
   - YouTube: Make it **unlisted** (searchable by link, not in recommendations)
   - Google Drive: Share link with "View" access
   - Loom: Get the link (auto-generated)
   - Any other platform works too

6. **Copy the video link** (you'll need it for submission)

## Step 3: Check Your README

Your `README.md` should have:
- ✅ Project description
- ✅ Feature list
- ✅ Tech stack mentioned
- ✅ How to run it (setup instructions)
- ✅ Video demo link (replace placeholder)
- ✅ Database schema (already there)
- ✅ Deployment guide (already there)

## Step 4: CS50 Submission Portal

1. Go to **cs50.me** or your course's submission portal
2. Fill in these fields:
   - **GitHub Repo URL**: `https://github.com/Harbringer-dom/cs50-Final-Project`
   - **Video URL**: `[Your YouTube/Loom/Drive link]`
   - **README**: (might auto-detect from repo)

3. Review all information
4. Submit!

## Step 5: After Submission

- CS50 staff will review your code
- They may ask questions about design choices
- Be ready to explain why you used Flask, SQLite, etc.
- You should be able to run the app live during review

---

## Quick Verification Before Final Submit

Run this locally to make sure everything works:

```bash
cd "cs50 Finall Project"
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python init_db.py
python app.py
```

Then:
1. Register a new account
2. Add an expense
3. Add a study task
4. Check the dashboard
5. Verify everything works

If all tests pass, you're ready!

---

## Common Questions

**Q: Do I need to include database.db in my repo?**
A: No! It's in `.gitignore`. CS50 reviewers will initialize it themselves with `python init_db.py`

**Q: What if they ask to explain my code during review?**
A: Be ready to discuss:
- Why you chose Flask
- Why you used SQLite
- How authentication works
- How you prevent SQL injection
- Your database design choices

**Q: Can I deploy the app online first?**
A: Yes! You can show them a working live version too. (See DEPLOYMENT.md)

---

**You're ready to submit! 🎓**
