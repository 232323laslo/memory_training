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

        # Create matrix components
        self.labels = []
        for row in matrix:
            for number in row:
                label = tk.Label(self.matrix_label, text=str(number))
                self.labels.append(label)

        #Palace the components of the matrix in the cells
        for row in range(size):
            for column in range(size):
                self.labels[row * size + column].grid(row=row, column=column)

        #Conf matrix components
        for label in self.labels:
            label.config(background="black", width=9, height=9, relief="raised")
            label.config(borderwidth=2, highlightthickness=2, highlightcolor="black")

    def mainloop(self):
        self.window.mainloop()


if __name__ == "__main__":
    memory = Memory()

    memory.mainloop()
