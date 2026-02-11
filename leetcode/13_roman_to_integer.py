class Solution:
    def romanToInt(self, s: str) -> int:
        doubles = {  
                "IV": 4,
                "IX": 9,
                "XL": 40,
                "XC": 90,
                "CD": 400,
                "CM": 900
                }
        singles = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000,
        }
        res = 0

        for n in doubles:
            if n in s:
                res += doubles[n]
                s = s.replace(n, "")
                
        for n in s:
            res += singles[n]
        return res
