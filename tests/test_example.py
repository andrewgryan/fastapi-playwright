from playwright.sync_api import Page, expect


def test_htmx_org_example(page: Page, server):
    page.goto("http://127.0.0.1:8000/")
    page.get_by_role("button").click()
    expect(page.get_by_role("heading")).to_contain_text("Hello, World!")
    expect(page.get_by_role("paragraph")).to_contain_text("Hello, HTMX!")


def test_settings_default_user(page: Page, server):
    page.goto("http://127.0.0.1:8000/settings")
    expect(page.get_by_role("heading")).to_contain_text("Matt's account!")


def test_settings_custom_user(page: Page, server):
    page.goto("http://127.0.0.1:8000/settings?name=Tom")
    expect(page.get_by_role("heading")).to_contain_text("Tom's account!")
