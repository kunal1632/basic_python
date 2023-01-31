import random
low_alpha = "abcdefghijklmnopqrstuvwxyz"
upp_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeric = "1234567890"
special_char = "!@#%^&*"
all_letter = low_alpha+upp_alpha+numeric+special_char
length = int(input("Enter the length of the password: "))
len_alpha_low = int(input("Enterthe minimum number of lower alphabets: "))
len_alpha_upp = int(input("Enterthe minimum number of upper alphabets: "))
len_numeric = int(input("Enter the minimum number of numbers: "))
len_special = int(input("Enter the minimum numbe of special character: "))

ans_low_alpha = "".join(random.choice(low_alpha) for i in range(len_alpha_low))
ans_upp_alpha = "".join(random.choice(upp_alpha) for i in range(len_alpha_upp))
ans_numeric = "".join(random.choice(numeric) for i in range(len_numeric))
ans_special = "".join(random.choice(special_char) for i in range(len_special))

temp_pw = ans_low_alpha+ans_upp_alpha+ans_numeric+ans_special

total_len = len_alpha_upp + len_alpha_low + len_numeric + len_special

if total_len < length:
    for i in range(length-total_len):
        temp_pw = temp_pw+random.choice(all_letter)
    final_pw = "".join(random.sample(temp_pw, length))
    print("Your password is:")
    print(final_pw)
elif total_len > length:
    print("You have enter invalid amount of character")
