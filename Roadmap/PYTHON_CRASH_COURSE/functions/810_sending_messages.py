"""
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it’s printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly.
"""

def send_messages(messages: list):
    sended = []
    for message in messages:
        sended.append(message)
        print(message)
    
    print(f"Message to send: {messages}")
    print(f"Messages sended: {sended}")
    
messages = ["Hello", "How old are you", "See you later"]

send_messages(messages=messages)