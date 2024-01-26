import numpy as np

def read_input(file_path):
    with open(file_path, "r") as file:
        lines = file.read().split('\n')
    lines.pop(-1)
    return [line.split() for line in lines]

def main():
    input_path = "C:\\Users\Downloads\documents\input10.txt"
    data = read_input(input_path)

    n, m = int(data[0][0]), int(data[0][1])
    numbers = [int(item) for sublist in data[1:] for item in sublist]

    matrix = np.array(numbers).reshape((n, m, m))

    max_det = -float('inf')
    max_matrix = None

    for i in range(n):
        for j in range(i + 1, n):
            tmp_det = np.linalg.det(np.dot(matrix[i], matrix[j]))

            if tmp_det > max_det:
                max_det = tmp_det
                max_matrix = (matrix[i], matrix[j])

    if np.linalg.det(max_matrix[0]) < np.linalg.det(max_matrix[1]):
        max_matrix = (max_matrix[1], max_matrix[0])

    final_res = np.linalg.inv(np.dot(max_matrix[0], max_matrix[1]))
    final_res = final_res.tolist()

    for row in final_res:
        print(" ".join([f"{round(val, 3)}" for val in row]))

if __name__ == "__main__":
    main()
