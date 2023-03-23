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
    elif message.startswith("Tell me about"):
        # list = message.split()
        # for i in range(3):
        #     list.pop(0)
        #     print(list)
       
        # print(list)
        # search = " ".join(list)
        search = message.replace("Tell me about ","")
        url = f"<a href='https://en.wikipedia.org/wiki/{search}' target='_blank'>https://en.wikipedia.org/wiki/{search}</a>"
        return f"Here is what I found: {url}"
    else:
        return "Cannot comprehend"