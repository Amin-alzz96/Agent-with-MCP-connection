from mcp.server.fastmcp import FastMCP
from typing import List, Dict
import requests
from bs4 import BeautifulSoup


class WebScraper:
    """Simple web scraping tool for extracting data from websites.
    
    Provides basic web scraping capabilities with error handling.
    """
    
    def __init__(self):
        """Initialize the web scraper with default settings."""
        self.session = requests.Session()
        
    def scrape(self, url: str, selector: str) -> List[Dict[str, str]]:
        """Scrape elements from a webpage matching the CSS selector.
        
        Args:
            url: URL of the webpage to scrape
            selector: CSS selector to find elements
            
        Returns:
            List of dictionaries with 'text' and 'attributes' for each element
            or error dictionary if scraping fails
        """
        try:
            response = self.session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            elements = soup.select(selector)
            return [{
                'text': el.get_text(strip=True),
                'attributes': dict(el.attrs)
            } for el in elements]
        except Exception as e:
            return {"error": str(e)}
    
    def web_scrape(self) -> Dict:
        """Return all information about the WebScraper instance.
        
        Returns:
            Dictionary containing class documentation and available methods.
        """
        return {
            "description": self.__doc__,
            "methods": {
                "scrape": self.scrape.__doc__
            }
        }


# MCP Tool Registration
mcp = FastMCP()
web_scraper = WebScraper()

@mcp.tool()
def scrape_website(url: str, selector: str) -> List[Dict[str, str]]:
    """MCP Tool: Scrape website using WebScraper instance.
    
    Args:
        url: Website URL to scrape
        selector: CSS selector to extract elements
        
    Returns:
        List of scraped elements or error dictionary
    """
    return web_scraper.scrape(url, selector)


if __name__ == "__main__":
    mcp.run()
