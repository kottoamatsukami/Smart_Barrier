import flet as ft


def IndexView(page: ft.Page, params, basket):
    return ft.View(
        "/barrier_control",
        controls=[
            ft.Container(
                expand=True,
                height=page.height,
                width=page.width,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=[
                        "#e0f2f1",
                        "#80CBC4",
                        "#26A69A",
                        "#004d40",
                    ],
                    tile_mode=ft.GradientTileMode.REPEATED,

                ),
                border_radius=15,
                content=ft.Column(
                    controls=[

                        # Appbar
                        ft.Divider(opacity=0),
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Container(width=10, height=0),
                                    ft.Text(
                                        f'Шлагбаум на: {page.current_barrier}',
                                        color='black',
                                        weight=ft.FontWeight.BOLD,
                                        size=25,
                                    ),
                                    ft.Container(width=80, height=0),
                                    ft.IconButton(
                                        ft.icons.ARROW_BACK_IOS,
                                        icon_color='black',
                                        on_click=lambda e: page.go('/street')
                                    ),
                                    ft.IconButton(
                                        ft.icons.SETTINGS,
                                        icon_color='black'
                                    ),

                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            width=page.width,
                            height=40,
                        ),
                        ft.Divider(),
                        # Stories
                        ft.Row(
                            controls=[
                                ft.Container(
                                    width=75,
                                    height=112,
                                    image_src=f"gui/assets/images/story{i}.jpg",
                                    image_fit=ft.ImageFit.FIT_HEIGHT,
                                    bgcolor='white',
                                    border_radius=15,
                                    border=ft.border.all(2, '#118c8b')
                                ) for i in range(1, 5)
                            ],
                            spacing=20,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        # Card
                        ft.Row(
                            controls=[
                                ft.Container(
                                    width=175,
                                    height=175,
                                    border_radius=20,
                                    content=ft.Column(
                                        controls=[
                                            ft.Text(f'Открыть', size=20)
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                    ),
                                    bgcolor='#99118c8b',
                                    alignment=ft.alignment.center,
                                    opacity=1,
                                    border=ft.border.all(2, '#00695C')
                                ),
                                ft.Container(
                                    width=175,
                                    height=175,
                                    border_radius=20,
                                    content=ft.Column(
                                        controls=[
                                            ft.Text(f'Закрыть', size=20)
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                    ),
                                    bgcolor='#99118c8b',
                                    alignment=ft.alignment.center,
                                    opacity=1,
                                    border=ft.border.all(2, '#00695C')
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    width=175,
                                    height=175,
                                    border_radius=20,
                                    content=ft.Column(
                                        controls=[
                                            ft.Text(f'Добавить номер', size=20)
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                    ),
                                    bgcolor='#99118c8b',
                                    alignment=ft.alignment.center,
                                    opacity=1,
                                    border=ft.border.all(2, '#00695C'),
                                ),
                                ft.Container(
                                    width=175,
                                    height=175,
                                    border_radius=20,
                                    content=ft.Column(
                                        controls=[
                                            ft.Text(f'Отчёт', size=20)
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                    ),
                                    bgcolor='#99118c8b',
                                    alignment=ft.alignment.center,
                                    opacity=1,
                                    border=ft.border.all(2, '#00695C')
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                    ]
                )
            )
        ],
    )
