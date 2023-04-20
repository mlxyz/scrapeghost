from dotenv import load_dotenv
load_dotenv()

from pprint import pprint
from scrapeghost import SchemaScraper
from scrapeghost.preprocessors import CSSUnified


url = "https://kaffeerista.de/products/kaffeerista-der-gouverneur-mischung?awc=32275_1681979585_6e67dfc126ae006d396e875e13a5a2b4"
schema = {
    "product_description": "str",
    "product_title": "str",
    "product_specifications": "list[str]",
}

episode_scraper = SchemaScraper(schema, extra_preprocessors=[CSSUnified(
    ".product-title,.product-description.rte")], engine='gpt-35')

response = episode_scraper(url)
pprint(response.data)
print(response.data)
print(f"Total Cost: ${response.total_cost:.3f}")
