class Solution:

    def __init__(self):
        pass

    def romanToInt(self, s:str)-> int:
        a = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        c = 0
        i = 0
        while i < len(s):
            if (i != (len(s) - 1)) and (a[s[i]] < a[s[i + 1]]):

                c += (a[s[i + 1]] - a[s[i]])
                i = i + 1
            else:
                c += a[s[i]]

            i += 1

        return c



s = input()
solution = Solution()
count = solution.romanToInt(s)
print(count)



