"""Vwoollo scraper configuration."""
import os
from dataclasses import dataclass, field
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    BRAND_NAME: str = "Vwoollo"
    SOURCE: str = "scraper-vwoollo"
    BRAND_COLUMN: str = "Vwoollo"
    SECOND_HAND: bool = False
    LANDING_PAGE: str = "https://vwoollo.com/?currency=EUR"
    BASE_URL: str = "https://vwoollo.com"
    CURRENCY: str = "EUR"
    PRODUCTS_JSON_LIMIT: int = 50

    CATEGORY_URLS: list[str] = field(default_factory=lambda: [
        "https://vwoollo.com/collections/knit-hoodie",
        "https://vwoollo.com/collections/star-knit-hoodie",
        "https://vwoollo.com/collections/star-knit-zip-up-hoodie",
        "https://vwoollo.com/collections/stellar-knit-hoodie",
        "https://vwoollo.com/collections/circle-hoodie",
        "https://vwoollo.com/collections/heavy-knit-sweater",
        "https://vwoollo.com/collections/double-layer-puffy-hoodie",
        "https://vwoollo.com/collections/double-layer-puffy-zip-up-hoodie",
        "https://vwoollo.com/collections/gold-star-button-hoodie",
        "https://vwoollo.com/collections/cropped-knit-sweatpant",
        "https://vwoollo.com/collections/star-shoes",
        "https://vwoollo.com/collections/headwear",
        "https://vwoollo.com/collections/wallet",
        "https://vwoollo.com/collections/accessories",
        "https://vwoollo.com/collections/discover",
    ])

    CATEGORY_DISPLAY: dict[str, str] = field(default_factory=lambda: {
        "knit-hoodie": "Knit Hoodies",
        "star-knit-hoodie": "Star Knit Hoodies",
        "star-knit-zip-up-hoodie": "Star Knit Zip-Up Hoodies",
        "stellar-knit-hoodie": "Stellar Knit Hoodies",
        "circle-hoodie": "Circle Hoodies",
        "heavy-knit-sweater": "Heavy Knit Sweaters",
        "double-layer-puffy-hoodie": "Double-Layer Puffy Hoodies",
        "double-layer-puffy-zip-up-hoodie": "Double-Layer Puffy Zip-Up Hoodies",
        "gold-star-button-hoodie": "Gold Star Button Hoodies",
        "cropped-knit-sweatpant": "Cropped Knit Sweatpants",
        "star-shoes": "Star Shoes",
        "headwear": "Headwear",
        "wallet": "Wallets",
        "accessories": "Accessories",
        "discover": "Discover",
    })

    SUPABASE_URL: str = field(default_factory=lambda: os.getenv("SUPABASE_URL", ""))
    SUPABASE_KEY: str = field(default_factory=lambda: os.getenv("SUPABASE_KEY", ""))

    EMBEDDING_MODEL: str = "google/siglip-base-patch16-384"
    EMBEDDING_DIM: int = 768
    EMBEDDING_VERSION: int = 2
    RATE_LIMIT_DELAY: float = 1.0
    BATCH_SIZE: int = 5
    STALE_MISS_THRESHOLD: int = 2
    REQUEST_TIMEOUT: int = 30
    USER_AGENT: str = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    )


cfg = Config()