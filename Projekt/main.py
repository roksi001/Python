from Projekt.app import AnimalSimulator
from ttkthemes import ThemedTk

if __name__ == "__main__":
    root = ThemedTk(theme="itft1")
    app = AnimalSimulator(root)
    root.mainloop()