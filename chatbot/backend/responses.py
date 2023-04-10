import random
import requests

last_message = ""

def bot_response(message):
    global last_message
    if message == last_message:
        return "STOP REPEATING YOURSELF!"
    elif message == "hello":
        last_message = message
        return "hello there human being!"
    elif message == "goodbye":
        last_message = message
        return "short circuit executed!"
    elif message == "gimme image":
        last_message = message
        id = str(random.randint(1, 1000))
        url = f"https://picsum.photos/500/500/?id={id}"
        generated_image = f"<img src='{url}' width='500' height='500'>"
        return generated_image
    elif message.startswith("tell me about"):
        last_message = message
        search = message.replace("Tell me about ","")
        url = f"<a href='https://en.wikipedia.org/wiki/{search}' target='_blank'>https://en.wikipedia.org/wiki/{search}</a>"
        return f"Here is what I found: {url}"
    elif message == "help":
        last_message = message
        commands = '''
            <div>
                <b><p>Gimme image</p></b>
                <p>I will reply with a random image.</p>
            </div>
            <br>
            <div>
                <b><p>Tell me about SOMETHING</p></b>
                <p>SOMETHING can be any kind of sentence, I will give you a Wikipedia link to that article back.</p>
            </div>
            <br>
            <div>
                <b><p>Weather in &lt;city&gt;</p></b>
                <p>For example, weather in Pori, I will respond back with the weather in Pori</p>
            </div> 
        '''
        return commands
    elif message.startswith("weather in"):
        city = message.replace("weather in ", "")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=8dd0bfdf34498af25b68abf9856bb663&units=metric"
        
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] != "404":
            weather_info = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            
            message = f"The weather in {city} is {weather_info}. The temperature is {temperature}°C, and it feels like {feels_like}°C."
            return message
        else:
            return "Sorry, I couldn't find the weather information for that city."
    else:
        last_message = message
        return "Cannot comprehend, type 'Help' to find out what I know :)"
        
    
    