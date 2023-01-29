class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
      
        # 3 7 8
        # 11 9 13
        # 15 16 17
        
        # transpose = list(zip(*matrix))
        # print(transpose)
        
        # unpacking operator, zip, and sets intersection
        return list({min(row) for row in matrix} & {max(col) for col in zip(*matrix)})