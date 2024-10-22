from rest_framework.views import APIView
from rest_framework import generics
from .models import Income,Expense,Category,BudgetGoal
from .serializers import IncomeSerializer,ExpenseSerializer,CategorySerializer,GoalSerializer
from rest_framework.permissions import IsAuthenticated
from openpyxl import Workbook
from django.db.models import Sum
from rest_framework.response import Response
from django.http import HttpResponse

class IncomeListView(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

class IncomeEnterView(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Income.objects.all()
    serializer_class=IncomeSerializer

class IncomeUpdateView(generics.UpdateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Income.objects.all()
    serializer_class=IncomeSerializer

class IncomeGetView(generics.RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Income.objects.all()
    serializer_class=IncomeSerializer

class IncomeDeleteView(generics.DestroyAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Income.objects.all()
    serializer_class=IncomeSerializer

class ExpenseListView(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseEnterView(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Expense.objects.all()
    serializer_class=ExpenseSerializer

class ExpenseUpdateView(generics.UpdateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Expense.objects.all()
    serializer_class=ExpenseSerializer

class ExpenseGetView(generics.RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Expense.objects.all()
    serializer_class=ExpenseSerializer

class ExpenseDeleteView(generics.DestroyAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Expense.objects.all()
    serializer_class=ExpenseSerializer

class CategoryListView(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Category.objects.all()
    serializer_class=CategorySerializer    

class CategoryEnterView(generics.CreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Category.objects.all()
    serializer_class=CategorySerializer  

class CategoryUpdateView(generics.UpdateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Category.objects.all()
    serializer_class=CategorySerializer  

class CategoryDeleteView(generics.DestroyAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Category.objects.all()
    serializer_class=CategorySerializer  

class GoalListView(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    queryset = BudgetGoal.objects.all()
    serializer_class = GoalSerializer

class GoalGetView(generics.RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    queryset = BudgetGoal.objects.all()
    serializer_class = GoalSerializer

class GoalUpdateView(generics.UpdateAPIView):
    permission_classes=[IsAuthenticated]
    queryset = BudgetGoal.objects.all()
    serializer_class = GoalSerializer

class GoalEnterView(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset = BudgetGoal.objects.all()
    serializer_class = GoalSerializer

class GoalDeleteView(generics.DestroyAPIView):
    permission_classes=[IsAuthenticated]
    queryset = BudgetGoal.objects.all()
    serializer_class = GoalSerializer

class SummaryReport(APIView):

    def get(self,request,user_id):
        Income_data=Income.objects.filter(user__id=user_id).aggregate(Sum('amount'))
        Expense_data=Expense.objects.filter(user__id=user_id).aggregate(Sum('amount'))
        data={
            'Income': Income_data,
            'expense': Expense_data
        }
        wb=Workbook()
        ws=wb.active    
        ws.title="Summary report"
        ws.append(['user_id,Income,Expense'])

        ws.append([
            user_id, 
            Income_data.get('total_income') or 0,  
            Expense_data.get('total_expense') or 0  
        ])

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="summary_report_user_{user_id}.xlsx"'

        wb.save(response)

        return response