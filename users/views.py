# import json
# import os
# from django.contrib.auth import authenticate
# from django.db import DatabaseError
# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import permission_classes, authentication_classes, api_view
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
# from django.http import HttpResponseNotFound, JsonResponse
# from django.contrib.auth.hashers import make_password
# from accounts.models import User
# from rest_framework.authtoken.serializers import AuthTokenSerializer
# from rest_framework.response   import Response
# from rest_framework import status
# import requests

# BASE_API_AUTH_URL = os.getenv('BASE_API_URL')+'/v1/auth'


# @api_view(["POST"])
# def login_with_email(request): 
#     try:
#         data = json.loads(request.body)
#         username = data[0].get("username")
#         email = data[0].get("email")
#         password = data[0].get('password')
#         if not all([email, password]):
#             return Response({"Response": {"status": 400, "message": "Missing required fields"}}, status=400)
        
#         data_request = {
#             #"username": username,
#             "email": email,
#             "password": password,
#         }

#         headers = {"Content-Type": "application/json", "Accept": "application/json"}
#         response = requests.post(
#             "http://127.0.0.1:8000/api/v1/auth/login/",
#             json=data_request,
#             headers=headers,
#         )
#         if response.status_code == 200:
#             return Response({"Response": {"status": response.status_code, "message": response.json()}}, status=201)
#         else:
#             return Response({"Response": {"status": response.status_code, "message": response.json()}}, status=201)
#     except json.JSONDecodeError as e:
#         return Response({'message': 'Error: Invalid JSON format'}, status=400)


# @api_view(["POST"])
# def register_with_email(request):
#     try:
#         data = json.loads(request.body)
#         name, surname, username, email, phone_number, profile_id = data[0].get("name"), data[0].get("surname"), data[0].get("username"), data[0].get("email"), data[0].get("phone_number"), data[0].get("profile_id")
#         password = data[0].get('password')
#         contract_active = data[0].get('contract_active', False)
        
#         if not all([name, surname, email, phone_number, password]):
#             return Response({"Response": {"status": 400, "message": "Missing required fields"}}, status=400)
        
#         data_request = {
#             "username": username,
#             "email": email,
#             "password1": password,
#             "password2": password,
#         }
#         headers = {"Content-Type": "application/json", "Accept": "application/json"}
#         response = requests.post(BASE_API_AUTH_URL+"/registration/", json=data_request, headers=headers)

#         if response.status_code == 201:
#             if User.objects.filter(email=email).exists():
#                 try:
#                     user = User.objects.get(email=email)
#                     user.name = name
#                     user.surname = surname
#                     user.phone_number = phone_number
#                     user.profile_id = profile_id
#                     user.contract_active = contract_active if contract_active is not None else False
#                     user.save()
#                 except DatabaseError as e:
#                     return Response({"message": str(e)})
#             else:
#                 return Response({"status": response.status_code, "message" : "User with email " + email + " not created on remote server."})
#             return Response({"Response": {"status": response.status_code, "message": response.json()}}, status=201)
#         else:
#             return  Response({"Response": {"status": response.status_code, "message": response.json()}})
#     except json.JSONDecodeError as e:
#         return Response({'message': 'Error: Invalid JSON format'}, status=400) 


# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
# def logout(request, *args, **kwargs):
#     request.user.auth_token.delete()
#     return JsonResponse({"Message": "Successful disconnection"})


# @api_view(["POST"])
# def password_reset_with_email(request, *args, **kwargs):
#     try:
#         data = json.loads(request.body)
#         email = data[0].get('email')

#         print(email)
#         if not email:
#             return Response({"Response": {"status": response.status_code, "message": "Email is required"}})
#         else:
#             if User.objects.filter(email=email).exists():
#                 headers = {"Content-Type": "application/json", "Accept": "application/json"}
#                 response = requests.post(BASE_API_AUTH_URL+"/password/reset/", json={"email": email}, headers=headers)
#                 if response.status_code == 200:
#                     return Response({"Response": {"status": response.status_code, "message": response.json()}})
#                 return Response({"Response": {"status": response.status_code, "message": response.json()}})
#             else:
#                 return Response({"Response": {"status": 404, "message": "User with email " + email + " not found"}})
#     except json.JSONDecodeError as e:
#         return Response({'message': 'Error: Invalid JSON format'}, status=400)


# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
# @api_view(["POST"])
# def password_change(request, *args, **kwargs):
#     try:
#         data = json.loads(request.body)
#         old_password, new_password1, new_password2 = data[0].get('old_password'), data[0].get('new_password'), data[0].get('new_password_confirmation')
#         if not all([old_password, new_password1, new_password2]):
#             return Response({"Response": {"status": 400, "message": "All fields are required"}})
#         data_request  = {
#             "old_password": old_password,
#             "new_password1": new_password1,
#             "new_password2": new_password2
#         }
#         token = request.user.auth_token.key
#         headers = {"Content-Type": "application/json", "Accept": "application/json", 'Authorization': 'Token '+token}
#         response = requests.post(BASE_API_AUTH_URL+"/password/change/", json=data_request, headers=headers)
#         if response.status_code == 200:
#             return Response({"Response": {"status": response.status_code, "message": response.json()}})
#         return Response({"Response": {"status": response.status_code, "message": response.json()}})
#     except json.JSONDecodeError as e:
#         return Response({'message': 'Error: Invalid JSON format'}, status=400)
