import random

def bot_response(message):
    if message == "hello": 
        return "Hello there human being!"
    elif message == "goodbye":
        return "Short circuit executed!"
    elif message == "Gimme image":
        id = str(random.randint(1, 1000))
        url = f"https://picsum.photos/500/500/?id={id}"
        generated_image = f"<img src='{url}' width='500' height='500'>"
        return generated_image
    else:
        return "Cannot comprehend"