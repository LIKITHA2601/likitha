import random
from collections import Counter
#1. count vowels and consonants
def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    v = 0
    c = 0
    for ch in text:
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    return v, c

def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])
    if cols_a !=rows_b:
        return None
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] +=matrix_a[i][k]*matrix_b[k][j]
    return result

def count_common_elements(list1, list2):
    return len(set(list1)& set(list2))

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[j][i] for j in range(rows)] for i in range(cols)]

def statistics_random_numbers():
    numbers = [random.randint(100, 150) for _ in range(100)]
    mean_value = sum(numbers) / len(numbers)
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median_value = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median_value = sorted_numbers[n // 2]
    frequency = Counter(numbers)
    mode_value = frequency.most_common(1)[0][0]
    return  mean_value, median_value, mode_value

if __name__ == "__main__":
    text = input("Enter a string:")
    v, c = count_vowels_consonants(text)
    print("Numbers of vowels:", v)
    print("Number of consonants:", c)

    matrix_a = [[1, 2],[3, 4]]
    matrix_b = [[5, 6],[7, 8]]
    product  =multiply_matrices(matrix_a, matrix_b)
    
    print("Matrix multiplication result:")
    for row in product:
        print(row)

    list1 = [1, 2, 3, 4, 5] 
    list2 = [3, 4, 5 ,6, 7]
    print("Number of common elements:", count_common_elements(list1, list2))

    matrix = [[1, 2, 3],[4, 5, 6]]
    print("Transpose of matrix:")
    for row in transpose_matrix(matrix):
        print(row)

    mean_val, median_val, mode_val = statistics_random_numbers()
    print("Mean:",mean_val)
    print("Median:", median_val)
    print("Mode:", mode_val)
        


            
