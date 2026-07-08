import numpy as np

# 任务1：逐元素乘法和矩阵乘法
A = np.random.randint(1, 10, size=(2, 3))
B = np.random.randint(1, 10, size=(2, 3))
print("数组A (2x3):")
print(A)
print("\n数组B (2x3):")
print(B)

element_wise = A * B  # 逐元素乘法
print(f"\n逐元素乘法 A * B:\n{element_wise}")

# 矩阵乘法需要维度匹配：A(2,3) @ B.T(3,2) = (2,2)
matrix_product = A @ B.T
print(f"\n矩阵乘法 A @ B.T:\n{matrix_product}")

# 任务2：按行和列求和
arr2 = np.array([[1, 2], [3, 4]])
print(f"\n数组: \n{arr2}")
print(f"按行求和 (axis=1): {np.sum(arr2, axis=1)}")
print(f"按列求和 (axis=0): {np.sum(arr2, axis=0)}")

# 任务3：统计运算
arr3 = np.array([1.2, 3.5, 2.8])
print(f"\n数组: {arr3}")
print(f"均值: {np.mean(arr3):.2f}")
print(f"标准差: {np.std(arr3):.3f}")
print(f"四舍五入: {np.round(arr3)}")
print(f"四舍五入到1位小数: {np.round(arr3, 1)}")