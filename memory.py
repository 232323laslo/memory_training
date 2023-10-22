import random
import tkinter as tk

class Memory:
    def __init__(self):
        self.window = tk.Tk()

        self.window.title("Memory Training")
        
        #Field for entering the size of the matrix
        self.size_entry = tk.Entry(self.window)
        self.size_entry.pack()

        self.generate_button = tk.Button(self.window, text="Generate", command=lambda: self.generate_matrix(int(self.size_entry.get())))
        self.generate_button.pack()


        self.matrix_label = tk.Label(self.window)
        self.matrix_label.pack()

    def generate_matrix(self, size):
        matrix = [[random.randint(1, 23) for _ in range(size)] for _ in range(size)]

        self.matrix_label.config(text="\n".join([" ".join([str(n) for n in row]) for row in matrix]))

    def mainloop(self):
        self.window.mainloop()


if __name__ == "__main__":
    memory = Memory()

    memory.mainloop()
