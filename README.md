# piffyart

Django scaffold for a responsive blob-grid homepage.

## Included structure

- `home` for the homepage and about modal
- `accounts` for login and dashboard access
- `personal`, `digital`, `community`, `shop`, and `contact` as separate routed app areas
- `contact` includes a database-backed message model
- `shop` includes a product model for storefront management

## Run locally

1. Create a virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Run `python manage.py migrate`.
4. Start the server with `python manage.py runserver`.