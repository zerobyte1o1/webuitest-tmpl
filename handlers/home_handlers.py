from pageObject.home_page import HomePage


class HomeHandlers(HomePage):
    def __init__(self):
        super(HomeHandlers, self).__init__()

    def change_password_handler(self):
        self.hi_lco().click()
        self.change_password_loc().click()

    def logout_handler(self):
        self.hi_lco().click()
        self.logout_loc()


if __name__ == '__main__':
    HomeHandlers().change_password()
