chosenValue = -1
currentDigit = -1

while True:
    if input.button_is_pressed(Button.A):
        currentDigit -= 1
        if currentDigit < 0:
            currentDigit = 9
        basic.show_number(currentDigit)
    if input.button_is_pressed(Button.B):
        if currentDigit == 9:
            currentDigit = -1
        currentDigit += 1
        basic.show_number(currentDigit)
    if input.logo_is_pressed():
        chosenValue = currentDigit
        print(currentDigit)