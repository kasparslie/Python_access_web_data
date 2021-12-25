import re
file = input("Enter file:")
if len(file) < 1:
    file = "regex_sum_1425734.txt"
handle = open(file)
sum=0
for line in handle:
    line = line.rstrip()
    data = re.findall('[0-9]+', line)
    print(data)
    for number in data:
        sum = sum + int(number)
        
    print(sum)
