import datetime
import json
from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.urls import reverse_lazy
from django.http import JsonResponse

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q

from client.models import Client
from jobrequest.models import JobRequest


class LoginView(AuthenticationForm, View):
    template_name = 'users/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('users:home'))
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None and password is not None:
            login(request, user)
            user.last_login = datetime.datetime.now()
            user.save(update_fields=['last_login'])
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect(reverse_lazy('users:home'))
        else:
            messages.warning(request, 'Username or password is incorrect. Or maybe account is inactive')
        return render(request, self.template_name)


class LogoutView(View):

    def get(self, request):
        logout(request)
        messages.success(request, 'Your account has been logout successfully.')
        return redirect(reverse_lazy('users:login'))


class HomeView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'base.html'
    login_url = 'users:login'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()

    def get_queryset(self):
        user = self.request.user
        queryset = Client.objects.filter(
            senior_manager__name=user, status="Active")
        return queryset


class VaProfile(LoginRequiredMixin, ListView):
    template_name = 'users/profile.html'

    def get(self, request):
        return render(request, self.template_name)


def client_status_data(request):
    dataset = Client.objects \
        .values('status') \
        .exclude(status='') \
        .annotate(total=Count('status'))

    status_name = dict()
    for status_tuple in Client.STATUS_CHOICES:
        status_name[status_tuple[0]] = status_tuple[1]

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Client information total count on Active/Inactive tasks'},
        'series': [{
            'name': 'Total count',
            'data': list(map(lambda row: {'name': status_name[row['status']], 'y': row['total']}, dataset))
        }]
    }

    return JsonResponse(chart)


def job_request_status_data(request):
    dataset = JobRequest.objects \
        .values('status') \
        .exclude(status='') \
        .annotate(total=Count('status'))

    status_name = dict()
    for status_tuple in JobRequest.JOB_STATUS_CHOICES:
        status_name[status_tuple[0]] = status_tuple[1]

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Job Request information total count on different status'},
        'series': [{
            'name': 'Total count',
            'data': list(map(lambda row: {'name': status_name[row['status']], 'y': row['total']}, dataset))
        }]
    }

    return JsonResponse(chart)


# def job_request_status_data(request):
#     dataset = JobRequest.objects \
#         .values('status') \
#         .annotate(complete_count=Count('status', filter=Q(status='Complete')),
#                   in_progress_count=Count('status', filter=Q(status='In Progress')),
#                   for_final_review_count=Count('status', filter=Q(status='For Final Review')),
#                   job_request_sent_to_va_count=Count('status', filter=Q(status='Job Request Sent to VA'))) \
#         .order_by('status')
#
#     categories = list()
#     complete_series_data = list()
#     in_progress_series_data = list()
#     for_final_review_series_data = list()
#     job_request_sent_to_va_series_data = list()
#
#     for entry in dataset:
#         categories.append('%s Status' % entry['status'])
#         complete_series_data.append(entry['complete_count'])
#         in_progress_series_data.append(entry['in_progress_count'])
#         for_final_review_series_data.append(entry['for_final_review_count'])
#         job_request_sent_to_va_series_data.append(entry['job_request_sent_to_va_count'])
#
#     complete_series = {
#         'name': 'Complete',
#         'data': complete_series_data,
#         'color': 'green'
#     }
#
#     in_progress_series = {
#         'name': 'In Progress',
#         'data': in_progress_series_data,
#         'color': 'blue'
#     }
#
#     for_final_review_series = {
#         'name': 'For Final Review',
#         'data': for_final_review_series_data,
#         'color': 'yellow'
#     }
#
#     job_request_sent_via_series = {
#         'name': 'Job Request Sent to Va',
#         'data': job_request_sent_to_va_series_data,
#         'color': 'red'
#     }
#
#     chart = {
#         'chart': {'type': 'column'},
#         'title': {'text': 'Job request status'},
#         'xAxis': {'categories': categories},
#         'series': [complete_series, in_progress_series, for_final_review_series, job_request_sent_via_series]
#     }
#
#     dump = json.dumps(chart)
#
#     return render(request, 'base.html', {'chart': dump})
