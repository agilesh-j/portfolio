"""Everything shown on the website. Edit the text here, save, refresh the page."""

NAME = "Agilesh J"
ROLE_LINE = "AI & Data Science Student · Python Developer · AI/ML Enthusiast · Full Stack Developer"
INTRO = ("I build computer vision, speech and generative AI applications in Python, "
         "and I’m working toward a career as a Machine Learning Engineer.")
LOCATION = "Nagercoil, Kanniyakumari, Tamil Nadu"

LINKS = {
    "email": "agileshj620@gmail.com",
    "phone": "+91 97877 69173",
    "phone_raw": "+919787769173",
    "linkedin": "https://linkedin.com/in/agilesh-j-91a576356",
    "github": "https://github.com/agilesh-j",
}

STATS = [
    ("8.23", "B.Tech CGPA"),
    ("5", "AI and full stack projects"),
    ("4", "internships"),
    ("15+", "certifications"),
]

ABOUT = [
    "I am a third-year B.Tech student in Artificial Intelligence and Data Science at "
    "Arunachala HiTech Engineering College. I like turning ideas into working products, "
    "from a Transformer trained from scratch to a speech-to-speech voice assistant.",
    "My toolkit covers OpenCV, scikit-learn, TensorFlow, PyTorch, Hugging Face Transformers "
    "and LLM APIs such as Groq and Google Gemini. I also build full stack apps with React, "
    "Node.js and PostgreSQL, and automate workflows with n8n.",
    "I am currently a Python Developer intern at Zeeyes AI Lab, and I am looking for "
    "Machine Learning Engineer and AI developer roles.",
]
LOOKING_FOR = ["Machine Learning Engineer", "AI Developer", "Python Developer"]

# Fallback SVG icons for skills not in Devicon
FALLBACK_ICONS = {
    "Hugging Face Transformers": '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10" fill="#FFD21E"/><circle cx="8.5" cy="10" r="1.5" fill="#1F2937"/><circle cx="15.5" cy="10" r="1.5" fill="#1F2937"/><path d="M9 13.5c.8 1.5 5.2 1.5 6 0" stroke="#1F2937" stroke-width="1.8" stroke-linecap="round"/><path d="M3.5 13c-.5.8-.2 1.8.6 2.2 1 .5 2 0 2.5-1" stroke="#D97706" stroke-width="1.5" stroke-linecap="round"/><path d="M20.5 13c.5.8.2 1.8-.6 2.2-1 .5-2 0-2.5-1" stroke="#D97706" stroke-width="1.5" stroke-linecap="round"/></svg>',
    "NLP": '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="24" height="24" rx="6" fill="#0E7C86"/><path d="M7 8.5h10M7 12h7M7 15.5h4" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/></svg>',
    "Generative AI": '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M10 2L12.5 7.5L18 10L12.5 12.5L10 18L7.5 12.5L2 10L7.5 7.5L10 2Z" fill="#8B5CF6"/><path d="M17 14L18.5 17.5L22 19L18.5 20.5L17 24L15.5 20.5L12 19L15.5 17.5L17 14Z" fill="#F59E0B"/></svg>',
    "Groq API": '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="24" height="24" rx="6" fill="#F55036"/><path d="M15 8.5a3.5 3.5 0 1 0 0 7h1v-4h-3" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "Google Gemini API": '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="gemini-grad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1BA1E3"/><stop offset="50%" stop-color="#5B73DF"/><stop offset="100%" stop-color="#C259D4"/></linearGradient></defs><path d="M12 2C12 7.52 7.52 12 2 12C7.52 12 12 16.48 12 22C12 16.48 16.48 12 22 12C16.48 12 12 7.52 12 2Z" fill="url(#gemini-grad)"/></svg>',
    "Whisper": '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="24" height="24" rx="6" fill="#10A37F"/><path d="M6 12v0M9 9v6M12 6v12M15 8v8M18 11v2" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round"/></svg>',
    "n8n": '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="24" height="24" rx="6" fill="#EA4B71"/><circle cx="7" cy="12" r="2.5" fill="#ffffff"/><circle cx="17" cy="8" r="2.5" fill="#ffffff"/><circle cx="17" cy="16" r="2.5" fill="#ffffff"/><path d="M7 12h5l5-4M12 12l5 4" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "JWT": '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="9.5" fill="#000000"/><path d="M12 2.5a9.5 9.5 0 0 1 8.23 14.25L12 12Z" fill="#FB015B"/><path d="M20.23 16.75a9.5 9.5 0 0 1-16.46 0L12 12Z" fill="#D63AFF"/><path d="M3.77 16.75a9.5 9.5 0 0 1 8.23-14.25L12 12Z" fill="#00B9F1"/><circle cx="12" cy="12" r="4.2" fill="#000000"/></svg>',
    "Seaborn": '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="24" height="24" rx="6" fill="#4C72B0"/><path d="M5 16c2.5 0 3.5-9 6-9s3.5 10 6 10 2.5-3 3-4" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
}

# Each group becomes one card. Add or remove items freely.
SKILLS = [
    ("Languages and web", [
        ("Python", "devicon-python-plain colored"),
        ("JavaScript", "devicon-javascript-plain colored"),
        ("HTML", "devicon-html5-plain colored"),
        ("CSS", "devicon-css3-plain colored"),
        ("React", "devicon-react-original colored"),
        ("Tailwind CSS", "devicon-tailwindcss-original colored"),
    ]),
    ("Machine learning and AI", [
        ("PyTorch", "devicon-pytorch-original colored"),
        ("TensorFlow", "devicon-tensorflow-original colored"),
        ("scikit-learn", "devicon-scikitlearn-plain colored"),
        ("Hugging Face Transformers", FALLBACK_ICONS["Hugging Face Transformers"]),
        ("OpenCV", "devicon-opencv-plain colored"),
        ("NLP", FALLBACK_ICONS["NLP"]),
        ("Generative AI", FALLBACK_ICONS["Generative AI"]),
    ]),
    ("Data analysis", [
        ("NumPy", "devicon-numpy-plain colored"),
        ("Pandas", "devicon-pandas-plain colored"),
        ("Matplotlib", "devicon-matplotlib-plain colored"),
        ("Seaborn", FALLBACK_ICONS["Seaborn"]),
    ]),
    ("APIs, automation and backend", [
        ("Groq API", FALLBACK_ICONS["Groq API"]),
        ("Google Gemini API", FALLBACK_ICONS["Google Gemini API"]),
        ("Whisper", FALLBACK_ICONS["Whisper"]),
        ("n8n", FALLBACK_ICONS["n8n"]),
        ("Streamlit", "devicon-streamlit-plain colored"),
        ("Node.js", "devicon-nodejs-plain colored"),
        ("Express.js", "devicon-express-original"),
        ("PostgreSQL", "devicon-postgresql-plain colored"),
        ("MySQL", "devicon-mysql-original colored"),
        ("JWT", FALLBACK_ICONS["JWT"]),
    ]),
    ("Tools", [
        ("Git and GitHub", "devicon-git-plain colored"),
        ("VS Code", "devicon-vscode-plain colored"),
        ("PyCharm", "devicon-pycharm-plain colored"),
        ("Jupyter Notebook", "devicon-jupyter-plain colored"),
        ("Google Colab", "devicon-googlecolab-plain colored"),
    ]),
]

# featured=True shows the project as a large card. Put the repo URL in "repo" to show a GitHub button.
PROJECTS = [
    {
        "title": "PhishSense: phishing email detector",
        "tag": "Team project · Data engineering lead",
        "featured": True,
        "stack": ["Python", "PyTorch", "Transformer encoder", "scikit-learn", "Pandas", "Google Colab"],
        "metrics": [("1.11M", "parameters, trained from scratch"), ("11,000", "emails from 8 sources"),
                    ("97.56%", "recall on modern phishing")],
        "points": [
            "Led data engineering for a from-scratch PyTorch Transformer that classifies emails as safe or phishing.",
            "Built a balanced corpus with MinHash LSH deduplication and leakage-free splits.",
            "Ablation tests showed the model does not learn shortcuts from the data source.",
        ],
        "repo": None,
    },
    {
        "title": "AI Voice Assistant",
        "tag": "Independent project",
        "stack": ["Python", "Streamlit", "Groq API", "Whisper", "Google TTS"],
        "points": ["Speech-to-speech pipeline: Whisper transcription, Groq LLM replies, Google TTS audio and a Streamlit interface."],
        "repo": None,
    },
    {
        "title": "Student Attendance Tracker",
        "tag": "Full stack project",
        "stack": ["React", "Vite", "Tailwind CSS", "Node.js", "Express.js", "PostgreSQL", "JWT"],
        "points": ["Role-based access for admins and teachers, with duplicate entries blocked by unique constraints.",
                   "Attendance percentages, monthly and cohort reports, and CSV export."],
        "repo": None,
    },
    {
        "title": "Face Emotion Detection System",
        "tag": "Internship project · CodeBind Technologies",
        "stack": ["Python", "OpenCV", "Machine learning", "Computer vision"],
        "points": ["Emotion recognition pipeline covering face detection, preprocessing and classification."],
        "repo": None,
    },
    {
        "title": "Google Workspace AI Executive Assistant",
        "tag": "Independent project",
        "stack": ["n8n", "Google Gemini API", "Google Workspace"],
        "points": ["n8n workflows on the Gemini API that automate tasks across Gmail, Calendar, Tasks and Drive."],
        "repo": None,
    },
]

# Newest first. current=True adds the "Working now" badge and live animation.
EXPERIENCE = [
    {"role": "Python Developer Intern", "company": "Zeeyes AI Lab, Tirunelveli", "when": "1 Sep 2026 – present",
     "text": "Developing Python-based AI application features in a 6-month full-time, on-site internship.",
     "current": True},
    {"role": "Python with AI and Machine Learning Intern", "company": "CodeBind Technologies, Chennai",
     "when": "Jun 2026", "text": "Built the Face Emotion Detection System with OpenCV during applied Python, AI and ML training."},
    {"role": "Python Development Intern", "company": "The Developers Arena (online)", "when": "Sep 2025",
     "text": "Solved guided exercises in core Python and algorithmic problem solving."},
    {"role": "Full Stack Web Development Intern", "company": "AK Infopark, Nagercoil", "when": "Apr – May 2025",
     "text": "Developed front-end web pages with HTML, CSS and JavaScript."},
]

EDUCATION = [
    {"title": "B.Tech, Artificial Intelligence and Data Science", "where": "Arunachala HiTech Engineering College",
     "when": "2024 – 2028", "score": "CGPA 8.23"},
    {"title": "Higher Secondary Certificate (HSC)", "where": "CMC Matriculation Higher Secondary School, Konam, Nagercoil",
     "when": "", "score": "81%"},
    {"title": "Secondary School Leaving Certificate (SSLC)", "where": "CMC Matriculation Higher Secondary School, Konam, Nagercoil",
     "when": "", "score": "84.2%"},
]

CERTIFICATIONS = [
    "Oracle Generative AI Certificate",
    "Data Science Essentials with Python, Cisco Networking Academy",
    "Python and Machine Learning Bootcamp, Corizo",
    "Python for Data Science, NPTEL",
    "Data Science Workshop, CodeBind Technologies",
    "Introduction to Cybersecurity, Cisco Networking Academy",
]

ACHIEVEMENTS = [
    "Presented the paper “Traffic Management” and served on the organizing committee, AIONIX 2025 Symposium.",
    "Participant, TATA Crucible Quiz (Prelims Level 1).",
    "Short-term training programme (STTP), Institution of Engineers, Durgapur Local Centre.",
]
