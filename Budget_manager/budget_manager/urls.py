from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import IncomeListView,IncomeEnterView,IncomeUpdateView,IncomeGetView,IncomeDeleteView,ExpenseListView,ExpenseEnterView,ExpenseUpdateView,ExpenseGetView,ExpenseDeleteView,CategoryListView,CategoryEnterView,CategoryUpdateView,CategoryDeleteView,GoalListView,GoalGetView,GoalEnterView,GoalDeleteView,GoalUpdateView,SummaryReport

urlpatterns=[

path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

path('income/',IncomeListView.as_view()),

path('income-enter/', IncomeEnterView.as_view()),

path('income-update/<int:pk>/',IncomeUpdateView.as_view()),

path('income-get/<int:pk>/',IncomeGetView.as_view()),

path('income-delete/<int:pk>/',IncomeDeleteView.as_view()),

path('Expense/',ExpenseListView.as_view()),

path('Expense-enter/', ExpenseEnterView.as_view()),

path('Expense-update/<int:pk>/',ExpenseUpdateView.as_view()),

path('Expense-get/<int:pk>/',ExpenseGetView.as_view()),

path('Expense-delete/<int:pk>/',ExpenseDeleteView.as_view()),

path('Category/',CategoryListView.as_view()),

path('Category-enter/', CategoryEnterView.as_view()),

path('Category-update/<int:pk>/',CategoryUpdateView.as_view()),

path('Category-delete/<int:pk>/',CategoryDeleteView.as_view()),

path('income/',IncomeListView.as_view()),

path('income-enter/', IncomeEnterView.as_view()),

path('income-update/<int:pk>/',IncomeUpdateView.as_view()),

path('income-get/<int:pk>/',IncomeGetView.as_view()),

path('income-delete/<int:pk>/',IncomeDeleteView.as_view()),

path('goal/',GoalListView.as_view()),

path('goal-enter/', GoalEnterView.as_view()),

path('goal-update/<int:pk>/',GoalUpdateView.as_view()),

path('goal-get/<int:pk>/',GoalGetView.as_view()),

path('goal-delete/<int:pk>/',GoalDeleteView.as_view()),

path('report/<int:user_id>/', SummaryReport.as_view())


]

