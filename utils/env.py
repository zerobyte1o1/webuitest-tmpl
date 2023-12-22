import configparser
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
configPath = os.path.join(BASE_DIR, "../config/env.ini")
cf = configparser.ConfigParser()
cf.read(configPath, encoding='UTF-8')

pick = cf.get("pick", "env")

environment = cf.get(pick, "env")
headless = cf.get(pick, "headless")
account = cf.get(pick, "account")
password = cf.get(pick, "password")


class Environment:
    def login_url(self):
        return "https://" + environment + "/#/login"

    def account(self):
        return account

    def password(self):
        return password

    def headless(self):
        return headless


if __name__ == "__main__":
    env = Environment()
    # print(env.url(module="flow"))
    print(environment)
    # print(account, password)
