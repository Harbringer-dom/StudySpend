# StudySpend - Video Demo Script

## Total Duration: ~4 minutes

---

## INTRO (0:00 - 0:30)

**On screen: Show desktop with project open**

"Hi, I'm Chitvan Suri, and this is StudySpend, my CS50 Final Project.

StudySpend is a Flask web app that helps students like me track expenses and manage study tasks all in one place. It combines expense tracking with study planning, which is something I couldn't find in one app.

Let me show you how it works."

---

## FEATURE 1: REGISTRATION & LOGIN (0:30 - 1:00)

**Action: Open app at localhost:5000**
- Show login page
- Click "Register here"
- Fill in username (e.g., "student123") and password (e.g., "password123")
- Click Register
- Show success message
- Click Login
- Enter credentials
- Show dashboard

**Narration:**
"First, you need to register. I'll create a new account with a username and password. The app securely hashes the password using Werkzeug, so your data is safe.

Once registered, I can log in and see my personalized dashboard."

---

## FEATURE 2: DASHBOARD (1:00 - 1:30)

**Action: Show dashboard**
- Point to each card: Monthly Expense, Total Tasks, Completed, Pending
- Point to Category Breakdown
- Show quick summary

**Narration:**
"The dashboard shows my monthly spending, how many study tasks I have, and how many are completed. It breaks down expenses by category so I can see where my money is going.

This gives me a quick overview of both my spending and study progress in one place."

---

## FEATURE 3: EXPENSE TRACKER (1:30 - 2:45)

**Action: Click "Expense Tracker"**
- Show form (Category dropdown, Amount, Date, Note)
- Add an expense (e.g., "Food", "150", today's date, "Lunch")
- Show success message
- Show expense in table
- Click on "Food" filter button
- Show filtered results
- Delete the expense
- Show "All" to see everything again

**Narration:**
"Next is the Expense Tracker. I can add an expense by selecting a category like Food, entering the amount, date, and an optional note.

Once added, it shows in a table sorted by date. I can filter by category to see only Food expenses, or Travel, Study, Shopping, Entertainment, or Other.

If I made a mistake or want to remove an expense, I can delete it with one click. The total spent updates automatically."

---

## FEATURE 4: STUDY PLANNER (2:45 - 3:45)

**Action: Click "Study Planner"**
- Show form (Title, Description, Due Date)
- Add a task (e.g., "Chapter 5 Reading", "Read pages 45-67", date in future)
- Show success message
- Show task in list with "Pending" badge
- Show task details (due date, description)
- Click "Mark Done" button
- Show task now says "Completed" with strikethrough
- Click "Mark Pending" to toggle back
- Delete the task

**Narration:**
"The Study Planner helps me organize my study tasks. I add a title, optional description, and due date.

Tasks show up in a list with a 'Pending' or 'Completed' badge. I can mark them as done when finished, and toggle them back if needed. 

Tasks are sorted by completion status and due date, so I see what's most urgent first. I can also delete tasks when they're no longer needed."

---

## FEATURE 5: CODE OVERVIEW (3:45 - 4:15)

**Action: Open VS Code, show files briefly**
- Show app.py (scroll through routes)
- Show templates folder (layout.html, dashboard.html)
- Show schema.sql
- Show requirements.txt

**Narration:**
"Here's what I built:

The backend is Flask—a Python web framework. I used SQLite for the database with three main tables: users, expenses, and study_tasks2. Each user has their own isolated data.

Templates use Jinja2 for dynamic HTML. I styled everything with CSS to make it responsive and look nice on any device.

For security, passwords are hashed using Werkzeug, and I use parameterized SQL queries to prevent injection attacks. Users are authenticated with Flask sessions."

---

## OUTRO (4:15 - 4:30)

**On screen: Show project on GitHub (optional)**

"This project taught me a lot about full-stack development—working with databases, user authentication, and building a real, usable app.

Thanks for watching! The code is on GitHub at [your-repo-link], and you can deploy it easily to Render or PythonAnywhere using the instructions in the README.

Thanks!"

---

## Recording Checklist

- [ ] Camera is in focus
- [ ] Audio is clear (no background noise)
- [ ] Mouse movements are smooth
- [ ] Text is readable on screen
- [ ] You speak clearly and not too fast
- [ ] Video is under 10 minutes
- [ ] You demo all features (auth, expenses, study tasks, dashboard)
- [ ] You mention the tech stack briefly

---

## Quick Recording Tools

1. **OBS Studio** (Windows/Mac/Linux) - Free, professional
2. **Loom** (loom.com) - Easiest, browser-based, auto-uploads
3. **ScreenFlow** (Mac) - Built-in, simple
4. **Windows 11 Snip & Sketch** - Built-in, basic

**Recommended: Loom** (just click "Start Recording", do your demo, and get a link!)
