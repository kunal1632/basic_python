tallies = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def romanToDecimal(num):
    sum = 0
    for i in range(len(num)-1):
        left = num[i]
        right = num[i+1]
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else:
            sum += tallies[left]

    sum += tallies[num[-1]]
    return sum


number = input("Enter a number: ").upper()
ans = romanToDecimal(number)
print(ans)
