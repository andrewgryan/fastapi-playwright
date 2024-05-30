from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index():
    return "<h1>Hello, World!</h1>"


@app.get("/settings", response_class=HTMLResponse)
def index():
    return "<h1>User account</h1>"
