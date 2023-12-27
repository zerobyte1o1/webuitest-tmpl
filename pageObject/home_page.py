from pageObject.base_page import BasePage


class HomePage(BasePage):
    def __init__(self):
        super(HomePage, self).__init__()

    def hi_lco(self): return self.page.locator('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[2]/a')

    def change_password_loc(self): return self.page.locator('//*[text()="修改密码"]')

    def logout_loc(self): return self.page.locator('//*[text()="退出登录"]')