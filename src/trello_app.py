import flet as ft
from flet import (
    Container,
    Icon,
    Page,
    Text,
    AppBar,
    PopupMenuButton,
    PopupMenuItem,
    colors,
    icons,
    margin
)

class TrelloApp(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.appbar_items = [
            ft.PopupMenuItem(text="Login"),
            ft.PopupMenuItem(),  # divider
            ft.PopupMenuItem(text="Settings")
        ]

        self.appbar = ft.AppBar(
            leading = ft.Icon(icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width = 100,
            title = ft.Text("Trolli", size=32, text_align="start"),
            center_title=False,
            toolbar_height = 75,
            bgcolor=ft.colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                ft.Container(
                    content=ft.PopupMenuButton(
                        items=self.appbar_items
                    ),
                    margin=margin.only(left=50, right=25)
                )
            ]
        ) 

        self.page.appbar = self.appbar
        self.page.update()