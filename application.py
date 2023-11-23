import flet as ft
import flet_route
import gui
from gui import (
    home,
    register,
    street,
    barrier_control
)


def main(page: ft.Page):
    page.title = gui.NAME

    page.window_width     = gui.WIDTH
    page.window_height    = gui.HEIGHT
    page.window_resizable = False

    app_routes = [
        flet_route.path(
            url   = '/reg',
            clear = True,
            view  = register.IndexView
        ),
        flet_route.path(
            url   = '/',
            clear = True,
            view  = home.IndexView
        ),
        flet_route.path(
            url   = '/street',
            clear = True,
            view  = street.IndexView
        ),
        flet_route.path(
            url   = '/barrier_control',
            clear = True,
            view  = barrier_control.IndexView
        )
    ]

    flet_route.Routing(
        page = page,
        app_routes = app_routes
    )

    page.go('/')


ft.app(
    target     = main,
    name       = gui.NAME,
    view       = ft.AppView.FLET_APP,
    assets_dir = gui.ASSETS_DIR,
)
