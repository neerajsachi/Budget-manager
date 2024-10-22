# serializers.py
from rest_framework import serializers
from .models import Income,Expense,Category,BudgetGoal

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'  # Include all fields or specify them individually

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model=BudgetGoal
        fields='__all__'