def spiralize(number):
    n = 1
    step = 2
    total_value = 0
    matrix_row = 0
    while (n <= (number**2)):
        total_value += n
        n += step
        matrix_row += 1
        if matrix_row == 4:
            step += 2
            matrix_row = 0
    return total_value

if __name__ == "__main__":
    print(spiralize(501))
