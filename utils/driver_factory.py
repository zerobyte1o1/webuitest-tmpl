from playwright.sync_api import sync_playwright
from utils.env import Environment


class DriverFactory:
    # 静态属性
    page = None
    env = Environment()

    @classmethod
    def get_driver(cls):
        if cls.page is None:
            playwright = sync_playwright().start()
            if cls.env.headless() == 'True':
                browser = playwright.chromium.launch(headless=True)
            else:
                browser = playwright.chromium.launch(headless=False)
            cls.page = browser.new_page()
            cls.page.goto(cls.env.login_url())
            cls.page.locator('//*[@placeholder="username"]').fill(cls.env.account())
            cls.page.locator('//*[@placeholder="password"]').fill(cls.env.password())
            cls.page.click('//button')
        return cls.page


if __name__ == '__main__':
    DriverFactory.get_driver()
