import numpy as np

# 任务1：创建形状为(3,4)的随机整数数组（范围0~9）
arr = np.random.randint(0, 10, size=(3, 4))
print("原始数组 (3x4):")
print(arr)
print(f"形状: {arr.shape}\n")

# 任务2：重塑为(4,3)并转置
reshaped_arr = arr.reshape(4, 3).T
print("重塑为(4,3)并转置后的数组:")
print(reshaped_arr)
print(f"形状: {reshaped_arr.shape}\n")

# 任务3：提取所有大于5的元素
filtered_arr = arr[arr > 5]
print("所有大于5的元素:")
print(filtered_arr)
print(f"元素个数: {len(filtered_arr)}")