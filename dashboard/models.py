from django.db import models


class Income(models.Model):
    income_category = models.CharField(max_length=20)
    income_amount = models.DecimalField(max_digits=5, decimal_places=2)
    income_date = models.DateField(auto_now=True)


class Expense(models.Model):
    expense_category = models.CharField(max_length=20)
    expense_amount = models.DecimalField(max_digits=5, decimal_places=2)
    expense_date = models.DateField(auto_now=True)
