list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]
min_sum = float('inf') 
result = []
for x in list1:
    if x in list1 and x in list2:
        current_sum = list1.index(x) + list2.index(x)
        if current_sum < min_sum:
            min_sum = current_sum
            result = [x]
        elif current_sum == min_sum:
            result.append(x)

print(result)
# print(list1.index("Shogun"))