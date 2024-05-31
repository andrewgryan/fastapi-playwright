from multiprocessing import Process
import uvicorn
import pytest
from playwright.sync_api import Page, expect
from fastapi_vitest.main import app


def run_server():
    uvicorn.run(app)


@pytest.fixture(scope="session")
def server():
    proc = Process(target=run_server, args=(), daemon=True)
    proc.start() 
    yield
    proc.kill() # Cleanup after test


def test_htmx_org_example(page: Page, server):
    page.goto("http://127.0.0.1:8000/")
    page.get_by_role("button").click()
    expect(page.get_by_role("paragraph")).to_be_visible()
