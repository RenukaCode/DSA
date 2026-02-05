# Time Complexity: O(2^n)
# Space Complexity: O(n)
def generate(n, curr,res):
    if len(curr)==n:
        res.append(curr)
        return 
    generate(n,curr+"0",res)
    if not curr or curr[-1] != "1":
        generate(n,curr+"1",res)
n = 3
res = []
generate(n,"",res)
print(res)   #['000', '001', '010', '100', '101']
n = 4
res = []
generate(n,"",res)
print(res)   #['0000', '0001', '0010', '0100', '0101', '1000', '1001', '1010']
