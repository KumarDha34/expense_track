from django.db import models
from django.conf import settings
from accounts.models import User


class Expense(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="expenses")
    expense_amount=models.DecimalField(max_digits=10,decimal_places=2)
    item_purchased=models.CharField(max_length=255)
    date_of_purchase=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_purchased} - {self.expense_amount}"