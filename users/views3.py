
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.serializers import UserSerializer


def login_api():
    pass

# def register_api():
#     pass

@api_view(['POST'])
def register_api(request):
    serializer = UserSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
    except ValidationError as e:
        return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

    user = serializer.save()
    token = authenticate(request=request, username=user.email, password=serializer.validated_data['password'])

    if token:
        data = {
            'user': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'address': user.address,
            'token': token,
        }
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        return Response(_('Impossible de se connecter.'), status=status.HTTP_400_BAD_REQUEST)

def logout_api():
    pass