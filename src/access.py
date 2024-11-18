from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Configure Selenium with headless option for simplicity
def setup_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # Update path to your Chrome WebDriver
    service = Service('lib/chromedriver-mac-x64/chromedriver') 
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.119 Safari/537.36")
    browser = webdriver.Chrome(service=service, options=chrome_options)
    return browser

def download_final_page(browser, url):
    html_content = ""
    try:
        # Access the URL
        browser.get(url)

        # Wait for redirection (if needed, you can also add explicit waits here)
        browser.implicitly_wait(5)

        # Get the final URL after redirection
        final_url = browser.current_url
        print(f"Final URL after redirection: {final_url}")

        # Get the HTML content of the final page
        html_content = browser.page_source

        # # Save the HTML content to a file
        # with open("final_page.html", "w", encoding="utf-8") as file:
        #     file.write(html_content)

        print("Final page content downloaded successfully.")
        return html_content
    finally:
        # Close the browser
        browser.quit()
        print("Final page content downloaded failure.")
        return html_content

# Example usage
if __name__ == "__main__":
    url_to_access = "https://doi.org/10.1109/TSE.2023.3345800"  # Replace with your initial URL
    download_final_page(url_to_access)
