import math

import matplotlib.pyplot as plt

from playLA.Matrix import Matrix

if __name__ == "__main__":
    plt.figure(figsize=(5, 5))
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    print("------")

    # 绘制原始矩阵图
    # matrix: 原始矩阵 (每行代表一个坐标)
    # transposed_matrix: 原始矩阵 (每列代表一个坐标)

    m_points = [[0, 0], [0, 5], [3, 5], [3, 4], [1, 4],
                [1, 3], [2, 3], [2, 2], [1, 2], [1, 0]]

    matrix = Matrix(m_points)
    transposed_matrix = matrix.transpose()
    print("matrix:", matrix)
    print("transposed_matrix:", transposed_matrix)

    # 绘制
    # x = [point[0] for point in m_points]
    # y = [point[1] for point in m_points]
    x = [transposed_matrix.col_vector(i)[0] for i in range(transposed_matrix.col_num())]
    y = [transposed_matrix.col_vector(i)[1] for i in range(transposed_matrix.col_num())]
    plt.plot(x, y)

    print("------")

    # 绘制变换后的矩阵图
    # transform: 变换矩阵
    # transformed_transposed_matrix: 变换后的矩阵 (每列代表一个坐标)

    # 缩放: 将 x 扩大 2 倍, y 扩大 1.5 倍
    # t_points = [[2, 0], [0, 1.5]]
    # 翻转: 关于 x 轴对称
    # t_points = [[1, 0], [0, -1]]
    # 翻转: 关于 y 轴对称
    # t_points = [[-1, 0], [0, 1]]
    # 翻转: 关于原点对称
    # t_points = [[-1, 0], [0, -1]]
    # 错切: 沿 x 轴错切
    # t_points = [[1, 0.5], [0, 1]]
    # 错切: 沿 y 轴错切
    # t_points = [[1, 0], [0.5, 1]]
    # 旋转: 沿原点顺时针旋转 60 度
    # t_points = [[cos60°, sin60°], [-sin60°, cos60°]]
    theta = math.pi / 3
    t_points = [[math.cos(theta), math.sin(theta)], [-math.sin(theta), math.cos(theta)]]

    transform = Matrix(t_points)
    transformed_transposed_matrix = transform.dot(transposed_matrix)
    print("transform:", transform)
    print("transformed_transposed_matrix:", transformed_transposed_matrix)

    # 绘制
    x2 = [transformed_transposed_matrix.col_vector(i)[0] for i in range(transformed_transposed_matrix.col_num())]
    y2 = [transformed_transposed_matrix.col_vector(i)[1] for i in range(transformed_transposed_matrix.col_num())]
    plt.plot(x2, y2)

    # 显示
    plt.show()
