import flet as ft

def main(page: ft.Page):
    # Función para manejar la respuesta y mostrar la imagen si es correcta
    def check_answer(e):
        # Aquí defines la respuesta correcta
        correct_answer = "Python"
        if answer_field.value.strip().lower() == correct_answer.lower():
            # Si la respuesta es correcta, muestra la imagen
            result_image.visible = True
            page.update()
            dialog.open = False  # Cierra el cuadro de diálogo
            page.update()
        else:
            # Mensaje de error si la respuesta es incorrecta
            error_label.value = "Respuesta incorrecta. Intenta de nuevo."
            page.update()

    # Crear el cuadro de diálogo con la pregunta
    dialog = ft.AlertDialog(
        title=ft.Text("Pregunta"),
        content=ft.Column([
            ft.Text("¿Cuál es el lenguaje de programación que estás utilizando ahora?"),
            (answer_field := ft.TextField(hint_text="Escribe tu respuesta aquí")),
            (error_label := ft.Text("", color="red"))  # Para mostrar un mensaje de error
        ]),
        actions=[
            ft.TextButton("Responder", on_click=check_answer),
        ],
        actions_alignment="end",
    )

    # Imagen que se mostrará solo si la respuesta es correcta
    result_image = ft.Image(
        src="Python.png",  # URL o ruta de la imagen
        visible=False,  # La imagen está oculta inicialmente
        width=200,
        height=200,
    )

    # Botón para abrir el cuadro de diálogo
    question_button = ft.TextButton("Responder Pregunta", on_click=lambda e: open_dialog())

    # Función para abrir el cuadro de diálogo
    def open_dialog():
        dialog.open = True
        page.update()

    # Añadir los elementos a la página
    page.add(
        question_button,
        ft.Container(result_image, alignment=ft.alignment.center),  # Ubicación específica de la imagen
    )

    # Añadir el cuadro de diálogo al layout
    page.dialog = dialog

# Ejecutar la app en Flet
ft.app(target=main)
