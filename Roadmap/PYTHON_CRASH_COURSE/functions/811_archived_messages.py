"""
8-11. Archived Messages: Start with your work from Exercise 8-10. Call the func-
tion send_messages() with a copy of the list of messages. After calling the func-
tion, print both of your lists to show that the original list has retained its messages.
"""

def send_messages(messages: list):
    sended = []
    for message in messages:
        sended.append(message)
        print(message)
    
    print(f"Message to send: {messages}")
    print(f"Messages sended: {sended}")
    
messages = ["Hello", "How old are you", "See you later"]

send_messages(messages=messages[:])