from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index():
    # HTMX homepage example
    return """
<!DOCTYPE html>
<html>
    <head>
        <script src="http://localhost:8000/static/script.js"></script>
    </head>
    <body>
        <!-- have a button POST a click via AJAX -->
        <button onclick="console.log('Hello, Click!')">
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

@app.get("/static/script.js", response_class=HTMLResponse)
def settings():
    return "console.log('Hello, World!')"
