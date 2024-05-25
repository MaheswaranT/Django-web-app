from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Destination
from .serializers import DestinationSerializer
from accounts.models import Account
import requests

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

@api_view(['POST'])
def incoming_data(request):
    token = request.headers.get('CL-X-TOKEN')
    if not token:
        return Response({"error": "Un Authenticate"}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        account = Account.objects.get(app_secret_token=token)
    except Account.DoesNotExist:
        return Response({"error": "Un Authenticate"}, status=status.HTTP_401_UNAUTHORIZED)

    data = request.data

    if request.method == 'POST' and not isinstance(data, dict):
        return Response({"error": "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)

    destinations = Destination.objects.filter(account=account)

    for destination in destinations:
        headers = destination.headers
        url = destination.url
        method = destination.http_method

        if method == 'GET':
            response = requests.get(url, headers=headers, params=data)
        elif method == 'POST':
            response = requests.post(url, headers=headers, json=data)
        elif method == 'PUT':
            response = requests.put(url, headers=headers, json=data)
        
        # Handle the response if needed

    return Response({"message": "Data sent to all destinations"}, status=status.HTTP_200_OK)

