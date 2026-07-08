import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("原始数组:")
print(arr)
print(f"形状: {arr.shape}\n")

# 任务1：获取第2行的第1~3列
result1 = arr[1, 0:3]
print(f"任务1 - 第2行的第1~3列: {result1}")

# 任务2：获取所有行的第3列
result2 = arr[:, 2]
print(f"任务2 - 所有行的第3列: {result2}")

# 任务3：使用步长切片获取奇数行（第1、3行）
result3 = arr[::2, :]
print(f"任务3 - 奇数行（第1、3行）:")
print(result3)

# 额外演示：对比不同索引方式
print("\n--- 索引方式对比 ---")
print(f"arr[:, 2] (所有行第3列): {arr[:, 2]}")
print(f"arr[:, 2:3] (保留维度): \n{arr[:, 2:3]}")
print(f"arr[::2, :] (步长2的行): \n{arr[::2, :]}")