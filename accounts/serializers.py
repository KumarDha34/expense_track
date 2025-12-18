from rest_framework import serializers
from .models import User
from expenses.models import Expense
from django.db.models import Sum


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'full_name',
            'email',
            'password',
            'address',
            'age',
            'monthly_income'
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(
            password=password,
            **validated_data
        )
        return user

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True)
    


class ProfileSerializer(serializers.ModelSerializer):
    total_expenses = serializers.SerializerMethodField()
    remaining_balance = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "full_name",
            "email",
            "address",
            "age",
            "monthly_income",
            "total_expenses",
            "remaining_balance"
        ]

    def get_total_expenses(self, obj):
        total=obj.expenses.aggregate(total=Sum("expense_amount"))["total"]
        return total or 0
    
    def get_remaining_balance(self, obj):
        return obj.monthly_income - self.get_total_expenses(obj)