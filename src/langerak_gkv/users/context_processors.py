from .forms import LoginForm


def login(request):
    if not request.user.is_authenticated:
        return {"login_form": LoginForm()}
    return {}
