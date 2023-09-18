import random
import pygame

pygame.init()
pygame.mixer.init()


# Here We Write the Question And there Option and the Question Answer We get This value By his index number
questions = [
    ["what is the color of Apple ?", "Red", "Blue", "Green", "Oranges", 1],
    ["what is the color of Orange ?", "Red", "Blue", "Green", "Oranges", 4],
    ["What is the color of Sky ?", "Red", "Blue", "Green", "Oranges", 2],
    ["What is the color of Blood ?", "Red", "Blue", "Green", "Oranges", 1],
    ["What is the color of Leaf ?", "Red", "Blue", "Green", "Oranges", 3],
    ["What is the color of Milk ?", "White", "Blue", "Green", "Oranges", 1],
    ["What is the color of Sunflower ?", "Red", "Blue", "Yellow", "Oranges", 3],
    ["What is the color of Chocolate ?", "Red", "Blue", "Green", "Brown", 4],
    ["What is the color of Wine ?", "Red", "Blue", "Green", "Oranges", 1],
    ["What is the color of Metal ?", "Silver", "Blue", "Green", "Oranges", 1],
    ["What color is the symbol pf peace ?", "Silver", "Blue", "Green", "White", 4],
    [
        "What color is most associated with Christmas ?",
        "Silver",
        "Blue",
        "Red",
        "Oranges",
        3,
    ],
    ["What color are the Smurfs ?", "Silver", "Blue", "Green", "Oranges", 2],
]

# Here We Created a Rule Where We Decided the game will carry 13 Question of amount 1 crore

levels = [
    1000,
    2000,
    3000,
    5000,
    10000,
    20000,
    40000,
    80000,
    160000,
    320000,
    640000,
    1250000,
    10000000,
]

# this Variable is Set for making game more intresting that if the user not go to rs 5000 rs question then they taken  money will 0 rs and so on the rule is going
money = 0
print("\n Let The Game Begin....!!")

# analysis part

total_answer = 0

# this Variable is use for Checking the lifeline is used or not to make the many condition in the below code 1 represt not use lifeline and 0 represent the user use the lifeline
fifty_fifty_lifelines = 1
skip_question = 1


# this Function is Creating to make this game more enhancing it mean every question the sound come of the game
def play_question_sound():
    question_sound = pygame.mixer.Sound("question_sound.wav")
    question_sound.play()


# this Function is for slip the Question Lifeline
def skip_the_question():
    print("You've chosen to skip this question.")


# this Function is for 50-50 Lifeline in this Function
def activate_5050(question):
    options = question[1:5]
    correct_answer = question[-1]

    incorrect_options = []

    # Loop through the options
    for i, option in enumerate(options, 1):
        if i != correct_answer:
            incorrect_options.append(option)
    # print(incorrect_options)
    removed_option = random.choice(incorrect_options)

    return removed_option


# here the looping of question start  we use for loop
for i in range(len(questions)):
    play_question_sound()

    # In this variable we get in which question number we have
    question = questions[i]
    question_no = i + 1
    print(f"\nHere is your {question_no} question for Rs {levels[i]}:")
    print("\033[1m" + question[0] + "\033[0m")
    print("---------------------------------")
    print("Here are your options:")
    print(f"1. {question[1]}                2. {question[2]}")
    print(f"3. {question[3]}              4. {question[4]}")
    print("---------------------------------")
    print()
    print("The Avallables Lifelines are")
    print()

    # Check the Avaibility of the lifelines
    if fifty_fifty_lifelines > 0:
        print("5. 50-50")

    if skip_question > 0:
        print("6. Skip the Question")

    # show this statement when all the lifeline will used by the user
    if fifty_fifty_lifelines == 0 and skip_question == 0:
        print("-----------------------------------")
        print("| You Have Used Your All Lifelines |")
        print("-----------------------------------")
        print()

    # here we set
    valid_input = False

    while not valid_input:
        try:
            user_answer = int(input("Enter your answer (1-4): "))
            valid_input = True
        except ValueError:
            print("Answer should be given as a number between 1 and 4.")

    # In the last index of the list the we get the correct answer of the question
    correct_answer = question[-1]

    lifeline_used_question = False
    #    Code if the user chooses lifeline

    # 1. 50-50
    if fifty_fifty_lifelines > 0:
        if user_answer == 5 and fifty_fifty_lifelines > 0:
            # these VAriable Estate that the user use the lifeline
            lifeline_used_question = True
            fifty_fifty_lifelines -= 1

            remaining_options = activate_5050(question)

            # Here the Value will Randomly Shuffle from the list
            fifty_fifty_option = [question[correct_answer], remaining_options]
            random.shuffle(fifty_fifty_option)

            print("50-50 Lifeline activated. Here are your options:")
            print("---------------------------------")
            print("Here are your options:")
            print(
                f"1. {fifty_fifty_option[0]}                2. {fifty_fifty_option[1]}"
            )
            print("---------------------------------")
            user_answer = int(input("Enter your answer (1-2): "))

    # 2. Skip the Answer
    if skip_question > 0:
        if user_answer == 6 and skip_question > 0:
            skip_the_question()

            # these VAriable Estate that the user use the lifeline
            skip_question -= 1
            continue

    # code end with lifeline
    # -----------------------
    # If the Answer is Correct goes to the below condition ---> This code go to that condition when the 50-50 lifeline not use
    if lifeline_used_question is False:
        if user_answer == correct_answer:
            print(f"Congratulations! You won Rs {levels[i]}")

            # money = levels[i]

            # Here We Creating A Levels for the user if the answer is wrong then what actual money what they get
            if i == 4:
                money = 10000
            elif i == 9:
                money = 320000
            elif i == 12:
                money = 10000000

        else:
            print("Oops! Your answer is incorrect.")
            print(f"Total Answer You gave: {total_answer} out of 13")
            print(f"You left {13 - total_answer} Question behind to became crorepati")
            break

    # There i make a Condition on make your the user chooses correct answer if user using lfeline otherwise it take only the list answer i given above
    elif lifeline_used_question is not False:
        answer_this = ""
        if user_answer == 1:
            answer_this = fifty_fifty_option[0]
        else:
            answer_this = fifty_fifty_option[1]
        if answer_this.lower() == question[correct_answer].lower():
            # print("Lifeline answer: " + answer_this)
            print(f"Congratulations! You won Rs {levels[i]}")
        else:
            print("Oops! Your answer is incorrect.")
            print(f"Total Answer You gave: {total_answer} out of 13")
            print(f"You left {13 - total_answer} Question behind to became crorepati")
            break
        lifeline_used_question = False

    # increment When the Question they Give
    total_answer += 1

    print("---------------------------------")
if money == 10000000:
    print("Jack Pot!!!!! YOU ARE THE WINNER OF KAUN BANEGA CROREPATI : ) ")
    print(f"Your Total Wining Amount is Rs. {money}")
else:
    print("\nGame Over!")
    print(f"Your total winnings are: Rs. {money}")
