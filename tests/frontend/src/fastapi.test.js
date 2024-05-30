// @vitest-environment happy-dom
import { expect, test } from "vitest"


test("it works", () => {
  expect(2 + 2).toEqual(4)
})

test("index route", async () => {
  const response = await fetch("http://localhost:8000/")
  const content = await response.text()
  const parser = new DOMParser()
  const elements = parser.parseFromString(content,"text/html")
  expect(elements.querySelector("h1").innerHTML).toEqual("Hello, World!")
})
