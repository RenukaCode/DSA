def fn(nums):
    n=len(nums)
    st=[]
    for num in nums:
        if num > 0:
            st.append(num)
        else:
            while(st and st[-1] > 0 and st[-1] < abs(num)):
                st.pop()
            if st[-1] == abs(num):
                st.pop()
            elif not st or st[-1]<0:
                st.append(num)
    return st
print(fn([10,20,-10]))  # [10,20]
print(fn([10,-10]))     # [10]