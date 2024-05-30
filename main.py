import tkinter as tk
from tkinter import messagebox

# Функция для вычисления суммы цифр, кратных 3
def sum_digits_multiple_of_3(number, use_for_loop):
    sum_digits = 0
    if use_for_loop:
        for digit in str(number):
            if digit.isdigit() and int(digit) % 3 == 0:
                sum_digits += int(digit)
    else:
        i = 0
        while i < len(str(number)):
            digit = str(number)[i]
            if digit.isdigit() and int(digit) % 3 == 0:
                sum_digits += int(digit)
            i += 1
    return sum_digits

# Функция обработки нажатия на кнопку "Вычислить"
def calculate_sum():
    try:
        number = int(entry_number.get())
        use_for_loop = var.get() == 1
        result = sum_digits_multiple_of_3(number, use_for_loop)
        entry_result.config(state='normal')  # Разблокируем поле для записи
        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(result))
        entry_result.config(state='readonly')  # Заблокируем поле для редактирования
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное целое число")

# Функция обработки нажатия на кнопку "Очистить"
def clear_fields():
    entry_number.delete(0, tk.END)
    entry_result.config(state='normal')
    entry_result.delete(0, tk.END)
    entry_result.config(state='readonly')

# Создание основного окна приложения
root = tk.Tk()
root.title("Работа с виджетом Radiobutton")

# Виджеты для выбора типа цикла
tk.Label(root, text="Выберите цикл:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
var = tk.IntVar(value=1)  # Установка значения по умолчанию
tk.Radiobutton(root, text="for", variable=var, value=1).grid(row=1, column=0, padx=20, sticky='w')
tk.Radiobutton(root, text="while", variable=var, value=2).grid(row=2, column=0, padx=20, sticky='w')

# Виджет ввода числа
tk.Label(root, text="Введите целое число:").grid(row=3, column=0, padx=10, pady=5, sticky='w')
entry_number = tk.Entry(root)
entry_number.grid(row=3, column=1, padx=10, pady=5)

# Поле для отображения результата
tk.Label(root, text="Сумма цифр кратных 3:").grid(row=4, column=0, padx=10, pady=5, sticky='w')
entry_result = tk.Entry(root, state='readonly')
entry_result.grid(row=4, column=1, padx=10, pady=5)

# Кнопка для запуска вычислений
button_calculate = tk.Button(root, text="Вычислить", command=calculate_sum)
button_calculate.grid(row=5, column=0, padx=10, pady=20)

# Кнопка для очистки полей
button_clear = tk.Button(root, text="Очистить", command=clear_fields)
button_clear.grid(row=5, column=1, padx=10, pady=20)

# Запуск основного цикла приложения
root.mainloop()
