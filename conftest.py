import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# add option for language
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language.")

# fixture for browser start\stop
@pytest.fixture(scope="function")
def browser(request):
    browser_lang = request.config.getoption("language")
    browser = None
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
    browser = webdriver.Chrome(options=options)
    print("\nstart browser for test")
    yield browser
    print("\nquit browser..")
    browser.quit()