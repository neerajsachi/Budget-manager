from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user=models.OneToOneField(User,max_length=100, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    category_choices=[('INCOME','Income'),('EXPENSE','Expense')]
    name=models.CharField(max_length=50)
    category_type=models.CharField(max_length=7, choices=category_choices, default='INCOME')
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Income(models.Model):
    amount=models.DecimalField(max_digits=12,decimal_places=2,validators=[MinValueValidator(Decimal('0.01'))])
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    date=models.DateField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)


class Expense(models.Model):
    amount=models.DecimalField(max_digits=12,decimal_places=2,validators=[MinValueValidator(Decimal('0.01'))])
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=100,blank=True,null=True)
    date=models.DateField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)

class BudgetGoal(models.Model):
    goal_amount = models.DecimalField(max_digits=12,decimal_places=2,validators=[MinValueValidator(Decimal('0.01'))])
    date=models.DateField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)