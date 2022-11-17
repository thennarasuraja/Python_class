pyramid_size = int(input("Enter Pyramid Size: "))
pyramid_space = pyramid_size-1
display_number = 1
for x in range(0, pyramid_size):
    for j in range(0, pyramid_space):
        print(end=" ")
    pyramid_space = pyramid_space-1
    for l in range(0, x+1):
        print(display_number, end=" ")
        display_number += 1
    print("\r")
for y in range(pyramid_size-2, -1, -1):
    for j in range(0, pyramid_space+2):
        print(end=" ")
    pyramid_space = pyramid_space+1
    for l in range(y+1, 0, -1):
        print(display_number, end=" ")
        display_number += 1
    print("\r")
