class Solution:
    @staticmethod
    def quick_sort(arr, low, high):
        if low < high:  # 修正递归终止条件
            partition_i = Solution.partition(arr, low, high)
            Solution.quick_sort(arr, low, partition_i - 1)  # 注意递归的范围
            Solution.quick_sort(arr, partition_i + 1, high)  # 注意递归的范围

    @staticmethod
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


# 示例使用
arr = [10, 7, 8, 9, 1, 5]
print("Initial array:", arr)
Solution.quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
