

# API Based ChatBot

This repository contains a Django Cookiecutter template that you can use to kickstart your Django projects.

## Features

tbd

## Getting Started

Follow these steps to get the project up and running on your local machine:

1. **Clone the GitHub repository**
   ```bash
   git clone https://github.com/yourusername/API-ChatBot.git
   ```
2. **Create a Python virtual environment**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
3. **Install the requirements**
   ```bash
   pip install -r requirements.txt
   ```
4. **Make migrations**
   ```bash
   python manage.py makemigrations
   ```
5. **Migrate the database**
   ```bash
   python manage.py migrate
   ```
6. **Run the server**
   ```bash
   python manage.py runserver
   ```



## Recreate it simple steps

1. **Step 1:** Create a Full Fledged Django project using my cookie cutter django template
   ```bash
   gh repo create my-new-project --template MeJaM35/Django-CookieCutter --private --clone
   ```
   Don't forget to star this repo ;)

2. **Step 2:** Create a virtual environment

3. **Step 3:** Install the requirements
   ```bash
   pip install -r requirements.txt
   ```

4. **Step 4:** Make migrations and migrate
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

Now let's get started with Google OAuth integration

5. **Step 5:** Install new dependency
   ```bash
   pip install django-allauth
   ```

6. **Step 6:** Update `settings.py` getting it ready for allauth

   Go to `Project_dir/settings.py`:
   Locate `INSTALLED_APPS` and add this:
   ```python
   # MJ's dependencies
   'allauth',
   'allauth.account',
   'allauth.socialaccount',
   'allauth.socialaccount.providers.google',
   ```
   Locate `MIDDLEWARES` and add this:
   ```python
   'allauth.account.middleware.AccountMiddleware',
   ```
   Just below that add social provider for google and authentication backends
   ```python
   AUTHENTICATION_BACKENDS = (
       'allauth.account.auth_backends.AuthenticationBackend',
       'django.contrib.auth.backends.ModelBackend',
   )
   ACCOUNT_EMAIL_REQUIRED = True
   ACCOUNT_USERNAME_REQUIRED = False
   ACCOUNT_AUTHENTICATION_METHOD = 'email'
   ACCOUNT_EMAIL_VERIFICATION = 'optional'
   LOGIN_REDIRECT_URL = '/'
   SITE_ID = 2
   LOGOUT_REDIRECT_URL = '/'
   SOCIALACCOUNT_PROVIDERS = {
       'google': {
           'APP': {
               'client_id': 'your-client-id',
               'secret': 'your-client secret',
               'key': ''
           },
           'SCOPE': [
               'profile',
               'email',
           ],
           'AUTH_PARAMS': {
               'access_type': 'online',
           }
       }
   }
   ```
   Update the client ID & Client secret from the google developer console 
   Here's the link: [Google Cloud Console](https://console.cloud.google.com/welcome)
   Make sure you have logged in and create a new project 

   Locate `API & Services` and go to `OAuth Consent screen`:
   Fill out the details

   Then go to `Credentials`:

   Click on add new credentials:
   Add a name and 
   Add `http://127.0.0.1:8000/accounts/google/login/callback/` to authorized URI

   Now you get CLIENT ID & CLIENT SECRET save this and add it to social account providers.
   
   Locate `your_project/urls.py` and add 
   ```python
     from django.urls import path,include
   ```
   To `urlpatterns` add
   ```python
         path('accounts/', include('allauth.urls')),
         path('accounts/', include('allauth.socialaccount.urls')),
   ```
   Also add `templates/account` from this project
   I'm too lazy to add all three of these pages :p

7. **Step 7:** Now we do Open AI API integration:

   Go to [OpenAI API Keys](https://platform.openai.com/api-keys)

   Click on create new secret key 
   Save the details

   Now we install open ai dependency:
   ```bash
   pip install openai
   ```

   Go to `core/views.py`

   ```python
   from openai import OpenAI

   client = OpenAI(
       # Defaults to os.environ.get("OPENAI_API_KEY")
       api_key='your-api-secret'
   )
   ```
   Now we add a function that gets api response
   ```python
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
   ```
   And we pass the api response to index which I need you to update

   ```python
   def index(request):
       context = {}
       if request.method == "POST":
           prompt = request.POST.get('prompt')
           response = get_completion(prompt)
           context['response'] = response
       return render(request, 'core.html', context)
   ```
   Also create `templates/core.html` just copy it from this repo as well ;P

Voila, the app is ready!


Please replace `'your-api-secret'`, `'your-client-id'`, and `'your-client secret'` with your actual OpenAI API secret key and Google OAuth client ID and secret. Also, make sure to handle any exceptions that might occur during the API calls.

Now, you should be able to see the application running at `127.0.0.1:8000` in your web browser. Enjoy coding!

If you have any questions, feel free to reach out to me at `jamsutkarmeetpradeep@gmail.com`.


