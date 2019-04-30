import datetime

from decimal import Decimal

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


from django.db.models import Sum, Q, F

from .models import VaPayroll
from .forms import PayrollCreateForm
from .serializers import VaPayrollSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class PayrollView(LoginRequiredMixin, TemplateView):
    template_name = 'payroll/view_payroll.html'
    model = VaPayroll
    paginate_by = 15

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search')
        user = request.user.staffs.full_name
        current_month = datetime.date.today().month
        current_year = datetime.date.today().year
        payroll_list = VaPayroll.objects.all()
        payroll_data = payroll_list.filter(Q(virtual_assistant=user),
                                           Q(date__month=current_month),
                                           Q(status='APPROVED-BY-THE-MANAGER'))
        total_salary = VaPayroll.objects.filter(Q(virtual_assistant=user), 
                                                Q(date__month=current_month),
                                                Q(status='APPROVED-BY-THE-MANAGER'),
                                                Q(date__year=current_year)).aggregate(Sum('salary'))
        if search:
            payroll_data = payroll_list.filter(Q(virtual_assistant=user),
                                               Q(status='APPROVED-BY-THE-MANAGER'),
                                               Q(date__icontains=search))
            total_salary = VaPayroll.objects.filter(Q(virtual_assistant=user),
                                                    Q(status='APPROVED-BY-THE-MANAGER'),
                                                    Q(date__month=search),
                                                    Q(date__year=current_year)).aggregate(Sum('salary'))
        context = {
            'total_salary': total_salary,
            'payroll_data': payroll_data
        }
        return render(request, self.template_name, context)


class AddPayroll(CreateView):
    template_name = 'payroll/add_payroll.html'
    form_class = PayrollCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.virtual_assistant = self.request.user.staffs.full_name
        self.object.save()
        return HttpResponseRedirect(reverse_lazy('payroll:view_payroll'))


class PayrollViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = VaPayrollSerializer

    def get_queryset(self):
        current_month = datetime.date.today().month
        current_year = datetime.date.today().year
        queryset = VaPayroll.objects.filter(Q(virtual_assistant=self.request.user.staffs.full_name), 
                                            Q(date__month=current_month), 
                                            Q(date__year=current_year)).annotate(Sum('salary'))
        return queryset
