class Solution:
    def intToRoman(self, num: int) -> str:
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        sym = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        
        res = ""
        
        for i in range(len(val)):
            while num >= val[i]:
                res += sym[i]
                num -= val[i]
        
        return res
