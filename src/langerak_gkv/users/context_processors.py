from .forms import LoginForm


def login(request):
    if not request.user.is_authenticated:
        return {"loginform": LoginForm()}
    return {}
