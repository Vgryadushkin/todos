from playwright.sync_api import sync_playwright
from pytest import fixture

from todomvc_model.todomvc import TodoMVC


@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright

@fixture
def desctop_todomvc(get_playwright):
    todomvc = TodoMVC(get_playwright)
    yield todomvc
    todomvc.close()