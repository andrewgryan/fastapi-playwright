// @vitest-environment jsdom
import { JSDOM } from "jsdom"
import { expect, test } from "vitest"

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms))
}

test("htmx example", async () => {
  const url = "http://localhost:8000/"
  const { window } = await JSDOM.fromURL(url, { runScripts: "dangerously", resources: "usable"})
  // window.htmx = htmx
  window.htmx = require("htmx.org")
  window.onload = () => console.log("Hello")
  
  const btn = window.document.getElementById("normal")
  await sleep(100)
  btn.click()
  // expect(btn.innerHTML).toContain("Click Me")
})
