import random

from flask import redirect
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


def all_pages() -> list[dict]:
    return list(fake_data.pages.values())


def all_redirects() -> list[dict]:
    return list(fake_data.redirects.values())


def get_redirect_by_id(redirect_id: int) -> dict | None:
    for url, redirect in fake_data.redirects.items():
        if redirect.get('id') == redirect_id:
            return redirect
    
    return None


def get_page_by_id(page_id: int) -> dict | None:
    for url, page in fake_data.pages.items():
        if page.get('id') == page_id:
            return page
    
    return None


def create_redirect(name: str, short_url: str, url: str) -> None:
    if get_redirect(short_url):
        raise Exception("Cannot create redirect, exists")
    
    data = {
        'id': random.randint(100, 1_000_000),
        'url': url,
        'short_url': short_url,
        'name': name
    }

    fake_data.redirects[short_url] = data


def update_redirect(redirect_id: int, name: str, short_url: str, url: str):
    redirect = get_redirect_by_id(redirect_id)

    if not redirect:
        raise Exception("Cannot update redirect, does not exist")

    del fake_data.redirects[redirect.get('short_url')]

    redirect['short_url'] = short_url
    redirect['url'] = url
    redirect['name'] = name

    fake_data.redirects[short_url] = redirect


def create_page(title: str, url: str, contents: str) -> None:
    if get_page(url):
        raise Exception("Cannot create page, exists")
    
    data = {
        'id': random.randint(100, 1_000_000),
        'url': url,
        'title': title,
        'contents': contents
    }

    fake_data.pages[url] = data


def update_redirect(page_id: int, title: str, url: str, contents: str):
    page = get_page_by_id(page_id)

    if not page:
        raise Exception("Cannot update page, does not exist")

    del fake_data.pages[page.get('url')]

    page['url'] = url.strip().lower()
    page['contents'] = contents.strip()
    page['title'] = title.strip()

    fake_data.pages[url] = page
