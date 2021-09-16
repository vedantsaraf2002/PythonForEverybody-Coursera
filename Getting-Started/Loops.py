largest = 0
smallest = 999999

while True:
    num = input("Enter a number: ")
    if num == "done":
        break    
    try:
      n = int(num)
    except:
        print("Invalid input")
        
    if n>largest:
        largest = n
    if n<smallest:
        smallest = n
    
    #print(num)

print("Maximum is", largest)
print("Minimum is", smallest)


