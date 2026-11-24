# Agilesh J – Portfolio (Flask + Python)

A one-page portfolio website. All text lives in **`data.py`**; the look lives in **`public/css/style.css`**.

## Project structure
```
portfolio/
├── app.py                  Flask app (one route, "/")
├── data.py                 ALL content: skills, projects, experience, links
├── requirements.txt        Python packages (just Flask)
├── templates/
│   ├── base.html           page shell: menu with the AJ logo, footer
│   ├── index.html          lists the sections in order
│   └── sections/           one small file per section (hero, about, skills, ...)
└── public/                 files served directly (Vercel serves this folder)
    ├── css/style.css       colours, fonts, layout
    ├── js/main.js          card tilt on hover + active menu link
    └── images/             your photos (agilesh.jpg, agilesh-blink.jpg) and favicon
```

## Run on your computer
```bash
python -m venv .venv
.venv\Scripts\activate          # Windows   (Mac/Linux: source .venv/bin/activate)
pip install -r requirements.txt
python app.py                   # open http://127.0.0.1:5000
```

## Common edits
- **Change text, skills, projects, links:** edit `data.py`, then refresh.
- **Add a GitHub button to a project:** set `"repo": "https://github.com/agilesh-j/your-repo"` in `data.py`.
- **Change colours:** edit the `:root` block at the top of `public/css/style.css`.
- **Change the photo:** replace `public/images/agilesh.jpg`. The blink needs `agilesh-blink.jpg` (same photo with closed eyes). To remove the blink, delete the second `<img>` in `templates/sections/hero.html`.

## Deploy on Vercel
1. Push this folder to a GitHub repository.
2. On vercel.com choose **Add New → Project**, import the repository and click **Deploy**. Vercel detects the Flask app in `app.py` automatically.
3. Or use the CLI: `npm i -g vercel`, then run `vercel` in this folder.

## Using Google Antigravity
Open this folder in Antigravity, then ask the agent for changes, for example: "Add a GitHub button to the PhishSense project" or "Make the skills cards use a different colour". `data.py` is the best file to point it to for content changes.
