from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic import FormView, ListView

from bands import models as band_models

from . import forms


class Dashboard(ListView):
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['band_list'] = band_models.Band.objects.all()
        return context


class SignUpView(FormView):
    form_class = forms.SignUpForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        req = self.request
        return req.GET.get('next', '/')

    def form_valid(self, form):
        data = form.cleaned_data
        # Create user
        u = User.objects.create_user(data['username'], password=data['password1'])
        u.save()
        # Add user to groups
        for group in data['groups']:
            u.groups.add(group)

        # TODO
        # Create any requested new bands

        # Add user as band manager of selected bands
        for band in data['bands']:
            band.manager = u
            band.save()

        # TODO
        # Don't just hand over bands because people asked for it.

        # Log user in
        login(self.request, u)

        return super().form_valid(form)
