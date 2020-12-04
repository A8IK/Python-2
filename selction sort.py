##In selction sort we don't need to sorted multiple time .That's the advantage of bubble sort

def sort(nums):

    for i in range (5):          ##we are counting as binary (0,1,2,3,4,5) in range
        minpos = i              ##This line is holding minimum position

        for j in range (i,6):  ## Here '6' because of size or value is six  ##Here we are changing minipos everytime
            if nums[j] < nums[minpos]:

                minpos = j


        ##Here we are swapping....
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)  ##This line is for show how it works.....


nums = [5,3,8,6,7,2]
sort(nums)
print(nums)