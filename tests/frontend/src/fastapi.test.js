// @vitest-environment jsdom
import jsdom from "jsdom"
import { expect, test } from "vitest"


test("it works", () => {
  expect(2 + 2).toEqual(4)
})

test("htmx example", async () => {
  const url = "http://localhost:8000/"
  const dom = await jsdom.JSDOM.fromURL(url, { runScripts: "dangerously", resources: "usable" })
  const btn = dom.window.document.body.querySelector("button")
  dom.window.onload = () => {
    btn.click()
  }
  expect(dom.window.document.body.querySelector("button").innerHTML).toContain("Click Me")
})

test("settings route", async () => {
  const response = await fetch("http://localhost:8000/settings?name=Matt")
  const content = await response.text()
  const parser = new DOMParser()
  const elements = parser.parseFromString(content,"text/html")
  expect(elements.querySelector("h1").innerHTML).toEqual("Matt's account!")
})
