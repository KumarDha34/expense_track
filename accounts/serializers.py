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

