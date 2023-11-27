#Требуется для своего варианта второй части л.р. №6 (усложненной программы) или ее объектно-ориентированной реализации
# (л.р. №7) разработать реализацию с использованием графического интерфейса. Допускается использовать любую графическую
# библиотеку питона. Рекомендуется использовать внутреннюю библиотеку питона  tkinter.
# В программе должны быть реализованы минимум одно окно ввода, одно окно вывода, текстовое поле, кнопка.

import tkinter as tk

class Philharmony:
    def __init__(self, instruments):
        self.instruments = instruments

    # Перебираем методом все возможные комбинации квартета
    def discover_best_quartet(self):
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
        return best_quartet

# Класс для описания инструментов
class Instrument:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

def display_best_quartet_info(number_musical_instruments):
    quartet = None
    # Создаем экземпляры квартетов для каждой группы инструментов
    if number_musical_instruments == 1:
        quartet = Philharmony(instruments_stringed)
    elif number_musical_instruments == 2:
        quartet = Philharmony(instruments_wooden)
    elif number_musical_instruments == 3:
        quartet = Philharmony(instruments_brass)
    elif number_musical_instruments == 4:
        quartet = Philharmony(instruments_percussion)

    if quartet:
        best_quartet = quartet.discover_best_quartet()
        result_rating = sum(instrument.rating for instrument in best_quartet)
        return [(f"Инструмент - {instrument.name}, Рейтинг: {instrument.rating}") for instrument in best_quartet], result_rating
    else:
        return [], 0

# Создаем объекты инструментов
instruments_stringed = [Instrument("Скрипка", 1000), Instrument("Виолончель", 700),
                    Instrument("Альт", 1000), Instrument("Комуз", 400), Instrument("Арфа", 1400),
                    Instrument("Гитара", 900), Instrument("Кыяк", 100), Instrument("Хомус", 100),
                   Instrument("Кобыз", 150), Instrument("Балалайка", 800), Instrument("Контрабас", 500),
                   Instrument("Домбыра", 3), Instrument("Гусли", 2)]
instruments_wooden = [Instrument("Флейта", 200), Instrument("Гобой", 300),
                    Instrument("Кларнет", 900), Instrument("Фагот", 430), Instrument("Саксофон", 600),
                    Instrument("Блокфлейта", 340), Instrument("Шалмей", 200), Instrument("Шалюмо", 100),
                   Instrument("Балабан", 800), Instrument("Дудук", 500), Instrument("Жалейка", 1800),
                   Instrument("Свирель", 3), Instrument("Зурна", 2)]
instruments_brass = [Instrument("Валторна", 900), Instrument("Труба", 800),
                    Instrument("Корнет", 2500), Instrument("Флюгельгорн", 1300), Instrument("Тромбон", 1400),
                    Instrument("Туба", 380), Instrument("Сакбут", 400), Instrument("Серпент", 230)]
instruments_percussion = [Instrument("Барабаны", 900), Instrument("Тарелки", 800),
                    Instrument("Бубен", 2300), Instrument("Кастаньеты", 1300), Instrument("Треугольник", 1400),
                    Instrument("Ксилофон", 380), Instrument("Литавры", 400), Instrument("Колокольчики", 230), Instrument("Вибрафон", 230)]

# Функция для вывода результата
def show_best_quartet():
    number_musical_instruments = int(selected_instrument.get())
    result, rating = display_best_quartet_info(number_musical_instruments)
    result_window = tk.Toplevel(root)
    result_window.geometry("300x200")
    result_window.title("Результат")
    result_label = tk.Label(result_window, text='\n'.join(result))
    result_label.pack()
    rating_label = tk.Label(result_window, wraplength=200, font=('Helvetica', 12), text=f"Общая сумма рейтинга квартета: {rating}")
    rating_label.pack()
    root.withdraw()
    result_window.protocol("WM_DELETE_WINDOW", root.destroy)  # устанавливаем действие при закрытии окна

# Создание графического интерфейса
root = tk.Tk()
root.title("Philharmony")
root.geometry('500x400')

# Выбор типа инструментов
label_choose = tk.Label(root, height=8, text="Уважаемый пользователь! Выберите тип инструментов, в котором вы хотите подобрать квартет с наивысшим рейтингом:", wraplength=300, font=('Helvetica', 14))
label_choose.pack()

selected_instrument = tk.StringVar()
selected_instrument.set("1")  # По умолчанию первый инструмент

radio1 = tk.Radiobutton(root, text="Струнные", variable=selected_instrument, value="1", font=('Helvetica', 10))
radio1.pack()
radio2 = tk.Radiobutton(root, text="Деревянные духовые", variable=selected_instrument, value="2", font=('Helvetica', 10))
radio2.pack()
radio3 = tk.Radiobutton(root, text="Медные духовые", variable=selected_instrument, value="3", font=('Helvetica', 10))
radio3.pack()
radio4 = tk.Radiobutton(root, text="Ударные", variable=selected_instrument, value="4", font=('Helvetica', 10))
radio4.pack()

# Кнопка для поиска квартета
search_button = tk.Button(root, font=('Helvetica', 10), width=40, height=2, bg="#87DFD6", text="Найти квартет c наивысшим рейтингом", command=show_best_quartet)
search_button.pack(pady=10)

root.mainloop()