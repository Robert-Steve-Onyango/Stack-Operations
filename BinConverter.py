from stacks import Stack

def convert_int_to_bin(num):
    
    if num == 0:
        return 0
    
    s = Stack()

    while num > 0:
        remainder = num % 2
        s.push(remainder)
        num = num // 2

    bin = ""
    while not s.is_empty():
        bin += str(s.pop())

    return bin
num = int(input("Enter the number: "))
print(convert_int_to_bin(num))