import imp
from pypi_org.db import fake_data


def get_page(base_url: str) -> dict | None:
    if not base_url or not base_url.strip():
        return None

    base_url = base_url.strip().lower()

    page = fake_data.pages.get(base_url)
    return page


def get_redirect(base_url: str) -> dict | None:
    if not base_url or not base_url.strip():
        return None

    base_url = base_url.strip().lower()

    redirect = fake_data.redirects.get(base_url)
    return redirect
