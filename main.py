from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import os

class ToDoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" : #or self.path.startswith("/?")
            self.render_home()
        elif self.path.startswith("/static/"):
            self.serve_static("." + self.path)
        else:
            self.serve_file("templates/404.html", 404)

    def do_POST(self):
        if self.path == "/add":
            content_len = int(self.headers.get('Content-Length'))
            post_data = self.rfile.read(content_len)
            fields = parse_qs(post_data.decode())

            task = fields.get("task", [""])[0].strip()
            if task:
                with open("data/tasks.txt", "a") as f:
                    f.write(task + "\n")
            self.send_response(303)
            self.send_header("Location", "/")
            self.end_headers()

    def render_home(self):
        try:
            with open("templates/index.html", "r") as f:
                html = f.read()

            if os.path.exists("data/tasks.txt"):
                with open("data/tasks.txt", "r") as f:
                    tasks = f.readlines()
            else:
                tasks = []

            task_items = "".join(f"<li>{t.strip()}</li>" for t in tasks)
            html = html.replace("{{tasks}}", task_items)

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())
        except Exception as e:
            self.send_error(500, str(e))

    def serve_file(self, path, status=200):
        try:
            with open(path, "rb") as f:
                self.send_response(status)
                if path.endswith(".html"):
                    self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f.read())
        except FileNotFoundError:
            self.send_error(404, "File not found")

    def serve_static(self, path):
        try:
            with open(path, "rb") as f:
                self.send_response(200)
                if path.endswith(".css"):
                    self.send_header("Content-type", "text/css")
                self.end_headers()
                self.wfile.write(f.read())
        except:
            self.send_error(404, "Static file not found")

def run():
    os.makedirs("data", exist_ok=True)
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, ToDoHandler)
    print("Serving at http://localhost:8080")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
