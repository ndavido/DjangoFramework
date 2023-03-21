from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def backend(request, slug=None):
    return HttpResponse("<p>Hello from the backend-side</p>")

import json

def get_chat_response(request, slug=None):
    response = {
        "message": "Hello from chatbot"
    }
    return HttpResponse(json.dumps(response))