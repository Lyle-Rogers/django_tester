from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view 
# from rest_framework import status
# from rest_framework.response import Response

from .models import Track

from .serializers import TrackSerializer

# @csrf_exempt
# @api_view(['GET'])
# def tracks(request):
#   if request.method == 'GET':
#     queryset = Track.objects.all()
#     serializer = TrackSerializer(queryset, many=True)
#     return Response(serializer.data)

@csrf_exempt
class TrackViewSet(viewsets.ModelViewSet):
  queryset = Track.objects.all()
  serializer_class = TrackSerializer 
