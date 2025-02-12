import flet as ft
import trello_app as trl


def main(page: ft.Page):
    page.title = "Flet Trello Clone"
    page.padding = 0
    page.bgcolor = ft.colors.BLUE_GREY_200
    app = trl.TrelloApp(page)
    page.add(app)
    page.update()


if __name__ == "__main__":
    ft.app(main)
