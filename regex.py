#The basic outline of this problem is to read the file, 
# look for integers using the re.findall(), looking for a regular expression of '[0-9]+'
# and then converting the extracted strings to integers and summing up the integers.

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
