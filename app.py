from fastapi import FastAPI
from playwright.sync_api import sync_playwright

app = FastAPI()

@app.get("/download")
def download():

    with sync_playwright() as p:

        browser = p.chromium.launch()

        page = browser.new_page()

        page.goto(
            "https://challenges.geovelo.app/193/?participant-types=association&holding-groups=false"
        )

        title = page.title()

        browser.close()

    return {
        "title": title
    }
