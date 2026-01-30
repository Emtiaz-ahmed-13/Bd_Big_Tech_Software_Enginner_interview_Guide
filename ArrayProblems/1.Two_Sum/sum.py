from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []



# -------- Driver Code --------
if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers (space separated): ").split()))
    target = int(input("Enter target: "))

    sol = Solution()
    result = sol.twoSum(nums, target)

    print("Output:", result)
