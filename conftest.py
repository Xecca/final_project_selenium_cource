import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', 
    help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en", help="Choose language: ru or en-gb")

def pytest_configure(config):
    config.addinivalue_line("markers", "lang_test: mark test as choose language")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print ("\n start Chrome browser for test ...")
        browser = webdriver.Chrome()
        # browser.implicitly_wait(12)
    elif browser_name == "firefox":
        print ("\n start Firefox browser for test ...")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name shoul be chrome or firefox")
    yield browser
    print("\n quit browser..")
    browser.quit()

@pytest.fixture(scope="function")
def user_language(request):
    language = request.config.getoption("language")
    if language == 'ru':
        print("\nYou chose russian language for test!")
        return (language)
    elif language == 'en':
        print("\nYou chose english language for test!")
        return ('en-gb')
    elif language == 'fr':
        print(f"\nYou chose français language for test!")
        return (language)
    elif language == 'ar':
        print(f"\nYou chose العربيّةlanguage for test!")
        return (language)
    elif language == 'ca':
        print(f"\nYou chose català language for test!")
        return (language)
    elif language == 'cs':
        print(f"\nYou chose česky language for test!")
        return (language)
    elif language == 'da':
        print(f"\nYou chose dansk language for test!")
        return (language)
    elif language == 'de':
        print(f"\nYou chose deutsch language for test!")
        return (language)
    elif language == 'el':
        print(f"\nYou chose Ελληνικά language for test!")
        return (language)
    elif language == 'es':
        print(f"\nYou chose español language for test!")
        return (language)
    elif language == 'fi':
        print(f"\nYou chose suomi language for test!")
        return (language)
    elif language == 'pl':
        print(f"\nYou chose polski language for test!")
        return (language)
    else:
        print(f"You was enter {language}! This language is not supported! Enter another language!")