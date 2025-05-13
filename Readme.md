📝 Python To-Do Web App (No Framework)
This is a minimal web-based To-Do application built from scratch using only Python’s standard library (http.server). It demonstrates how to handle HTTP requests, serve HTML and static files, and manage simple data storage-all without any external frameworks.

🚀 Features
Add tasks to your To-Do list

View all tasks (persisted in a text file)

Simple HTML interface

Serves static assets (CSS, images, etc.)

Custom 404 error page

🛠️ Requirements
Python 3.x
(No external packages needed!)

📦 Installation
Clone this repository:

bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
(Optional) Create and activate a virtual environment:

bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
⚡ Usage
Run the application:

bash
python app.py
(Make sure you’re in the project directory and app.py is the main file.)

Open your web browser and go to:
http://localhost:8080

📁 Project Structure
your-repo-name/
│
├── main.py
├── data/
│   └── tasks.txt        # (auto-created) Stores your tasks
├── templates/
│   ├── index.html       # Main page template
│   └── 404.html         # 404 error page
├── static/
│   └── style.css        # (optional) Your CSS files
└── README.md
📝 How It Works
Server: Uses Python’s http.server to handle HTTP requests.

Routing:

/ - Home page (shows and adds tasks)

/add - Handles adding new tasks (POST)

/static/ - Serves static files (CSS, images, etc.)

Data Storage: Tasks are saved line-by-line in data/tasks.txt.

Templating: Simple HTML replacement for task list.


🛡️ Notes
The app creates a data/ directory and tasks.txt file automatically if they don’t exist.

Only basic error handling is provided.

For educational/demo purposes; not intended for production use.

📚 References
Python Official Docs: http.server

Build a Web Server in Python

🙌 Contributing
Pull requests and suggestions are welcome!

📧 Contact
For questions, reach out to srijanrayiembca2026@gmail.com

Feel free to copy, edit, and improve this README for your project! If you want, share your repo link for even more customization.