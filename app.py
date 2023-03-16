import pickle
from flet import *
from pages.home import Home
from pages.forgotpassword import ForgotPassword
from pages.dashboard import Dashboard
from pages.login import Login
from pages.signup import Signup
from service.auth2 import authenticate_token


class Main(UserControl):
    def __init__(self, page: Page,):
        super().__init__()
        page.padding = 0
        self.page = page
        self.init()

    def init(self,):
        self.page.on_route_change = self.on_route_change
        token = self.load_token()
        if authenticate_token(token):
            self.page.go('/me')
        else:
            self.page.go('/login')

    def on_route_change(self, route):
        new_page = {
            "/": Home,
            "/login": Login,
            "/signup": Signup,
            "/me": Dashboard,
            "/forgotpassword": ForgotPassword

        }[self.page.route](self.page)

        self.page.views.clear()
        self.page.views.append(
            View(route, [new_page])
        )

    def load_token(self,):
        try:
            with open('token.pickle', 'rb') as f:
                token = pickle.load(f)
            return token
        except:
            return None


app(target=Main, view=WEB_BROWSER)
