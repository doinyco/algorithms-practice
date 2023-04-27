# Hamming distance between two integers is the number of positions at which the corresponding bits are different
# Given two integers x and y, calculate the Hamming distance.

# x = 1, y = 4, output: 2

def hamming_distance(x, y):
    x_binary = bin(x)[2:]
    y_binary = bin(y)[2:]

    count = 0

    x_index = len(x_binary) - 1
    y_index = len(y_binary) - 1

    while x_index >= 0 or y_index >= 0:
        if x_index >= 0:
            x_digit = x_binary[x_index]
        else:
            x_digit = "0"

        if y_index >= 0:
            y_digit = y_binary[y_index]
        else:
            y_digit = "0"

        if x_digit != y_digit:
            count += 1

        x_index -= 1
        y_index -= 1

    return count

#  0123
# "1010"
#    01
# "0011"

x = 10
y = 3
R = hamming_distance(x, y)
print(R)