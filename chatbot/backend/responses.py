import random

last_message = ""

def bot_response(message):
    global last_message
    if message == last_message:
        return "STOP REPEATING YOURSELF!"
    elif message == "hello":
        last_message = message
        return "Hello there human being!"
    elif message == "goodbye":
        last_message = message
        return "Short circuit executed!"
    elif message == "Gimme image":
        last_message = message
        id = str(random.randint(1, 1000))
        url = f"https://picsum.photos/500/500/?id={id}"
        generated_image = f"<img src='{url}' width='500' height='500'>"
        return generated_image
    elif message.startswith("Tell me about"):
        last_message = message
        search = message.replace("Tell me about ","")
        url = f"<a href='https://en.wikipedia.org/wiki/{search}' target='_blank'>https://en.wikipedia.org/wiki/{search}</a>"
        return f"Here is what I found: {url}"
    elif message == "Help":
        last_message = message
        commands = '''
            Yes
        '''
        return commands
    else:
        last_message = message
        return "Cannot comprehend, type 'Help' to find out what I know :)"
        
    
    