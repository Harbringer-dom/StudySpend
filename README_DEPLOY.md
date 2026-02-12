# Deploying StudySpend (quick)

Two easy options to make your app reachable from a phone:

- Quick temporary (useful for demos): ngrok
  1. Install ngrok and sign up for a free account.
 2. Run your app locally:

```powershell
cd "cs50 Finall Project"
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

3. In another terminal run:

```powershell
ngrok http 5000
```

4. Open the public ngrok URL on your phone.

- Permanent (recommended): Render / Railway
  - Create an account and connect your GitHub repo.
  - Set the build command: `pip install -r requirements.txt` (Render/Railway auto-detects).
  - Start command (Render): leave Procfile (web: gunicorn app:app) in repo — Render will use it.
  - Add an environment variable `SECRET_KEY` in the service settings.
  - Deploy — the service will give you a public HTTPS URL you can open on any phone.

Notes
- The app will auto-create `database.db` from `schema.sql` the first time it runs on the host.
- For local phone testing without ngrok, run `python app.py` and open `http://<your-pc-ip>:5000` on the phone (same Wi‑Fi).
