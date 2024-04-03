import sys

def smash_pinatas(pinatas):
    num_pinatas = len(pinatas)
    
    if num_pinatas == 0:
        return 0
    elif num_pinatas == 1:
        return pinatas[0]

    max_candies = 0
    for i in range(num_pinatas):
        if i - 1 >= 0:#there's a pinata to the left of the current pinata
            left = pinatas[i - 1]
        else:#out of bounds
            left = 1
        
        if i + 1 < num_pinatas:#there's a pinata to the right 
            right = pinatas[i + 1]
        else:#there's no pinata to the right
            right = 1
        
        candies = left * pinatas[i] * right
        max_candies = max(max_candies, candies)#get max value

    return max_candies

def main():
    if len(sys.argv) < 2:
        print("Program receives as input array of nums,\
           \nPlease add numbers as parameters")
        sys.exit(1)

    pinatas = []
    for num in sys.argv[1:]:
        try:
            pinatas.append(int(num))
        except ValueError:
            print("Invalid input. Please provide integers only.")
            sys.exit(1)

    max_candies = smash_pinatas(pinatas)
    print("Max amount of candies:", max_candies)

main()
