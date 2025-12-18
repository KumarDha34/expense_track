from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from .models import Expense
from .serializers import ExpenseSerializer


class ExpenseAPIView(APIView):
    permission_classes=[IsAuthenticated]
    
    @swagger_auto_schema(responses={200:ExpenseSerializer(many=True)})
    def get(self,request):
        expenses=Expense.objects.filter(user=request.user)
        serializer=ExpenseSerializer(expenses,many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=ExpenseSerializer)
    def post(self,request):
        serializer=ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                serializer.data,status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
   