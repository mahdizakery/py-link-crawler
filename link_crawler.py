## LINK CRAWLER

import asyncio
import json
from urllib.parse import urlparse
from playwright.async_api import async_playwright

# Function to extract the base domain from a URL
def get_base_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

async def get_all_links(url, base_domain):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # Use headless=False to see the browser
        page = await browser.new_page()
        await page.goto(url)

        # Get all the links on the page
        links = await page.eval_on_selector_all('a', 'elements => elements.map(el => el.href)')

        # Filter links to only include those with the same base domain
        filtered_links = [link for link in links if get_base_domain(link) == base_domain]

        await browser.close()
        return filtered_links

async def find_all_pages(start_url):
    visited = set()
    to_visit = [start_url]
    all_links = []

    # Extract the base domain from the starting URL
    base_domain = get_base_domain(start_url)

    while to_visit:
        current_url = to_visit.pop()
        if current_url not in visited:
            visited.add(current_url)
            print(f"Visiting: {current_url}")
            links = await get_all_links(current_url, base_domain)
            all_links.extend(links)

            # Add new links to visit
            for link in links:
                if link not in visited:
                    to_visit.append(link)

    return all_links

# Function to save the links to a JSON file
def save_links_to_json(links, filename):
    with open(filename, 'w') as f:
        json.dump(links, f, indent=4)

# Function to remove duplicates from a JSON file
def remove_duplicates_from_json(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    if not isinstance(data, list):
        print("Error: JSON data is not a list.")
        return

    unique_data = list(set(data))

    with open(filename, 'w') as f:
        json.dump(unique_data, f, indent=4)

    print(f"Duplicates removed from '{filename}'.")

# Main function to run the crawler
def main():
    start_url = 'https://example.com'  # Ensure the URL is complete with 'http' or 'https'

    # Run the async function within the existing event loop
    all_links = asyncio.run(find_all_pages(start_url))

    # Save the collected links to a JSON file
    save_links_to_json(all_links, 'all_links.json')

    print(f'Total number of links found: {len(all_links)}')
    print(all_links[:10])  # Print first 10 links as a sample

    # Remove duplicates from the JSON file
    remove_duplicates_from_json('all_links.json')

if __name__ == "__main__":
    main()