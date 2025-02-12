import flet as ft
import trello_app as t_a
import app_layout as a_l


def main(page: ft.Page):
    page.title = "Flet Trello Clone"
    page.padding = 0
    page.bgcolor = ft.colors.BLUE_GREY_200
    app = t_a.TrelloApp(page)
    page.add(app)
    page.update()


if __name__ == "__main__":
    ft.app(main)
