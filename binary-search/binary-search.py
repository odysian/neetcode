class Solution:
    @staticmethod
    def binary_search(array: list[int], target: int) -> int:
        l, r = 0, len(array) - 1

        while l <= r:
            mid = (l + r) // 2
            if array[mid] < target:
                l = mid + 1
            elif array[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1


def main():
    test_array = [-1, 0, 3, 4, 7, 8, 12, 16]
    test_target = 12
    res = Solution.binary_search(test_array, test_target)
    print(f"array: {test_array}")
    print(f"target: {test_target} -> index: {res}")


if __name__ == "__main__":
    main()
