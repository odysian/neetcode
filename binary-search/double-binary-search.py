class Solution:
    @staticmethod
    def double_binary_search(matrix, target):
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                break
        if not (top <= bot):
            return False

        l, r = 0, cols - 1
        row = (top + bot) // 2
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        return False


def main():
    test_matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(f"matrix: {test_matrix}")
    print(
        f"target: 3 -> found: {Solution.double_binary_search(test_matrix, 3)}"
    )  # Should return True
    print(
        f"target: 13 -> found: {Solution.double_binary_search(test_matrix, 13)}"
    )  # Should return False


if __name__ == "__main__":
    main()
