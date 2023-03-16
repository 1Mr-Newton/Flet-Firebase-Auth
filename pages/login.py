import re
from flet import *
from service.auth2 import login_user, store_session
from utils.validation import Validator


class Login(Container):
    def __init__(self, page: Page):
        super().__init__()
        page.padding = 0
        self.validator = Validator()
        self.expand = True
        self.bgcolor = '#4e73df'
        self.alignment = alignment.center
        self.error_border = border.all(width=1, color='red')
        self.email_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(
                    top=0, bottom=0, right=20, left=20),
                hint_style=TextStyle(
                    size=12, color='#858796'
                ),
                hint_text='Enter email address...',
                cursor_color='#858796',
                text_style=TextStyle(
                    size=14,
                    color='black',
                ),

            ),
            border=border.all(width=1, color='#bdcbf4'),
            border_radius=30
        )

        self.password_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(
                    top=0, bottom=0, right=20, left=20),
                hint_style=TextStyle(
                    size=12, color='#858796'
                ),
                text_style=TextStyle(
                    size=14,
                    color='black',
                ),
                hint_text='Password',
                cursor_color='#858796',
                password=True,


            ),
            border=border.all(width=1, color='#bdcbf4'),
            border_radius=30
        )

        self.content = Column(
            alignment='center',
            horizontal_alignment='center',
            controls=[
                Container(
                    width=500,
                    border_radius=12,
                    padding=40,
                    bgcolor='white',
                    content=Column(
                        horizontal_alignment='center',
                        controls=[
                            Text(
                                value="Welcome Back!",
                                size=16,
                                color='black',
                                text_align='center'
                            ),

                            self.email_box,

                            self.password_box,
                            Container(height=0),

                            Container(
                                alignment=alignment.center,
                                bgcolor='#4e73df',
                                height=40,
                                border_radius=30,
                                content=Text(
                                    value='Login'
                                ),
                                on_click=self.login
                            ),
                            Container(height=0),
                            Container(
                                content=Text(
                                    value='Forgot Password?',
                                    color='#4e73df',
                                    size=12
                                ),
                                on_click=lambda _: (
                                    setattr(self.page, 'data', self.email_box.content.value), self.page.go('/forgotpassword'))

                            ),
                            Container(
                                content=Text(
                                    value='Create New Account',
                                    color='#4e73df',
                                    size=12
                                ),
                                on_click=lambda _: self.page.go('/signup')
                                # on_click=lambda _: (
                                #     setattr(self.page, 'data', self.email_box.content.value), self.page.go('/signup'))

                            )
                        ]
                    )
                )

            ]
        )

    def login(self, e):
        if not self.validator.is_valid_email(self.email_box.content.value):
            self.email_box.border = self.error_border
            self.email_box.update()

        if not self.validator.is_valid_password(self.password_box.content.value):
            self.password_box.border = self.error_border
            self.password_box.update()

        else:
            email = self.email_box.content.value
            password = self.password_box.content.value

            self.page.splash = ProgressBar()
            self.page.update()

            token = login_user(email, password)
            self.page.splash = None
            self.page.update()
            if token:
                store_session(token)
                self.page.go('/me')
            else:
                self.page.snack_bar = SnackBar(
                    Text('Invalid credentials')
                )
                self.page.snack_bar.open = True
                self.page.update()
