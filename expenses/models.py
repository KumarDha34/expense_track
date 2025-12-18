from django.db import models
from django.conf import settings

class Expense(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="expemses")
    expense_amount=models.DecimalField(max_digits=10,decimal_places=2)
    item_purchased=models.CharField(max_length=255)
    date_of_purchased=models.DateField()

    def __str__(self):
        return f"{self.item_purchased} - {self.expense_amount}"