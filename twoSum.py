def twoSum(nums: list[int], target: int) -> list[int]:
    map = {}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in map:
            return [map[diff],i]
        map[n] = i
         
#   We want a target of 7
#   So the resulting list should be => [0,3]

sample = [2,9,3,5]
answer = twoSum(sample, 7)
print(answer)

test2 = [3,2,4]
nextans = twoSum(test2, 6)
print(nextans)

test3 = [2,2]
nextans2 = twoSum(test3, 4)
print(nextans2)
         
test3 = [0,2,2,0]
nextans2 = twoSum(test3, 0)
print(nextans2)
         
#   O(n) => Uses one loop
#   Find the difference of target and an element
#   Then, looks for the diff in map
