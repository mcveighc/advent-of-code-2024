
def calc_digits(nums): 
    result = 0
    for i in nums:
      result += i

    return result

def cacl_pair_distance(left, right):
   distance = left - right
   if distance < 0:
      distance *= -1

   return distance

def sort_list(nums):
   nums.sort()
   return nums

def get_list_distances(leftNums, rightNums):
   distances = []

   sortedLeft = sort_list(leftNums)
   sortedRight = sort_list(rightNums)

   i = 0
   while i < len(sortedLeft):
      left = sortedLeft[i]
      right = sortedRight[i]

      distance = cacl_pair_distance(left, right)
      distances.append(distance)

      i+=1
   
   return distances

def get_nums_from_input_line(input):
   santized = input.replace("\n", "")

   left = int(santized[:5])
   right = int(santized[-5:])

   return [left, right]

def get_distance_total():
   distances = []
   left = []
   right = []

   f = open("inputs/hystorian_hysteria.txt", "r")
   for input in f:
      nums = get_nums_from_input_line(input)
      left.append(nums[0])
      right.append(nums[1])
   f.close()

   inputDistances = get_list_distances(left, right)
   inputDistancesTotal = calc_digits(inputDistances)
   distances.append(inputDistancesTotal)

   return calc_digits(distances)

## Part 2
def get_similarity_score(left, right):
   digits = []

   for i in left:
      count = 0
      for j in right:
         if j == i:
            count+=1
      digits.append(i * count)
   
   return calc_digits(digits)

def get_similarity_total():
   left = []
   right = []

   f = open("inputs/hystorian_hysteria.txt", "r")
   for input in f:
      nums = get_nums_from_input_line(input)
      left.append(nums[0])
      right.append(nums[1])
   f.close()
   
   return get_similarity_score(left, right)
