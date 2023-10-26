try:
    user_input = str(input("Enter the String: "))
except ValueError:
    print("The Input Should Be in String..!")


vowels = ["a", "e", "i", "o", "u"]


def check_the_vowels(user, vowel):
    count = 0
    vowel_count = {}

    for i in user.lower():
        # Counting the Actual Value
        for j in vowel:
            if i == j:
                count += 1
                if i in vowel_count:
                    vowel_count[i] += 1
                else:
                    vowel_count[i] = 1
    percentage = 100.0 * count / len(user)
    return vowel_count, percentage, count


Vowels_item, percentage, total_count = check_the_vowels(user_input, vowels)

print()
print(f"The Vowels in This String ")
for key, value in Vowels_item.items():
    print(f"{key} => {value}")
print()

print(f"Total Vowels in a String : {total_count}")
print()

print(f"Percentage: {percentage}%")
