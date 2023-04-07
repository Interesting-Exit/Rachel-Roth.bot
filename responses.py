import random


def get_response(message) -> str:
    p_message = message.lower()

    if p_message == "hey":
        return "Heya"

    elif p_message == "roll":
        return "The number you rolled between 1 and 50 is: "+str(random.randint(1, 50))+"!"

    elif "tenor" in p_message:
        return

    elif p_message == "!help":
        return '**Current commands are: "hey" and "roll" **'

