class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_v = max(candies)
        print(max_v)
        ans = []
        
        def f(x):
            return x + extraCandies >= max_v
        
        for i in range(0, len(candies)):
            if f(candies[i]):
                ans.append(True)
            else:
                ans.append(False)

        return ans