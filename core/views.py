from django.shortcuts import render
from django.http import HttpResponse
from openai import OpenAI


client = OpenAI(
    # Defaults to os.environ.get("OPENAI_API_KEY")
)


def get_completion(prompt):
    query = client.chat.completions.create(
        model="gpt-3.5-turbo",
       messages=[ 
           {"role": "system", "content": "You are a helpful AI assistant."},
           {"role": "user", "content": prompt}],
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = query.choices
    return response





def index(request):
    context = {}
    if request.method == "POST":
        prompt = request.POST.get('prompt')
        response = get_completion(prompt)
        context['response'] = response
    
    return render(request, 'core.html', context)

# Create your views here.
