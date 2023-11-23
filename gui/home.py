import flet as ft


def IndexView(page: ft.Page, params, basket):
    def go_to_control(e, label):
        page.current_barrier = label
        page.go("/street")

    return ft.View(
        "/",
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
                                        'Избранное',
                                        color='black',
                                        weight=ft.FontWeight.BOLD,
                                        size=25,
                                    ),
                                    ft.Container(width=140, height=0),
                                    ft.IconButton(
                                        ft.icons.ARROW_BACK_IOS,
                                        icon_color='black',
                                        on_click=lambda e: page.go('/reg')
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
                                            ft.Text(f'Улица A', size=20)
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                    ),
                                    bgcolor='#99118c8b',
                                    opacity=1,
                                    alignment=ft.alignment.center,
                                    on_click=lambda e: go_to_control(e, 'A'),
                                    border=ft.border.all(2, '#00695C')
                                ),
                                ft.Container(
                                    width=175,
                                    height=175,
                                    border_radius=20,
                                    content=ft.Column(
                                        controls=[
                                            ft.Text(f'Улица B', size=20)
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                    ),
                                    bgcolor='#99118c8b',
                                    opacity=1,
                                    alignment=ft.alignment.center,
                                    on_click=lambda e: go_to_control(e, 'B'),
                                    border=ft.border.all(2, '#00695C')
                                ),

                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    width=175,
                                    height=40,
                                    border_radius=20,
                                    content=ft.Column(
                                        controls=[
                                            ft.IconButton(ft.icons.ADD, icon_color='white')
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                    ),
                                    bgcolor='#99118c8b',
                                    opacity  = 0 if i % 2 else 1,
                                    disabled = True if i % 2 else False,
                                    alignment=ft.alignment.center,
                                    border=ft.border.all(2, '#00695C')

                                ) for i in range(2)

                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),

                        # App bar
                        # ft.Container(
                        #     content=ft.Row(
                        #         controls=[
                        #             ft.IconButton(
                        #                 icon=ft.icons.MENU,
                        #             ),
                        #             ft.IconButton(
                        #                 icon=ft.icons.KEYBOARD_COMMAND_KEY,
                        #                 icon_size=50,
                        #                 icon_color='black',
                        #                 disabled=False,
                        #                 bgcolor='white'
                        #             ),
                        #
                        #             ft.IconButton(
                        #                 icon=ft.icons.SETTINGS,
                        #             )
                        #         ],
                        #         alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        #         vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        #         width=200,
                        #     ),
                        #
                        #     alignment=ft.alignment.bottom_center
                        # )
                    ]
                )
            )
        ],
        # controls = [
        #     # APP BAR
        #     # ft.AppBar(
        #     #     title=ft.Text("Умный Нижний"),
        #     # ),
        #
        #     ft.Container(
        #         content=ft.Text(
        #             'Умный Нижний',
        #             size=15,
        #             color='white'
        #         ),
        #         width=150,
        #         height=25,
        #         border_radius=20,
        #         bgcolor='#118c8b',
        #         alignment=ft.alignment.center
        #     ),
        #     # Stories
        #
        #
        #     # Card



    )
