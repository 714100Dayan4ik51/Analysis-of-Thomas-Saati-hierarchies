def calculateWeights(matrix):
    n = len(matrix)
    weights = [0] * n

    sums = [0] * n  # вычисление суммы для каждого столбца
    for j in range(n):
        sum = 0.0
        for i in range(n):
            sum += matrix[i][j]  # вычисляем сумму для каждого столбца
        sums[j] = sum

    # вычисление весовых коэффициентов
    for i in range(n):
        sum = 0.0
        for j in range(n):
            sum += matrix[i][j] / sums[j]  # вычисляем весовые коэффициенты, деля каждый элемент на сумму столбца
        weights[i] = sum / n

    return weights


if __name__ == "__main__":
    n = str(input("Введите количество критериев: "))
    # проверяем введенные данные на правильность
    if not n.isnumeric():
        print("Ошибка!")
        exit()  # если n не является числом, то программа завершается
    n = int(n)
    m = [[0.0] * n for _ in range(n)]  # создаем матрицу, заполненную нулями, размером n x n
    for i in range(n):
        for j in range(i, n):
            if i == j:
                m[i][j] = 1.0
            else:
                try:
                    m[i][j] = float(input(
                        f"Введите пару сравнения для критериев {i + 1} и {j + 1}: "))  # запрашиваем вес критериев и сохроняем в матрице
                except ValueError:
                    print("Ошибка!")
                    exit()  # если введенное значение не является числом, то программа завершается
                m[j][i] = 1.0 / m[i][j]
    weights = calculateWeights(m)
    # вывод данных
    print("Весовые коэффициенты:")
    for weight in weights:
        print(f"{weight:.2f}", end=" ")