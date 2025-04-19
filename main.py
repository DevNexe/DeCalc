import flet as ft
from decimal import Decimal, getcontext, DivisionByZero

getcontext().prec = 28

def main(page: ft.Page):
    page.title = "Калькулятор"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.window.width = 328
    page.window.height = 430
    page.window.resizable = False
    page.padding = 10

    current_input = []
    history_entries = []

    display = ft.TextField(
        value="",
        text_align="right",
        read_only=True,
        width=292,
        height=80,
        border_radius=10,
        text_size=30,
    )

    def format_decimal(val: Decimal) -> str:
        s = format(val, 'f')
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return s if s else '0'

    def calculate_expression(expr):
        try:
            expr = ''.join(expr)
            while expr and expr[-1] in '+-*/':
                expr = expr[:-1]
            if not expr:
                return "Ошибка"

            tokens = []
            num = ''
            for char in expr:
                if char in '0123456789.':
                    num += char
                else:
                    if num:
                        tokens.append(Decimal(num))
                        num = ''
                    tokens.append(char)
            if num:
                tokens.append(Decimal(num))

            def apply_op(a, b, op):
                if op == '+': return a + b
                if op == '-': return a - b
                if op == '*': return a * b
                if op == '/':
                    if b == Decimal(0):
                        raise DivisionByZero
                    return a / b

            i = 0
            while i < len(tokens):
                if tokens[i] in ['*', '/']:
                    res = apply_op(tokens[i - 1], tokens[i + 1], tokens[i])
                    tokens[i - 1:i + 2] = [res]
                    i -= 1
                else:
                    i += 1

            i = 0
            while i < len(tokens):
                if tokens[i] in ['+', '-']:
                    res = apply_op(tokens[i - 1], tokens[i + 1], tokens[i])
                    tokens[i - 1:i + 2] = [res]
                    i -= 1
                else:
                    i += 1

            return format_decimal(tokens[0])
        except DivisionByZero:
            return "Деление на 0"
        except Exception:
            return "Ошибка"

    def button_click(e):
        text = e.control.text
        if text == "=":
            result = calculate_expression(current_input)
            expression = ''.join(current_input)
            display.value = result
            current_input.clear()
            if result not in ["Ошибка", "Деление на 0"]:
                current_input.append(result)
        elif text == "C":
            current_input.clear()
            display.value = ""
        elif text == "←":
            if current_input:
                current_input.pop()
                display.value = ''.join(current_input)
        elif text == "+/-":
            if current_input and current_input[-1].lstrip('-').replace('.', '').isdigit():
                last = current_input.pop()
                if last.startswith('-'):
                    current_input.append(last[1:])
                else:
                    current_input.append('-' + last)
                display.value = ''.join(current_input)
        else:
            current_input.append(text)
            display.value = ''.join(current_input)
        page.update()

    def toggle_history(e):
        scroll_view.visible = not scroll_view.visible
        page.update()

    def create_button(text, width=60):
        return ft.ElevatedButton(
            text=text,
            width=width,
            height=45,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=6)),
            on_click=button_click
        )

    layout = [
        ft.Row([create_button(text, width=70) for text in row], spacing=4)
        for row in [
            ["%", "CE", "C", "←"],
            ["1/x", "x²", "√", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["+/-", "0", ".", "="],
        ]
    ]

    # Добавляем scroll_view в основную колонку
    page.add(
        ft.Stack(
            controls=[
                ft.Column([
                    ft.Row([display], alignment=ft.MainAxisAlignment.END),
                    *layout
                ], spacing=4),
            ]
        )
    )

ft.app(target=main)
