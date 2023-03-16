
from flet import *
from utils.colors import *
from flet.plotly_chart import PlotlyChart
import plotly.graph_objs as go
import random
from service.auth2 import load_token, get_name, revoke_token


class Dashboard(Container):
    def __init__(self, page: Page):
        super().__init__()

        page.padding = 0
        self.expand = True
        fig = self.get_fig()
        self.current_user_name = get_name(load_token())

        self.content = Row(
            spacing=0,
            controls=[
                Container(
                    width=220,
                    bgcolor=blue,
                    padding=padding.only(top=20, left=10, right=10),
                    content=Column(
                        controls=[
                            Row(
                                controls=[
                                    Icon(
                                        icons.PERSON,
                                        size=50
                                    )
                                ]
                            ),
                            Divider(
                                color='#9caede',
                                height=0.5,
                                thickness=.5
                            ),
                            Container(
                                Text(
                                    value="Dashboard",
                                    size=14,
                                    color='white'
                                ),
                            ),
                            Divider(
                                color='#9caede',
                                height=0.5,
                                thickness=.5
                            ),
                            Container(
                                Text(
                                    value="Utilities",
                                    size=14,
                                    color='white'
                                ),
                            ),
                            Divider(
                                color='#9caede',
                                height=0.5,
                                thickness=.5
                            ),

                            Row(
                                alignment='center',
                                controls=[
                                    Container(
                                        alignment=alignment.center,
                                        height=35,
                                        width=35,
                                        bgcolor='#9caede',
                                        border_radius=20,
                                        content=Icon(
                                            icons.ARROW_BACK_IOS,
                                            size=12,
                                        )
                                    ),
                                ]
                            ),
                            Container(
                                height=200,
                                bgcolor='#3c5ec1',
                                border_radius=5,
                                alignment=alignment.center,
                                content=Column(
                                    horizontal_alignment='center',
                                    alignment='center',
                                    controls=[
                                        Text(
                                            value="This site was designed by: @1MrNewton on YouTube",
                                            text_align='center',
                                            color='#9caede'
                                        ),
                                        Container(
                                            on_click=lambda _: self.page.launch_url(
                                                "https://youtube.com/@1mrnewton", "Mr. Newton",),
                                            alignment=alignment.center,
                                            height=35, width=110,
                                            border_radius=5,
                                            bgcolor='#1cc88a',
                                            content=Text(
                                                value="Visit Channel",
                                            )
                                        ),
                                        Container(
                                            on_click=lambda _: (revoke_token(
                                                load_token()), self.page.go('/login')),
                                            alignment=alignment.center,
                                            height=35, width=110,
                                            border_radius=5,
                                            bgcolor='#66FFFFFF',
                                            content=Text(
                                                value="Log Out",
                                                color='black',
                                                size=14,
                                                weight=FontWeight.W_600
                                            )
                                        )
                                    ]
                                )

                            )
                        ]
                    )
                ),


                Container(
                    expand=True,
                    bgcolor=white,
                    content=Column(
                        expand=True,

                        controls=[
                            Container(
                                height=70, shadow=BoxShadow(
                                    spread_radius=2,
                                    blur_radius=20,
                                    color='#1a000000'
                                ),
                                padding=padding.only(
                                    left=30, top=10, bottom=10, right=10),
                                bgcolor=white,
                                content=Row(
                                    alignment='spaceBetween',
                                    controls=[
                                        Row(
                                            spacing=0,
                                            controls=[
                                                Container(
                                                    bgcolor='#f8f9fc',
                                                    width=350,
                                                    height=40,
                                                    border_radius=BorderRadius(
                                                            topLeft=5, topRight=0, bottomLeft=5, bottomRight=0),
                                                    content=TextField(
                                                        border=InputBorder.NONE,
                                                        hint_text='Search for...',
                                                        hint_style=TextStyle(
                                                            color='#66000000',
                                                            size=12,
                                                        ),
                                                        content_padding=padding.only(
                                                            top=0, bottom=10, left=20, right=10,
                                                        ),
                                                        text_style=TextStyle(
                                                            color='black',
                                                            size=12,
                                                            weight=FontWeight.W_600

                                                        )

                                                    )


                                                ),

                                                Container(
                                                    height=40, width=40, bgcolor=blue, border_radius=BorderRadius(
                                                        topLeft=0,
                                                        topRight=5, bottomLeft=0, bottomRight=5
                                                    ),
                                                    content=Icon(
                                                        icons.SEARCH
                                                    )
                                                ),
                                            ]
                                        ),
                                        Row(
                                            spacing=15,
                                            controls=[

                                                Container(
                                                    alignment=alignment.center,
                                                    content=Stack(
                                                        controls=[
                                                            Container(
                                                                content=Icon(
                                                                    icons.NOTIFICATIONS,
                                                                    size=25,
                                                                    color='#dddfeb'
                                                                ),
                                                                margin=10
                                                            ),
                                                            Container(
                                                                height=15,
                                                                width=18,
                                                                bgcolor='red',
                                                                border_radius=5,
                                                                right=3,
                                                                top=11,
                                                                alignment=alignment.center,
                                                                content=Text(
                                                                    value='1+',
                                                                    size=9
                                                                )
                                                            )
                                                        ]
                                                    )

                                                ),
                                                Container(
                                                    alignment=alignment.center,
                                                    content=Stack(
                                                        controls=[
                                                            Container(
                                                                content=Icon(
                                                                    icons.NOTIFICATIONS,
                                                                    size=25,
                                                                    color='#dddfeb'
                                                                ),
                                                                margin=10
                                                            ),
                                                            Container(
                                                                height=15,
                                                                width=18,
                                                                bgcolor='red',
                                                                border_radius=5,
                                                                right=3,
                                                                top=11,
                                                                alignment=alignment.center,
                                                                content=Text(
                                                                    value='1+',
                                                                    size=9
                                                                )
                                                            )
                                                        ]
                                                    )

                                                ),
                                                Container(
                                                    height=30,
                                                    width=1,
                                                    bgcolor='#66000000'
                                                ),

                                                CircleAvatar(
                                                    foreground_image_url="",
                                                    radius=15
                                                )

                                            ]
                                        ),
                                    ]
                                )

                            ),

                            Column(
                                expand=True,
                                scroll='auto',
                                controls=[

                                    Container(
                                        padding=20,
                                        content=Row(
                                            alignment='spaceBetween',
                                            controls=[
                                                Row(
                                                    controls=[
                                                        Text(
                                                            value="Hello,",
                                                            size=30,
                                                            color='#5a5c69',
                                                            weight=FontWeight.W_300

                                                        ),
                                                        Text(
                                                            value=self.current_user_name,
                                                            size=30,
                                                            color='#5a5c69',
                                                            weight=FontWeight.W_700,


                                                        )
                                                    ]
                                                ),
                                                Container(
                                                    border_radius=5,
                                                    bgcolor=blue,
                                                    height=30,
                                                    width=120,
                                                    content=Text(
                                                        value="Generate Report",
                                                        size=14,
                                                        color='white'
                                                    ),
                                                    alignment=alignment.center
                                                )
                                            ]
                                        )
                                    ),

                                    Container(
                                        padding=20,
                                        content=GridView(
                                            max_extent=400,
                                            child_aspect_ratio=4,
                                            spacing=20,
                                            run_spacing=20,
                                            expand=1,
                                            controls=[

                                                Container(
                                                    padding=30,
                                                    alignment=alignment.center,
                                                    bgcolor='white',
                                                    shadow=BoxShadow(
                                                        # spread_radius=1,
                                                        blur_radius=20,
                                                        color='#1a000000'
                                                    ),
                                                    border=border.only(
                                                        left=border.BorderSide(5, color='green')),
                                                    content=Row(
                                                        alignment='spaceBetween',
                                                        vertical_alignment='center',
                                                        controls=[
                                                            Column(
                                                                spacing=0,
                                                                alignment='center',
                                                                controls=[
                                                                    Text(
                                                                        value="Monthly Earnings",
                                                                        color=blue,
                                                                    ),
                                                                    Text(
                                                                        value="$45,000",
                                                                        color=db_text,
                                                                        size=25,
                                                                        weight=FontWeight.W_600
                                                                    )
                                                                ]
                                                            ),
                                                            Icon(
                                                                icons.MONEY,
                                                                color='#dddfeb'
                                                            )
                                                        ]
                                                    )

                                                ),
                                                Container(
                                                    padding=30,
                                                    alignment=alignment.center,
                                                    bgcolor='white',
                                                    shadow=BoxShadow(
                                                        # spread_radius=1,
                                                        blur_radius=20,
                                                        color='#1a000000'
                                                    ),
                                                    border=border.only(
                                                        left=border.BorderSide(5, color='blue')),
                                                    content=Row(
                                                        alignment='spaceBetween',
                                                        vertical_alignment='center',
                                                        controls=[
                                                            Column(
                                                                spacing=0,
                                                                alignment='center',
                                                                # horizontal_alignment='center',
                                                                controls=[
                                                                    Text(
                                                                        value="Monthly Spendings",
                                                                        color=blue,
                                                                    ),
                                                                    Text(
                                                                        value="$20,000",
                                                                        color=db_text,
                                                                        size=25,
                                                                        weight=FontWeight.W_600
                                                                    )
                                                                ]
                                                            ),
                                                            Icon(
                                                                icons.MONEY_SHARP,
                                                                color='#dddfeb'
                                                            )
                                                        ]
                                                    )

                                                ),
                                                Container(
                                                    padding=30,
                                                    alignment=alignment.center,
                                                    bgcolor='white',
                                                    shadow=BoxShadow(
                                                        # spread_radius=1,
                                                        blur_radius=20,
                                                        color='#1a000000'
                                                    ),
                                                    border=border.only(
                                                        left=border.BorderSide(5, color='yellow')),
                                                    content=Row(
                                                        alignment='spaceBetween',
                                                        vertical_alignment='center',
                                                        controls=[
                                                            Column(
                                                                spacing=0,
                                                                alignment='center',
                                                                # horizontal_alignment='center',
                                                                controls=[
                                                                    Text(
                                                                        value="Yearly Earnings",
                                                                        color=blue,
                                                                    ),
                                                                    Text(
                                                                        value="$4,050,000",
                                                                        color=db_text,
                                                                        size=25,
                                                                        weight=FontWeight.W_600
                                                                    )
                                                                ]
                                                            ),
                                                            Icon(
                                                                icons.PRICE_CHANGE,
                                                                color='#dddfeb'
                                                            )
                                                        ]
                                                    )

                                                ),
                                                Container(
                                                    padding=30,
                                                    alignment=alignment.center,
                                                    bgcolor='white',
                                                    shadow=BoxShadow(
                                                        # spread_radius=1,
                                                        blur_radius=20,
                                                        color='#1a000000'
                                                    ),
                                                    border=border.only(
                                                        left=border.BorderSide(5, color='red')),
                                                    content=Row(
                                                        alignment='spaceBetween',
                                                        vertical_alignment='center',
                                                        controls=[
                                                            Column(
                                                                spacing=0,
                                                                alignment='center',
                                                                # horizontal_alignment='center',
                                                                controls=[
                                                                    Text(
                                                                        value="Yearly Spendings",
                                                                        color=blue,
                                                                    ),
                                                                    Text(
                                                                        value="$500,000",
                                                                        color=db_text,
                                                                        size=25,
                                                                        weight=FontWeight.W_600
                                                                    )
                                                                ]
                                                            ),
                                                            Icon(
                                                                icons.PRICE_CHECK,
                                                                color='#dddfeb'
                                                            )
                                                        ]
                                                    )

                                                ),

                                            ]
                                        )
                                    ),

                                    Container(
                                        shadow=BoxShadow(
                                            spread_radius=0,
                                            color='#1A000000',
                                            blur_radius=20,
                                        ),
                                        border_radius=10,
                                        clip_behavior=ClipBehavior.ANTI_ALIAS,
                                        padding=padding.only(
                                            left=20, right=20),
                                        content=Column(
                                            spacing=0,
                                            # alignment='center',
                                            controls=[
                                                Container(
                                                    height=30,
                                                    bgcolor='#f8f9fc',
                                                    border=border.only(bottom=border.BorderSide(
                                                        width=2, color='#662a334d',))
                                                ),
                                                Container(
                                                    content=PlotlyChart(
                                                        fig,
                                                        expand=True,
                                                    )
                                                )
                                            ]
                                        )
                                    ),

                                ]
                            )
                        ]
                    )
                ),


            ]
        )

    def get_fig(self):
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        spendings = [random.randint(100, 1000) for _ in range(len(months))]
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=months,
            y=spendings,
            mode='lines+markers',
            line=dict(shape='spline', width=5,
                      color='rgba(78, 115, 223, 0.5)'),
            fill='tozeroy',
            fillcolor="rgba(78, 115, 223, 0.3)",
            marker=dict(size=9, color='rgba(78, 115, 223, 1)',
                        line=dict(width=1, color='rgba(78, 115, 223, 1)')),
            hovertemplate="""<b>%{x}</b><br>
        <span>Spendings: %{y}</span>"""

        ))
        fig.update_xaxes(showgrid=False, gridwidth=0.1, gridcolor='LightPink')

        fig.update_layout(
            title='Monthly Expenses',
            xaxis_title='Month',
            yaxis_title='Spending ($)',
            showlegend=False,
            # plot_bgcolor='rgba(0,0,0,0)',
            # paper_bgcolor='rgba(0,0,0,0)',
            # grid=dict(type='dot')
        )
        return fig
