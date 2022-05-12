#Kai Geller
#GitHub Username: KaiGeller
#5/11/2022
#The goal of this assignment is to take a list and square all of the numbers in it and print the list
def square_list(nums):
    """This will take the numbers in a list and square them then print the numbers."""
    for i in range(len(nums)):
        nums[i]=(nums[i]*nums[i])
