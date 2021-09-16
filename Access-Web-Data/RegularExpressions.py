import re
x = open('q.txt','r')
total = 0
for line in x:
    line = line.rstrip()
    y = re.findall('[0-9]+',line)
    for element in y:
        if element.isdigit():
      # adding the element to the total
            total += int(element)
# printing the total
print(total)

            
