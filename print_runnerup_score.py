#Given the participants' score sheet for your University Sports Day, 
#you are required to find the runner-up score. 
#You are given n scores.
#Store them in a list and find the score of the runner-up.
#Example:
#Input:
#5
#2 3 6 6 5
#Output
#5

#here n Reads the number of scores.
n = int(input())

# split() separates space-separated numbers: "2 3 6 6 5" -> ["2", "3", "6", "6", "5"]
# map(int, ...) converts each string to an integer.
arr = map(int, input().split())

# A set removes duplicate values.
# So [2, 3, 6, 6, 5] becomes {2, 3, 5, 6}
unique_arr = set(arr)

# max(unique_arr) finds the highest score (e.g. 6) and removes it
unique_arr.remove(max(unique_arr))

# find runner-up score (e.g. max of {2, 3, 5} is 5)
runner_up = max(unique_arr)

# print runner-up score
print(runner_up)