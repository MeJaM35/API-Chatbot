from django.shortcuts import render
from django.http import HttpResponse
from openai import OpenAI


client = OpenAI(
    # Defaults to os.environ.get("OPENAI_API_KEY")
    api_key='your key here'
)





def index(request):
    return render(request, 'core.html')

# Create your views here.
