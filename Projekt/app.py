import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.messagebox as messagebox
from Projekt import utils


class AnimalSimulator:
    """

    """
    def __init__(self, master):
        """
        Inicjalizuje symulator zwierzątka z podanym master widgetem.

        :param master: master widget
        """
        self.master = master
        self.master.title("Gra symulator zwierzątka")

        self.create_widgets()
        self.initialize_values()

    def create_widgets(self):
        """
        Tworzy widżety dla symulatora zwierzątka.
        """
        # Wybór postaci
        self.selection_frame = ttk.Frame(self.master)
        self.selection_frame.pack(pady=10)


        self.label = ttk.Label(self.selection_frame, text="Witaj w grze symulator zwierzątka, wybierz swoją postać", font=("Arial", 12,"bold"))
        self.label.pack()

        self.dog_button = ttk.Button(self.selection_frame, text="Pies", command=self.select_dog, width=10)
        self.dog_button.pack(side=tk.LEFT,padx=5)

        self.cat_button = ttk.Button(self.selection_frame, text="Kot", command=self.select_cat,width=10)
        self.cat_button.pack(side=tk.LEFT,padx=5)

        self.rabbit_button = ttk.Button(self.selection_frame, text="Królik", command=self.select_rabbit,width=10)
        self.rabbit_button.pack(side=tk.LEFT,padx=5)

        self.snake_button = ttk.Button(self.selection_frame, text="Wąż", command=self.select_snake,width=10)
        self.snake_button.pack(side=tk.LEFT,padx=5)

        # Nakarmienie zwierzątka
        self.feed_frame = ttk.Frame(self.master)
        self.feed_frame.pack(pady=10)

        self.feed_button = ttk.Button(self.feed_frame, text="Nakarm", command=self.feed_animal,width=10)
        self.feed_button.pack(side=tk.LEFT,padx=5)



        self.food_options = {
            "Wybierz": None,
            "Jabłko +10": 10,
            "Marchew +5": 5,
            "Woda +3": 3,
            "Arbuz +4": 4,
            "Burger +35": 35,
            "Chlebek +1": 1,
        }

        self.food_var = tk.StringVar(self.feed_frame)
        self.food_var.set("Wybierz")

        self.food_menu = ttk.OptionMenu(self.feed_frame, self.food_var, *self.food_options.keys())
        self.food_menu.pack(side=tk.LEFT,padx=5)



        # Zabawa ze zwierzątkiem
        self.play_frame = ttk.Frame(self.master)
        self.play_frame.pack(pady=10)

        self.play_button = ttk.Button(self.play_frame, text="Pobaw się", command=self.play_with_animal,width=10)
        self.play_button.pack(side=tk.LEFT,padx=5)

        self.play_options = {
            "Wybierz(każda zabawa zwiększa senność i głód o 5)": None,
            "Rzuć piłkę +5": 5,
            "Pogłaszcz +10": 10,
            "Aportuj +2": 2,
            "Turlaj się +4": 4,
            "Daj maskotkę +15": 15
        }

        self.play_var = tk.StringVar(self.play_frame)
        self.play_var.set("Wybierz")

        self.play_menu = ttk.OptionMenu(self.play_frame, self.play_var, *self.play_options.keys())
        self.play_menu.pack(side=tk.LEFT, padx=5)

        # Sen
        self.sleep_frame = ttk.Frame(self.master)
        self.sleep_frame.pack(pady=10)
        self.sleep_button = ttk.Button(self.sleep_frame, text="Prześpij się", command=self.sleep,width=10)
        self.sleep_button.pack()


        # Wyświetlanie wartości poziomów
        self.stats_frame = ttk.Frame(self.master)
        self.stats_frame.pack(pady=10)

        self.hunger_label = ttk.Label(self.stats_frame, text="Poziom najedzenia: 0", font=("Arial", 10))
        self.hunger_label.pack(side=tk.LEFT,padx=5)

        self.boredom_label = ttk.Label(self.stats_frame, text="Poziom nudy: 0", font=("Arial", 10))
        self.boredom_label.pack(side=tk.LEFT,padx=5)

        self.sleepiness_label = ttk.Label(self.stats_frame, text="Poziom senności: 0", font=("Arial", 10))
        self.sleepiness_label.pack(side=tk.LEFT,padx=5)

        # self.happiness_label = ttk.Label(self.stats_frame, text="Poziom radości: 0", font=("Arial", 10))
        # self.happiness_label.pack(side=tk.LEFT,padx=5)

        # Wyświetlanie postaci
        self.character_label = tk.Label(self.master)
        self.character_label.pack(pady=10)



    def initialize_values(self):
        """
        Inicjalizuje wartości początkowe dla symulatora zwierzątka.
        :return:
        """
        self.hunger = 50
        self.boredom = 0
        self.sleepiness = 0
        #self.happiness = 0
        self.is_selected=False
        self.sleep_frame.pack()
        self.update_values()

    def reset_values(self):
        """
        Ustawia wartości na początkowe przy zmianie zwierzęcia
        :return:
        """
        self.hunger = 50
        self.boredom = 0
        self.sleepiness = 0
        self.update_stats_labels()

    def select_dog(self):
        """
        Wybiera psa jako zwierzątko w symulatorze.
        """
        self.reset_values()
        self.is_selected = True
        self.character = ImageTk.PhotoImage(Image.open('../test_images/dog.png'))
        self.draw_character()


    def select_cat(self):
        """
        Wybiera kota jako zwierzątko w symulatorze.
        """
        self.reset_values()
        self.is_selected = True
        self.character = ImageTk.PhotoImage(Image.open('../test_images/cat.png'))
        self.draw_character()


    def select_rabbit(self):
        """
        Wybiera królika jako zwierzątko w symulatorze.
        """
        self.reset_values()
        self.is_selected = True
        self.character = ImageTk.PhotoImage(Image.open('../test_images/rabbit.png'))
        self.draw_character()


    def select_snake(self):
        """
        Wybiera węża jako zwierzątko w symulatorze.
        """
        self.reset_values()
        self.is_selected = True
        self.character = ImageTk.PhotoImage(Image.open('../test_images/snake.png'))
        self.draw_character()



    def feed_animal(self):
        """
        Karmi zwierzątko wybranym jedzeniem
        """
        selected_food = self.food_var.get()
        food_points = self.food_options[selected_food]
        self.hunger += food_points

        if self.hunger > 100:  # zabezpieczenie aby poziom nie przekraczał 100
            self.feed_button.config(state='disabled')
            messagebox.showinfo("Informacja", "Zwierzątko jest pełne jedzenia, poczekaj aż zgłodnieje :)")
        self.update_stats_labels()


    def play_with_animal(self):
        """
        Bawi się z zwierzątkiem wybraną zabawą oraz zwiększa sen i głód
        """
        if self.hunger >= 1 and self.sleepiness <= 99:
            selected_play = self.play_var.get()
            play_points = self.play_options[selected_play]
            self.boredom -= play_points

            self.sleepiness+=5
            self.hunger-=5

            self.update_stats_labels()
            self.play_button.config(state='normal')
            self.sleep_button.config(state='disabled')
            self.feed_button.config(state='normal')


    def draw_character(self):
        """
        Wyświetla wybraną postać zwierzątka
        """
        self.character_label.config(image=self.character)

    def sleep(self):
        """
        Powoduje, że zwierzątko idzie spać, resetując jego poziom snu do 0.
        """
        self.sleepiness = 0  # Gdy zwierzak się przespi, jego poziom snu wraca do 0
        self.feed_button.config(state='normal')
        self.play_button.config(state='normal')
        self.sleep_button.config(state='disabled')
        self.update_stats_labels()

    def update_values(self):
        """
        Aktualizuje wartości symulatora zwierzątka, zwiększając nudę, senność i zmniejszając najedzenie.
        """

        utils.update_values(self) # Wywołanie funkcji z utils

    def update_stats_labels(self):
        """
        Aktualizuje etykiety statystyk, aby odzwierciedlić obecne wartości.
        """
        utils.update_stats_labels(self) # Wywołanie funkcji z utils