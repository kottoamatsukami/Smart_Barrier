import flet as ft


def IndexView(page: ft.Page, params, basket):
    return ft.View(
        "/reg",
        controls=[
            ft.Container(
                image_src="gui/assets/images/summer.jpg",
                image_fit=ft.ImageFit.FIT_HEIGHT,
                expand=True,
                alignment=ft.alignment.center,
                width=page.width,
                height=page.height,
                border_radius=10,
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Divider(opacity=0, height=1),
                            ft.Text(
                                value="Умный Нижний",
                                size = 30,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.colors.BLACK

                            ),
                            ft.Text(
                                value="Регистрация",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.colors.BLACK
                            ),
                            ft.Container(
                                padding=10,
                                content = ft.Column(
                                    controls= [
                                        ft.TextField(
                                            label="Login"
                                        ),
                                        ft.TextField(
                                            label="Password",
                                            password=True,
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Text("Регистрация"),
                                                ft.Text("Соглашение пользователя"),
                                                ft.Text("Вопрос")
                                            ],
                                        )
                                    ],
                                ),
                            ),
                            ft.TextButton(
                                text="Войти",
                                style=ft.ButtonStyle(
                                    color='black',
                                    bgcolor='white',
                                    overlay_color='gray',
                                ),
                                on_click=lambda e: page.go("/"),
                                opacity=0.75
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=ft.colors.with_opacity(0.2, color=ft.colors.WHITE),
                    border_radius=15,
                    width=350,
                    height=450,
                    blur=20,
                    border=ft.border.all(1, '#000000')
                )
            )

        ]
    )
