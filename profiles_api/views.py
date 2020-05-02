from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.renderers import BrowsableAPIRenderer

from profiles_api import serializers


class HelloApiView(APIView):
    """Test Api View"""
    serializers_class = serializers.HelloSerializer
    # renderer_classes = [BrowsableAPIRenderer]

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the mos control over your application logic',
            'Is mapped manually to URLs']

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating and object"""
        return Response({'method': 'PUT'})

    def path(self, request, pk=None):
        """Handle a partial updateof an object"""
        return Response({"rmethod": 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
