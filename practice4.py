import numpy as np

# 生成随机浮点数组
arr = np.random.random(10)  # 范围0~1
print("原始随机数组:")
print(arr)
print(f"最小值: {arr.min():.4f}, 最大值: {arr.max():.4f}\n")

# 任务1：归一化到[0, 100]
arr_normalized = (arr - arr.min()) / (arr.max() - arr.min()) * 100
print("归一化到[0, 100]:")
print(arr_normalized)
print(f"归一化后范围: [{arr_normalized.min():.2f}, {arr_normalized.max():.2f}]\n")

# 任务2：累计和与累计最大值
cumsum_result = np.cumsum(arr_normalized)
cummax_result = np.maximum.accumulate(arr_normalized)

print("累计和:")
print(cumsum_result)
print("\n累计最大值:")
print(cummax_result)

# 可视化对比（文字版）
print("\n--- 对比 ---")
print("原始值    :", np.round(arr_normalized, 2))
print("累计和    :", np.round(cumsum_result, 2))
print("累计最大值:", np.round(cummax_result, 2))