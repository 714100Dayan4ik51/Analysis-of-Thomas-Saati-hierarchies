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
