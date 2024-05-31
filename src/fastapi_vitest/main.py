import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/", response_class=HTMLResponse)
def index():
    # HTMX homepage example
    return """
<!DOCTYPE html>
<html>
    <head>
        <script src="/static/htmx.js"></script>
    </head>
    <body>
        <!-- have a button POST a click via AJAX -->
        <button hx-post="/clicked" hx-swap="outerHTML">
            Click Me
        </button>
    </body>
</html>
"""


@app.post("/clicked", response_class=HTMLResponse)
def clicked():
    return "<p>Clicked!</p>"


@app.get("/settings", response_class=HTMLResponse)
def settings():
    name = "Matt"
    return f"<h1>{name}'s account!</h1>"
