from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer,LoginSerializer,ProfileSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from rest_framework.permissions import AllowAny,IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import authenticate



class RegisterAPIView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "message": "User Registered Successfully",
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            },
            status=status.HTTP_201_CREATED
        )
    
    
class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(
            request,
            username=email,   # maps to USERNAME_FIELD=email
            password=password
        )

        if not user:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        })


class ProfileAPIView(APIView):
    permission_classes=[IsAuthenticated]
    @swagger_auto_schema(responses={200:ProfileSerializer})
    def get(self,request):
        serializer=ProfileSerializer(request.user)
        return Response(serializer.data)