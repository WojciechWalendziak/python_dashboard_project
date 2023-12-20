from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_with_income_pivot, name='dashboard_income_with_pivot'),
    path('income_view', views.dashboard_with_income_pivot, name='dashboard_income_with_pivot'),
    path('expense_view', views.dashboard_with_expense_pivot, name='dashboard_expense_with_pivot'),
    path('income_data', views.income_pivot_data, name='income_pivot_data'),
    path('expense_data', views.expense_pivot_data, name='expense_pivot_data'),
]