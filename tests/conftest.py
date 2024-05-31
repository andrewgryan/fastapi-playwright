import pytest
from multiprocessing import Process
import uvicorn
from fastapi_playwright.main import app



def run_server():
    uvicorn.run(app)


@pytest.fixture(scope="session")
def server():
    proc = Process(target=run_server, args=(), daemon=True)
    proc.start() 
    yield
    proc.kill() # Cleanup after test
