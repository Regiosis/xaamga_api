import json
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.http import HttpResponseNotFound, JsonResponse
from django.contrib.auth.hashers import make_password
from users.models import User
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response   import Response
from rest_framework import status


@api_view(["POST"])
def login_api(request): 
    user = authenticate(request, email=request.data['email'], password=request.data['password'])
    if user is None:
        return Response({"detail": 'Invalid email or password'}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)

    return Response([{
        'user_info': {
            'id': user.id,
            'name': user.name,
            'surname': user.surname,
            'email': user.email,
            'phone_number': user.phone_number,
            'username': user.username
        },
        'token': token.key
    }])


@api_view(["POST"])
def register_api(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError as e:
        return JsonResponse({'message': 'Error: Invalid JSON format'}, status=400)
    
    if isinstance(data, list):
        name = data[0].get("name")
        surname = data[0].get("surname")
        email = data[0].get("email")
        phone_number = data[0].get('phone_number')
        password = make_password(data[0].get('password'))
        contract_active = data[0].get('contract_active')
        profile_id = data[0].get('profile_id')
        # Validation  des données requises
        if not (name and surname and email and phone_number and password):
            return JsonResponse({ "Response" :{"status": 400, "message":"Missing required fields"}} , status=400)

        # Check if username or email already exists
        if User.objects.filter(phone_number=phone_number).exists() or User.objects.filter(email=email).exists():
            return JsonResponse({"Response": {"status": 409, "message": "Username or email already exists"}}, status=409)
        
        try:
            user = User.objects.create(surname=surname, name=name, phone_number=phone_number, email=email, password=password, contract_active=False if not(contract_active) else contract_active, profile_id=profile_id)
            user_data = {
                "name": user.name,
                "surname": user.surname,
                "phone_number": user.phone_number,
                "email": user.email,
            }
            data = [{ "Response" :{"message": "", "status": 200, "user": user_data}}]
            return JsonResponse(data, safe=False)
        except  User.DoesNotExist:
            data = [{ "Response" :{"message": "The request did not succeed, please check the data", "status": 400}}]
            return JsonResponse(data)
    return JsonResponse({ "Response" :{"message": "Please send a json in an array", "status": 400}})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def logout_api(request, *args, **kwargs):
    request.user.auth_token.delete()
    return JsonResponse({"Message": "Logout"})

        
