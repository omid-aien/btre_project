from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

# Create your views here.


def register(request):
    if request.method == 'POST':
        # get values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username is already existed!')
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'The Email is already existed!')
                    return redirect('accounts:register')
                else:
                    # looks good
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                    email=email, password=password)
                    # login after register
                    # auth.login(request=request, user=user)
                    # messages.success(request, 'You are noq logged in!')
                    # return redirect('pages:index')
                    user.save()
                    messages.success(request, 'You are registered successfully')
                    return redirect('accounts:login')
        else:
            messages.error(request, 'Tow passwords have been not matched!')
            return redirect('accounts:register')
    else:
        return render(request, template_name='accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request=request, user=user)
            messages.success(request, 'You are now logged in!')
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'Invalid credential!')
            return redirect('accounts:login')
    else:
        return render(request, template_name='accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('pages:index')


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': user_contacts
    }
    return render(request, template_name='accounts/dashboard.html', context=context)
