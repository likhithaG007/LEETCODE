class Solution:
    def searchRange(self, nums, target):

        def findFirst():
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    right = mid - 1

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return ans

        def findLast():
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return ans

        return [findFirst(), findLast()]


# Main program
nums = [5, 7, 7, 8, 8, 10]
target = 8

obj = Solution()
result = obj.searchRange(nums, target)

print(result)