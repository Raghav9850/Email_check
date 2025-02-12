# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
# from django.core.mail import EmailMessage
# from django.contrib import messages
# from .forms import LoginForm
# import csv
# from django.contrib.auth import logout


# def custom_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('send_email')
#             else:
#                 messages.error(request, 'Incorrect username or password.')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})


# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'Username already exists!')
#         else:
#             user = User.objects.create_user(username=username, password=password)
#             login(request, user)
#             messages.success(request, 'Account created successfully!')
#             return redirect('login')
#     return render(request, 'register.html')


# def send_email_view(request):
#     if request.method == 'POST':
#         subject = request.POST['subject']
#         content = request.POST['content']
#         file = request.FILES.get('file')
#         csv_file = request.FILES.get('csv_file')

#         try:
#             email_list = []
#             decoded_file = csv_file.read().decode('utf-8').splitlines()
#             reader = csv.reader(decoded_file)
#             for row in reader:
#                 email_list.append(row[0])  # First column assumed for emails

#             email = EmailMessage(subject, content, 'your_email@gmail.com', email_list)
#             if file:
#                 email.attach(file.name, file.read(), file.content_type)
#             email.send()

#             messages.success(request, 'Emails sent successfully!')
#         except Exception as e:
#             messages.error(request, f'Error sending emails: {e}')

#     return render(request, 'send_email.html')

# def custom_logout(request):
#     logout(request)
#     return redirect('login')



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib import messages
from .forms import LoginForm
import csv
from django.contrib.auth import logout


def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('send_email')
            else:
                messages.error(request, 'Incorrect username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    return render(request, 'register.html')


def send_email_view(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        content = request.POST['content']
        file = request.FILES.get('file')
        csv_file = request.FILES.get('csv_file')

        try:
            # Read email addresses from CSV
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file)
            email_list = [row[0] for row in reader]  # Assumes first column contains emails

            # Send individual emails
            for recipient in email_list:
                email = EmailMessage(subject, content, 'your_email@gmail.com', [recipient])
                if file:
                    email.attach(file.name, file.read(), file.content_type)
                email.send()

            messages.success(request, 'Emails sent successfully to all recipients!')
        except Exception as e:
            messages.error(request, f'Error sending emails: {e}')

    return render(request, 'send_email.html')


def custom_logout(request):
    logout(request)
    return redirect('login')
