# Vwoollo Product Scraper

Production-grade fashion product scraper for [Vwoollo](https://vwoollo.com/?currency=EUR).

## Features

- Scrapes Vwoollo collections (knit hoodies, star hoodies, sweaters, shoes, headwear, wallets, accessories, discover)
- Uses Shopify `products.json` endpoints with `?currency=EUR` + `cart_currency=EUR` cookie
- Paginates with `limit=50` until an empty page
- Generates 768-d SigLIP embeddings locally (`google/siglip-base-patch16-384`) — **no HuggingFace API token, no Gemini**
- Optional back-view embeddings when gallery/alt/URL signals a back shot
- Smart diffing: skip unchanged products; only re-embed when image/text fields change
- Batch upserts to Supabase (≤5/request) with single-row fallback; never upserts `embedding_version`
- Stale cleanup after 2 consecutive misses (local tracker)
- GitHub Actions: **Mon/Tue 10:05 UTC** + `workflow_dispatch`

## Architecture

```
main.py              # Orchestrates scrape → embed → upsert
config.py            # Brand + env configuration
parser.py            # Shopify products.json extraction (EUR)
embeddings.py        # Local SigLIP image + text embeddings
supabase_client.py   # Batch upsert + stale cleanup
.github/workflows/
  scrape.yml         # Mon/Tue/Thu schedule
```

## Setup

### Local

```bash
pip install -r requirements.txt
cp .env.example .env
# Fill SUPABASE_URL and SUPABASE_KEY
python main.py
```

### GitHub Actions

Repository secrets (only):
- `SUPABASE_URL`
- `SUPABASE_KEY`

No HuggingFace token needed — the model runs locally and is cached under `~/.cache/huggingface`.

## Back-view detection

Back shots are detected from image URL/alt keywords (`back`, `rear`, `_b.`, `_back`, etc.). When found:
- `back_image_url` + `back_image_embedding` are set
- URL is also listed in `additional_images`
- `image_url` always stays the front packshot (what the iOS app displays)

## Source fields

- `source`: `scraper-vwoollo`
- `brand`: `Vwoollo`
- `second_hand`: `false`
- Prices preferred in EUR (`89.90EUR`)