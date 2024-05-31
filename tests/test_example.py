import re
from playwright.sync_api import Page, expect

def test_htmx_org_example(page: Page):
    page.goto("http://127.0.0.1:8000/")
    page.get_by_role("button").click()
    expect(page.get_by_role("paragraph")).to_be_visible()
