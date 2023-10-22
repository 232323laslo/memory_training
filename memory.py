import random
import tkinter as tk

class Memory:
    def __init__(self):
        self.window = tk.Tk()
        # self.window.geometry("600x700")

        self.window.title("Memory Training")
        
        #Field for entering the size of the matrix
        self.size_entry = tk.Entry(self.window)
        self.size_entry.pack()

        self.generate_button = tk.Button(self.window, text="Generate", command=lambda: self.generate_matrix(int(self.size_entry.get())))
        self.generate_button.pack()


        self.matrix_label = tk.Label(self.window)
        self.matrix_label.pack()

    def generate_matrix(self, size):
        
        # Generate the matrix
        matrix = [[random.randint(1, 23) for _ in range(size)] for _ in range(size)]

        # Create matrix components
        self.labels = []
        for row in matrix:
            for number in row:
                label = tk.Label(self.matrix_label, text=str(number))
                label.config(background="black", font=("Arial", 30), width=4, height=4, relief="raised", anchor="center")
                label.config(borderwidth=2, highlightthickness=2, highlightcolor="black")
                self.labels.append(label)

        # Place the components of the matrix in the cells
        for row in range(size):
            for column in range(size):
                self.labels[row * size + column].grid(row=row, column=column)

        # Set the size of the window
        self.window.geometry(f"{size * 150}x{size * 180}")

    def mainloop(self):
        self.window.mainloop()


if __name__ == "__main__":
    memory = Memory()

    memory.mainloop()
