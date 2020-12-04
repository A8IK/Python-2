## "BUBBLE SORT" is all about comparing and swapping

def sort(nums):
##Here we have to think how many time I want to do this  and
##Which way we have to do this

    for i in range (len(nums)-1,0,-1):          ##outer loop(multiple iteration)
        ##outer loop just for check the number of element
        ##inner loop is swapping value

        for j in range (i):  ### Inner loop
            if nums[j]>nums[j+1]:
                temp = nums[j]   # Here it's swapping range
                nums [j] = nums[j+1]
                nums[j+1] = temp


nums = [5,3,8,6,7,2]
sort(nums)

print(nums)
