from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def backend(request, slug=None):
    return HttpResponse("<p>Hello from the backend-side</p>")

import json
from .responses import bot_response

def get_first_message(request, slug=None):
    response = {
        "message": "Hello, how can I help you today?"
    }
    return HttpResponse(json.dumps(response))

def get_chat_response(request, slug=None):
    data = request.GET
    message = data.get("message")
    
    response = {
        "message": bot_response(message)
    }
    return HttpResponse(json.dumps(response))