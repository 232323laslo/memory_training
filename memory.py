import random
import tkinter as tk

class Memory_game:  
    def __init__(self):
        #Saved numbers who need to remember
        self.numbers = []

        #Titles, sizes window, text
        self.window = tk.Tk()
        self.window.geometry("600x250")
        self.window.title("Memory Training")
        self.label = tk.Label(self.window, text="Use your brains, use your memory!", font=("Arial", 18))
        self.label.pack(padx=20, pady=20)

        #Buttons
        self.button_easy = tk.Button(self.window, text="Easy", command=lambda: self.generate_first_matrix(2, change_label=True))        
        self.button_normal = tk.Button(self.window, text="Normal", command=lambda: self.generate_first_matrix(4, change_label=True))        
        self.button_hard = tk.Button(self.window, text="Hard", command=lambda: self.generate_first_matrix(6, change_label=True)) 
        self.button_easy.pack()
        self.button_normal.pack()
        self.button_hard.pack()

        #Matrix
        self.matrix_label = tk.Label(self.window)
        self.matrix_label.pack()

        #Label for the timer at the main screen
        self.timer_label = tk.Label(self.window, text="05:00", font=("Arial", 20))
        self.timer_label.pack(side="top")

    def generate_first_matrix(self, size, change_label=False):
        #Generate the random numbers in matrix
        self.size = size
        matrix = [[random.randint(1, 23) for _ in range(size)] for _ in range(size)]

        #Create visual matrix components
        self.labels = []
        for row in matrix:
            for number in row:
                label = tk.Label(self.matrix_label, text=str(number))
                label.config(background="black", font=("Arial", 30), width=4, height=4, relief="raised", anchor="center")
                label.config(borderwidth=2, highlightthickness=2, highlightcolor="black")
                self.labels.append(label)

        #Place the components (numbers) of the matrix in the cells
        for row in range(size):
            for column in range(size):
                self.labels[row * size + column].grid(row=row, column=column)

        #Sets the size of the window depending on the size of the matrix 
        self.window.geometry(f"{size * 160}x{size * 230}")

        #Removed buttons after user choose level
        self.button_easy.destroy()
        self.button_normal.destroy()
        self.button_hard.destroy()
        
        #Set the new label text
        if change_label:
            self.label.config(text="Remember as much as possible!")

        #Start the timer
        self.timer_count = 2
        self.update_timer()

        #Adds all numbers to a list of numbers to compare results in the future
        for row in matrix:
            for number in row:
                self.numbers.append(number)
                
    def update_timer(self):
        #Decrement the timer count
        self.timer_count -= 1

        #Timer label
        self.timer_label.config(text=f"{self.timer_count // 60:02d}:{self.timer_count % 60:02d}")

        #If the timer has expired, go to next level
        if self.timer_count == 0:
            self.next_level()
            return

        #Schedule the next timer update
        self.timer_update_id = self.window.after(1000, self.update_timer)

    def next_level(self):
        #Printed all numbers in terminal
        for number in self.numbers:
            print(number)

        #Remove all labels (numbers) from the matrix
        for label in self.labels:
            label.destroy()

        #Generate a new matrix without numbers
        matrix = [[self.numbers[row * self.size + column] for column in range(self.size)] for row in range(self.size)]

        #Create new labels (blocks) for the matrix
        self.labels = []
        for row in matrix:
            for number in row:
                label = tk.Label(self.matrix_label)
                label.config(background="black", font=("Arial", 30), width=4, height=4, relief="raised", anchor="center")
                label.config(borderwidth=2, highlightthickness=2, highlightcolor="black")
                self.labels.append(label)   

        #Place the components (blocks)of the matrix in the cells
        for row in range(self.size):
            for column in range(self.size):
                self.labels[row * self.size + column].grid(row=row, column=column)  

        button_check_answers = tk.Button(self.window, text="Check Answers", command=self.on_click)
        button_check_answers.pack(padx=2, pady=2)

        for label in self.labels:
            label.bind("<Button-1>", lambda event: self.on_click(event))
            

    def on_click(self, event=None):
        if event is None:
            return
        clicked_label = event.widget
        # Get the width of the label
        label_size = clicked_label.winfo_width()
        # Create a text entry widget
        text_entry = tk.Entry(clicked_label)
        # Set the text entry widget's width to 4 characters
        text_entry.config(width=4)
        # Set the text entry widget's position
        text_entry.place(x=label_size / 6.5 - text_entry.winfo_width() / 2, y=label_size / 1.5 - text_entry.winfo_height() / 2)
        # Get the user's input
        new_number = text_entry.get()
        # If the user enters a valid number, set the label's text to the new number
        if new_number.isdigit() and 0 <= int(new_number) <= 23:
            clicked_label.config(text=new_number)
            if all([label.config() for label in self.labels]):
                # Compare the user's input to the correct answers
                correct_answers = self.numbers
                user_answers = [int(label.config()[0]) for label in self.labels]
                correct_count = 0
                for i in range(len(correct_answers)):
                    if user_answers[i] == correct_answers[i]:
                        correct_count += 1
                percentage_correct = correct_count / len(correct_answers) * 100

                # Print the percentage of correct answers to the console
                print("You got {}% correct!".format(percentage_correct))











    def mainloop(self):
        #Start the main loop
        self.window.mainloop()
        

if __name__ == "__main__":
    memory = Memory_game()

    memory.mainloop()