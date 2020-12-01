# 

infile=open("input.txt")
input=infile.readlines()
nums=[int(str) for str in input]


# pt.1

for n in nums:
    if (2020-n) in nums:
        print(n*(2020-n))
        break

# pt.2
res=False
for i in range(len(nums)):
    n1=nums[i]
    quotient=2020-n1
    for j in range(i+1,len(nums)):
        n2=nums[j]
        if (quotient-n2) in nums:
            print(n1*n2*(quotient-n2))
            res=True
            break
    if res: break
