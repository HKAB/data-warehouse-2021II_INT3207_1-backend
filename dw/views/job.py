from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import ParseError

from dw.models.job import Job
from dw.services.job import get_job, list_job

class JobGetView(APIView):
    class InputSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=True)

        class Meta:
            ref_name = 'JobGetIn'
            fields = ['id']
    
    class OutputSerializer(serializers.ModelSerializer):

        class Meta:
            model = Job
            ref_name = 'JobGetOut'
            fields = '__all__'
            
    
    permission_classes = [AllowAny]
    authentication_classes = []

    @swagger_auto_schema(query_serializer=InputSerializer, responses={200: OutputSerializer()})
    def get(self, request):
        serializer = self.InputSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        result = get_job(**serializer.validated_data)
        return Response(self.OutputSerializer(result).data, status=status.HTTP_200_OK)

class JobListView(APIView):
    class InputSerializer(serializers.Serializer):
        cat = serializers.CharField(required=True)

        class Meta:
            ref_name = 'JobListIn'
            fields = ['cat']
    
    class OutputSerializer(serializers.ModelSerializer):

        class Meta:
            model = Job
            ref_name = 'JobListOut'
            fields = '__all__'
    
    permission_classes = [AllowAny]
    authentication_classes = []
    
    @swagger_auto_schema(query_serializer=InputSerializer, responses={200: OutputSerializer(many=True)})
    def get(self, request):
        serializer = self.InputSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        result = list_job(**serializer.validated_data)
        return Response(self.OutputSerializer(result, many=True).data, status=status.HTTP_200_OK)
