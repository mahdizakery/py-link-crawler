# Py Link Crawler

Py Link Crawler is a Python-based web crawler that uses Playwright to extract and filter links from web pages. The crawler starts from a given URL and collects all links within the same base domain, saving them to a JSON file and removing duplicates.

## Requirements

- Python 3.7+
- Playwright

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/mahdizakery/py-link-crawler.git
    cd py-link-crawler
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Install Playwright browsers:
    ```sh
    playwright install
    ```

## Usage

1. Update the `start_url` variable in `link_crawler.py` with the URL you want to start crawling from.

2. Run the crawler:
    ```sh
    python link_crawler.py
    ```

3. The collected links will be saved to `all_links.json`.

## Functions

- `get_base_domain(url)`: Extracts the base domain from a URL.
- `get_all_links(url, base_domain)`: Retrieves all links from a page and filters them by the base domain.
- `find_all_pages(start_url)`: Crawls the web starting from the given URL and collects all links within the same base domain.
- `save_links_to_json(links, filename)`: Saves the collected links to a JSON file.
- `remove_duplicates_from_json(filename)`: Removes duplicate links from the JSON file.

## License

This project is licensed under the MIT License.