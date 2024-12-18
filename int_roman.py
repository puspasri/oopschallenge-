class solution :
    def int_roman(self,num):
        
        res=""

        for (n,rom) in lookup:
            (d,num)=divmod(num,n)
            res+rom*d
        return res 
    
obj=solution()
print(obj.int_roman(51))