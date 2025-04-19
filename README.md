<p align="center">
  <img width="200" height="200" src="images/icon.png" alt="DeNote Logo">
</p>

<h1 align="center" class="outfit-text">
  DeCalc
</h1>

Простой и красивый калькулятор, реализованный с использованием Python и [Flet](https://flet.dev/) — фреймворка для создания GUI-приложений.

<p align="center">
  <a style="text-decoration:none" href="https://github.com/DevNexe/DeCalc/releases">
    <img src="https://img.shields.io/github/release/DevNexe/DeCalc.svg?label=latest%20version" alt="Releases" />
  </a>
</p>

## 🖼️ Интерфейс
Современный пользовательский интерфейс, напоминающий стандартный калькулятор Windows. Приложение поддерживает базовые математические операции, обработку ошибок и ограничение размеров окна.

## 🚀 Возможности

- ➕ Сложение  
- ➖ Вычитание  
- ✖ Умножение  
- ➗ Деление  
- 🧮 Поддержка десятичных дробей  
- 🧾 История вычислений (заготовка)
- ⌫ Удаление последнего символа
- ♻ Сброс ввода  
- ➕/➖ Изменение знака  
- ⚠ Обработка деления на 0 и других ошибок

## 📦 Зависимости

- Python >=3.12
- [Flet](https://pypi.org/project/flet/)

Установить Flet:

```bash
pip install flet
```

## ▶ Запуск

Склонируй репозиторий и запусти:

```bash
python main.py
```
## 📸 Скриншот

![image](images/image.png)

## 🛠 Примечания

- Используется decimal.Decimal для точных вычислений.
- Интерфейс фиксированной ширины и высоты (328x430), не изменяется пользователем.
- Поддержка кнопок %, CE, √, 1/x, x² добавлена в интерфейс, но функциональность не реализована — ты можешь доработать.


