from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ollama_app.langchain_utils import get_answer, vector_db
from .models import ChatMessage


@api_view(["POST"])
def chat_message(request):
    if request.method == "POST":
        data = request.data
        print("Received data:", data)
        message = data.get("message")
        if message:
            msg = ChatMessage.objects.create(message=message)
            vector_db()
            response = get_answer(msg.message)
        return Response(
            {"message": msg.message, "id": msg.id, "response": response}, status=201
        )
    else:
        print("Invalid request method:", request.method)
    return Response({"error": "Invalid request"}, status=400)
