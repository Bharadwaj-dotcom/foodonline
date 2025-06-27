from django.shortcuts import redirect, render
from django.contrib import messages
from accounts.models import User
from .forms import UserForm

def registeruser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # ✅ Secure password saving
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
            )
            user.role = User.CUSTOMER
            user.save()

            messages.success(request, "Your account has been registered successfully.")
            return redirect('registeruser')
        else:
            print("Invalid form")
            print(form.errors)
            return render(request, 'accounts/registeruser.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'accounts/registeruser.html', {'form': form})
