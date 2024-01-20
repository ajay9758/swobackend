from .models import Product
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer

class GetAllProducts(APIView):
    authentication_classes=[]
    permission_classes=[]
    def get(self, request ):
        try:
            print("inside get method")
            data = Product.objects.all()
            ser = ProductSerializer(data, many=True)
            return Response({"data":ser.data} , status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"message":"Data not found"} , status=status.HTTP_400_BAD_REQUEST)
