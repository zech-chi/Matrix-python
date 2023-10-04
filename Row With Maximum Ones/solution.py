class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        row = 0
        count = 0
        for r in range(len(mat)):
            cur_count = 0
            for c in range(len(mat[0])):
                cur_count += mat[r][c]
            if cur_count > count:
                count = cur_count
                row = r
        return [row, count]
