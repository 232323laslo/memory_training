import random
import tkinter as tk

class Memory:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("600x700")
        self.window.title("Memory Training")
        self.label = tk.Label(self.window, text="Use your brains, use your memory!", font=("Arial", 18))
        self.label.pack(padx=20, pady=20)

        # Додаємо кнопки
        self.button_easy = tk.Button(self.window, text="Easy", command=lambda: self.generate_matrix(2, change_label=True)) 
        self.button_easy.pack()
        self.button_normal = tk.Button(self.window, text="Normal", command=lambda: self.generate_matrix(4, change_label=True)) 
        self.button_normal.pack()
        self.button_hard = tk.Button(self.window, text="Hard", command=lambda: self.generate_matrix(6, change_label=True)) 
        self.button_hard.pack()

        self.matrix_label = tk.Label(self.window)
        self.matrix_label.pack()

        # Label for the timer
        self.timer_label = tk.Label(self.window, text="05:00", font=("Arial", 20))
        self.timer_label.pack(side="top")

        # Список всіх label'ів з матриці
        self.numbers = []

    def generate_matrix(self, size, change_label=False):
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
        self.window.geometry(f"{size * 160}x{size * 200}")

        #Прибираємо кнопки
        self.button_easy.destroy()
        self.button_normal.destroy()
        self.button_hard.destroy()
        
        # Змінюємо текст label, якщо це необхідно
        if change_label:
            self.label.config(text="Remember as much as possible!")

       # Start the timer
        self.timer_count = 2
        self.update_timer()

        # Add all numbers to the numbers list
        for row in matrix:
            for number in row:
                self.numbers.append(number)

    def update_timer(self):
        # Decrement the timer count
        self.timer_count -= 1

        # Update the timer label
        self.timer_label.config(text=f"{self.timer_count // 60:02d}:{self.timer_count % 60:02d}")

        # If the timer has expired, end the game
        if self.timer_count == 0:
            # Stop the timer before returning
            self.window.after_cancel(self.timer_update_id)

            # End the game
            self.end_game()

            # Return control to the main loop
            return

        # Schedule the next timer update
        self.timer_update_id = self.window.after(1000, self.update_timer)

        return

    def end_game(self):
        # Print all the numbers
        for number in self.numbers:
            print(number)


    def mainloop(self):
        self.window.mainloop()


if __name__ == "__main__":
    memory = Memory()

    memory.mainloop()