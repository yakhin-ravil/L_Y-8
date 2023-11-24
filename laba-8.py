#Требуется для своего варианта второй части л.р. №6 (усложненной программы) или ее объектно-ориентированной реализации
# (л.р. №7) разработать реализацию с использованием графического интерфейса. Допускается использовать любую графическую
# библиотеку питона. Рекомендуется использовать внутреннюю библиотеку питона  tkinter.
# В программе должны быть реализованы минимум одно окно ввода, одно окно вывода, текстовое поле, кнопка.

import tkinter as tk
from tkinter import messagebox

class Philharmony:
    def __init__(self, instruments, instruments2, instruments3, instruments4):
        self.instruments = instruments
        self.instruments2 = instruments2
        self.instruments3 = instruments3
        self.instruments4 = instruments4
    
    # Перебираем методом все возможные комбинации квартета из объектов
    def discover_best_quartet(self, number_musical_instruments):
        if number_musical_instruments == 1:
            best_quartet = None
            max_rating = 0
            for i in range(len(self.instruments)):
                for j in range(i + 1, len(self.instruments)):
                    for k in range(j + 1, len(self.instruments)):
                        for b in range(k + 1, len(self.instruments)):
                            quartet = [self.instruments[i], self.instruments[j], self.instruments[k], self.instruments[b]]
                            rate_sum = sum(instrument.rating for instrument in quartet)
                            if rate_sum > max_rating:
                                best_quartet = quartet
                                max_rating = rate_sum
                                
        elif number_musical_instruments == 2:
            best_quartet = None
            max_rating = 0
            for i in range(len(self.instruments2)):
                for j in range(i + 1, len(self.instruments2)):
                    for k in range(j + 1, len(self.instruments2)):
                        for b in range(k + 1, len(self.instruments2)):
                            quartet = [self.instruments2[i], self.instruments2[j], self.instruments2[k], self.instruments2[b]]
                            rate_sum = sum(instrument.rating for instrument in quartet)
                            if rate_sum > max_rating:
                                best_quartet = quartet
                                max_rating = rate_sum

        elif number_musical_instruments == 3:
            best_quartet = None
            max_rating = 0
            for i in range(len(self.instruments3)):
                for j in range(i + 1, len(self.instruments3)):
                    for k in range(j + 1, len(self.instruments3)):
                        for b in range(k + 1, len(self.instruments3)):
                            quartet = [self.instruments3[i], self.instruments3[j], self.instruments3[k], self.instruments3[b]]
                            rate_sum = sum(instrument.rating for instrument in quartet)
                            if rate_sum > max_rating:
                                best_quartet = quartet
                                max_rating = rate_sum

        elif number_musical_instruments == 4:
            best_quartet = None
            max_rating = 0
            for i in range(len(self.instruments4)):
                for j in range(i + 1, len(self.instruments4)):
                    for k in range(j + 1, len(self.instruments4)):
                        for b in range(k + 1, len(self.instruments4)):
                            quartet = [self.instruments4[i], self.instruments4[j], self.instruments4[k], self.instruments4[b]]
                            rate_sum = sum(instrument.rating for instrument in quartet)
                            if rate_sum > max_rating:
                                best_quartet = quartet
                                max_rating = rate_sum
      
        return best_quartet
    
# Класс для описания инструментов
class Instrument:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

# Задаем списки инструментов в филармонии
def create_philharmony():
    instruments = [Instrument("Скрипка", 1000), Instrument("Виолончель", 700),
                    Instrument("Альт", 1000), Instrument("Комуз", 400), Instrument("Арфа", 1400),
                    Instrument("Гитара", 900), Instrument("Кыяк", 100), Instrument("Хомус", 100),
                   Instrument("Кобыз", 150), Instrument("Балалайка", 800), Instrument("Контрабас", 500),
                   Instrument("Домбыра", 3), Instrument("Гусли", 2)]
    
    instruments2 = [Instrument("Флейта", 200), Instrument("Гобой", 300),
                    Instrument("Кларнет", 900), Instrument("Фагот", 430), Instrument("Саксофон", 600),
                    Instrument("Блокфлейта", 340), Instrument("Шалмей", 200), Instrument("Шалюмо", 100),
                   Instrument("Балабан", 800), Instrument("Дудук", 500), Instrument("Жалейка", 1800),
                   Instrument("Свирель", 3), Instrument("Зурна", 2)]
    
    instruments3 = [Instrument("Валторна", 900), Instrument("Труба", 800),
                    Instrument("Корнет", 2500), Instrument("Флюгельгорн", 1300), Instrument("Тромбон", 1400),
                    Instrument("Туба", 380), Instrument("Сакбут", 400), Instrument("Серпент", 230)]
    
    instruments4 = [Instrument("Барабаны", 900), Instrument("Тарелки", 800),
                    Instrument("Бубен", 2300), Instrument("Кастаньеты", 1300), Instrument("Треугольник", 1400),
                    Instrument("Ксилофон", 380), Instrument("Литавры", 400), Instrument("Колокольчики", 230), Instrument("Вибрафон", 230)]
    
    philharmony = Philharmony(instruments, instruments2, instruments3, instruments4)
    return philharmony

# Функция для вывода наилучшего квартета
def show_best_quartet():
    try:
        number_musical_instruments = int(entry.get())
        if number_musical_instruments < 1 or number_musical_instruments > 4: 
            messagebox.showerror("Ошибка", "Введите натуральное число больше 0, но меньше 5")
        philharmony = create_philharmony()
        best_quartet = philharmony.discover_best_quartet(number_musical_instruments)
    
        if best_quartet:
            results_window = tk.Tk() # Открытие окна с результатом
            results_window.title('Полученный результат')
            results_window['bg'] = '#DB8000'
            results_window.geometry('550x400')
            results_window.resizable(False, False)
            results_label = tk.Label(results_window, width=55, height=10, text="")
            results_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            results_label.config(font=('Helvetica',12))
        
            result_text = "Найден квартет с наибольшим рейтингом инструментов\n"
            for instrument in best_quartet:
                result_text +=f"Инструмент: {instrument.name}, Уровень навыка: {instrument.rating}\n"
            result_rating = sum(instrument.rating for instrument in best_quartet)
            result_text += f"\nОбщая стоимость: {result_rating}\n"
            results_label.config(text=result_text)
        
    except ValueError:
        messagebox.showerror("Ошибка", "Введите натуральное число!")

# Создание графического интерфейса
window = tk.Tk()
window.geometry('600x500')
window.title('Лабораторная работа №8')

label = tk.Label(window, text='\nВыберите тип инструментов:' '\n1 - струнные''\n2 - деревянные духовые''\n3 - медные духовые''\n4 - ударные\n')
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text='Найти лучший квартет',  width=25, height=3, command=show_best_quartet, bg = '#DB8000')
button.place(anchor=tk.CENTER)
button.pack()

result_label = tk.Label(window, text='')
result_label.pack()

window.mainloop()