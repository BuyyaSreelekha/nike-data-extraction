from playwright.sync_api import sync_playwright
import time

BASE_URL = "https://www.nike.com/ph/w"

def scroll_all_products(page):
    last_height = 0
    while True:
        page.mouse.wheel(0, 4000)
        time.sleep(2)
        new_height = page.evaluate("document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def get_product_links(page):
    links = page.locator("a[href*='/t/']").all()
    urls = set()
    for link in links:
        href = link.get_attribute("href")
        if href:
            urls.add("https://www.nike.com" + href)
    return list(urls)

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(BASE_URL, timeout=60000)

        print("Scrolling to load all products...")
        scroll_all_products(page)

        product_urls = get_product_links(page)
        print(f"Total products found: {len(product_urls)}")

        browser.close()

if __name__ == "__main__":
    main()
