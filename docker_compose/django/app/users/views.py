from users.forms import UserRegisterForm, UserUpdateForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Account created successfully!")
            return redirect("login")
    else:
        form = UserRegisterForm()
    context = {"form": form}
    return render(request, "users/register.html", context)


@login_required
def profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Account has been updated")
            return redirect("profile")
    else:
        form = UserUpdateForm(instance=request.user)

    context = {"form": form}
    return render(request, "users/profile.html", context)
