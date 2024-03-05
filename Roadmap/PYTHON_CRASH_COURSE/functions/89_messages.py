"""
8-9. Messages: Make a list containing a series of short text messages. Pass the
list to a function called show_messages(), which prints each text message.
"""

def show_messages(messages: list):
    for message in messages:
        print(f"{message}")

messages = ["Hello", "How old are you", "See you later"]

show_messages(messages=messages)