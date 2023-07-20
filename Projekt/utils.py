from tkinter import messagebox


def update_stats_labels(self):
    """
    Aktualizuje liczby wyświetlane użytkownikowi
    :param self:
    :return:
    """
    self.hunger_label.config(text=f"Poziom najedzenia: {self.hunger}")
    self.boredom_label.config(text=f"Poziom nudy: {self.boredom}")
    self.sleepiness_label.config(text=f"Poziom senności: {self.sleepiness}")

def update_values(self):
    """
    Aktualizuje wartości symulatora zwierzątka co 2 sekundy, zwiększając poziom nudy, senności i zmniejszając najedzenia.
    :param self:
    :return:
    """
    if self.is_selected:
        self.boredom += 2
        self.sleepiness += 1
        self.hunger -= 1
        #self.happiness -= 1

        if self.sleepiness >= 100:
            messagebox.showinfo("Informacja", "Zwierzątko jest zmęczone, musi iść spać!")
            self.sleep_button.config(state='normal')
            self.feed_button.config(state='disabled')
            self.play_button.config(state='disabled')
        elif self.hunger <= 0:
            messagebox.showinfo("Informacja", "Zwierzątko jest głodne, nakarm je :(")
            self.feed_button.config(state='normal')
            self.play_button.config(state='disabled')
            self.sleep_button.config(state='disabled')
        elif self.boredom >= 100:
            messagebox.showinfo("Informacja", "Zwierzątko się nudzi, pobaw się z nim! :(")
            self.feed_button.config(state='disabled')
            self.play_button.config(state='normal')
            self.sleep_button.config(state='disabled')
        else:
            self.play_button.config(state='normal')

        self.update_stats_labels()

    self.master.after(2000, self.update_values)  # Wywołanie funkcji co 2 sekudny