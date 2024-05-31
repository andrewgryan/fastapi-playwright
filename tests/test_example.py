import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("http://127.0.0.1:8000/")
    page.on("console", lambda msg: print(msg.text))
    page.get_by_role("button").click()
    expect(page.get_by_role("paragraph")).to_be_visible()
