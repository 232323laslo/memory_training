import random
import tkinter as tk

class Memory:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("600x700")
        self.window.title("Memory Training")
        
        #Field for entering the size of the matrix
        self.size_entry = tk.Entry(self.window)
        self.size_entry.pack()

        #Generate button
        self.generate_button = tk.Button(self.window, text="Generate", command=lambda: self.generate_matrix(int(self.size_entry.get())))
        self.generate_button.pack()


        self.matrix_label = tk.Label(self.window)
        self.matrix_label.pack()


        # Label for the timer
        self.timer_label = tk.Label(self.window, text="05:00", font=("Arial", 20))
        self.timer_label.pack(side="top")

    def generate_matrix(self, size):
        #Generate the matrix
        matrix = [[random.randint(1, 23) for _ in range(size)] for _ in range(size)]

        #Create matrix components
        self.labels = []
        for row in matrix:
            for number in row:
                label = tk.Label(self.matrix_label, text=str(number))
                label.config(background="black", font=("Arial", 30), width=4, height=4, relief="raised", anchor="center")
                label.config(borderwidth=2, highlightthickness=2, highlightcolor="black")
                self.labels.append(label)

        #Place the components of the matrix in the cells
        for row in range(size):
            for column in range(size):
                self.labels[row * size + column].grid(row=row, column=column)

        #Set the size of the window
        self.window.geometry(f"{size * 150}x{size * 180}")

        #Start the timer
        self.timer_count = 300
        self.update_timer()

    def update_timer(self):
        #Decrement the timer count
        self.timer_count -= 1

        #Update the timer label
        self.timer_label.config(text=f"{self.timer_count // 60:02d}:{self.timer_count % 60:02d}")

        #If the timer has expired, end the game
        if self.timer_count == 0:
            self.end_game()

        #Schedule the next timer update
        self.window.after(1000, self.update_timer)

    def mainloop(self):
        self.window.mainloop()


if __name__ == "__main__":
    memory = Memory()

    memory.mainloop()
