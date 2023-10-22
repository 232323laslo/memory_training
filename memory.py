import random



class Memory:
    def generate_random_matrix(self, size):
        # Генерує рандомну матрицю розміром size
        return [[random.randint(1, 9) for _ in range(size)] for _ in range(size)]


    def print_matrix(self, matrix):
        # Виводить матрицю в термінал
        for row in matrix:
            print(" ".join(str(n) for n in row))


def main():
    # Створюємо об'єкт класу Memory
    memory = Memory()

    # Запитуємо розмір матриці у користувача
    size = int(input("Введіть розмір матриці: "))

    # Генеруємо матрицю
    matrix = memory.generate_random_matrix(size)

    # Виводимо матрицю
    memory.print_matrix(matrix)


if __name__ == "__main__":
    main()



