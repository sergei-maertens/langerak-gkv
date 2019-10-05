from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import RedirectView

from newsletter.models import Newsletter
from newsletter.views import UnsubscribeRequestView, UnsubscribeUserView

ACTION_MAPPING = {
    'subscribe': _('You have successfully subscribed to "{newsletter}"'),
    'update': _('You have successfully updated your subscription to "{newsletter}"'),
    'unsubscribe': _('You have successfully unsubscribed from "{newsletter}"'),
}


class ActionRedirectView(RedirectView):
    url = reverse_lazy('home')
    permanent = False

    def get(self, request, *args, **kwargs):
        response = super(ActionRedirectView, self).get(request, *args, **kwargs)
        newsletter = get_object_or_404(Newsletter, slug=kwargs.get('newsletter_slug'))
        message = ACTION_MAPPING.get(kwargs.get('action')).format(newsletter=newsletter.title)
        messages.success(request, message)
        return response


class RedirectUnsubscribeUserView(UnsubscribeUserView):
    def post(self, request, *args, **kwargs):
        super(RedirectUnsubscribeUserView, self).post(request, *args, **kwargs)
        return redirect('home')


class RedirectUnsubscribeRequestView(UnsubscribeRequestView):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            kwargs['confirm'] = self.confirm
            return RedirectUnsubscribeUserView.as_view()(request, *args, **kwargs)

        response = super(RedirectUnsubscribeRequestView, self).dispatch(request, *args, **kwargs)
        if self.request.method == 'POST':
            return redirect('home')
        return response
