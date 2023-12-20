from django.http import JsonResponse
from django.shortcuts import render
from dashboard.models import Income
from dashboard.models import Expense
from django.core import serializers


def dashboard_with_income_pivot(request):
    return render(request, 'dashboard_income_with_pivot.html', {})


def dashboard_with_expense_pivot(request):
    return render(request, 'dashboard_expense_with_pivot.html', {})


def income_pivot_data(request):
    dataset = Income.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


def expense_pivot_data(request):
    dataset = Expense.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)