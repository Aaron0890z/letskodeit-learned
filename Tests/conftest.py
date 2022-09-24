import pytest
from selenium import webdriver
from Base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage


@pytest.fixture()
def setUp():
    print("Before method")
    yield
    print(" After method")


@pytest.fixture(scope="class")     # "session", "package", "module", "class", "function"
def oneSetUp(request, browser):      # pytest -s -v OrderingPrac.py --browser Firefox / browser is from def browser line no 46
    print("Running one time setup")
    wdf = WebDriverFactory(browser)     # WebDriverFactory accepts browser
    driver = wdf.getWebDriverInstance()     # getWebDriverInstance returns driver with browser config
    lp = LoginPage(driver)
    lp.login("test@email.com", "abcabc")

    # if browser == "Firefox":
    #     print("Running in firefox")         # video 164
    #     baseurl = "https://courses.letskodeit.com/practice"
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     driver.implicitly_wait(2)
    #     driver.get(baseurl)
    # else:
    #     print("Running in Chrome")
    #     driver = webdriver.Chrome()
    #     baseurl = "https://courses.letskodeit.com/practice"
    #     driver.get(baseurl)

    if request.cls is not None:             # returning driver value from fixture which is available for scope = class
        request.cls.driver = driver         # make driver as class attr, so it's available to whole test class / eg: https://gist.github.com/highsmallxu/7ab383bee1bf1f375a66dc8d85ee403c
                                            # https://www.lambdatest.com/blog/end-to-end-tutorial-for-pytest-fixtures-with-examples/
    yield driver                            # adding driver attribute to the test class using request / if class attribute is not null
    driver.quit()
    print(" After all methods over")


def pytest_addoption(parser):       # creating options for cmd mode pytest_addoption (case sensitive)
    parser.addoption("--browser")   # https://www.codementor.io/@adammertz/pytest-quick-tip-adding-cli-options-1fpqnnaokc
    parser.addoption("--osType")    # https://code-maven.com/slides/python/add-extra-command-line-parameters


@pytest.fixture(scope="session")
def browser(request):               # setting the options
    return request.config.getoption("--browser")    # getoption will return whatever value after --browser


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

# py.test -s -v pyTestTuts\Test_For_Code2.py --browser Chrome --html=report.html