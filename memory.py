import random

class Memory:
    def generate_random_matrix(self, size):
        #Generates a random matrix of size
        return [[random.randint(1, 9) for _ in range(size)] for _ in range(size)]


    def print_matrix(self, matrix):
        #Outputs the matrix to the terminal
        for row in matrix:
            print(" ".join(str(n) for n in row))


def main():
    memory = Memory()

    #Ask the size of the matrix from the user
    size = int(input("Введіть розмір матриці: "))
    matrix = memory.generate_random_matrix(size)
    memory.print_matrix(matrix)


if __name__ == "__main__":
    main()



