from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .agents import run_agent

import os

def chat_page(request):
    return render(request, "chat.html")

@csrf_exempt
def ask_agent(request):
    if request.method == "POST":
        report = request.FILES.get("report")
        question = request.POST.get("question")

        if not report or not question:
            return JsonResponse({"error": "Both report and question are required."}, status=400)

        # Read and decode uploaded report
        report_text = report.read().decode("utf-8")

        # Run agent
        response = run_agent(question, report_text)

        return JsonResponse({"response": response})