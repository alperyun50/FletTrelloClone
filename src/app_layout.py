import flet as ft
from flet import (
    Control,
    Column,
    Container,
    IconButton,
    Page,
    Row,
    Text,
    IconButton,
    colors,
    icons,
)
import sidebar as sb



class AppLayout(ft.Row):
    def __init__(self, app, page: ft.Page, *args, **Kwargs):
        super().__init__(*args, **Kwargs)
        self.app = app
        self.page = page
        self.toogle_nav_rail_button = ft.IconButton(
            icon=icons.ARROW_CIRCLE_LEFT,
            selected=False,
            selected_icon=icons.ARROW_CIRCLE_RIGHT,
            on_click=self.toogle_nav_rail
        )
        self.sidebar = sb.SideBar(self, page)
        self._active_view: ft.Control = ft.Column(
            controls=[
                Text("Active View")
            ],
            alignment="center",
            horizontal_alignment="center"
        )
        self.controls = [
            self.sidebar, 
            self.toogle_nav_rail_button,
            self._active_view 
        ]

    @property
    def active_view(self):
        return self.active_view
    
    @active_view.setter
    def active_view(self, view):
        self.active_view = view
        self.update()

    def toggle_naw_rail(self, e):
        self.sidebar.visible = not self.sidebar.visible
        self.toggle_naw_rail_button.selected = not self.toogle_nav_rail_button.selected
        self.page.update()