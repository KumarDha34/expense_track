from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields=['id','expense_amount','item_purchased','date_of_purchase','created_at']
        read_only_fields=['id']