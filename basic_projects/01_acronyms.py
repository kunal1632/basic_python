user_input = input("Enter a pharse: ")
text = user_input.split()
ans = ""
for i in text:
    ans = ans+str(i[0]).upper()

print(ans)
