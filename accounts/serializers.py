from django.contrib.auth import get_user_model
from rest_framework import serializers, validators
from accounts.models import Profile, User

class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    surname = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=255)
    contract_active = serializers.BooleanField(default=False)
    #profile_id =  serializers.ForeignKey(Profile, on_delete=serializers.CASCADE, null=True)
    class Meta(object):
        model = get_user_model()
        fields = ['name', 'surname', 'username', 'password', 'email', 'phone_number']
        extra_kwargs = {
            "password": {"write_only": True},
            "name": {"required": True},
            "email": {
                "required": True, 
                "validators": [
                    validators.UniqueValidator(
                        queryset=User.objects.all(), 
                        message="This email address is already"
                    )
                ]
            }
        }
        
   
    def create(self, validated_data):
        password = validated_data.get( 'password')
        user = User.objects.create(
            name=validated_data['name'],
            surname=validated_data['surname'] ,
            username=validated_data['username'],
            phone_number=validated_data['phone_number'],
            password =password,
        )
        return user



# class CustomRegisterSerializer(RegisterSerializer):
#     name = serializers.CharField(max_length=255)
#     surname = serializers.CharField(max_length=255)
#     phone_number = serializers.CharField(max_length=255)
#     contract_active = serializers.BooleanField(default=False)
#     profile_id =  serializers.ForeignKey(Profile, on_delete=serializers.CASCADE, null=True)
#     class Meta(object):
#         model = get_user_model()
#         fields = ['name', 'surname', 'username', 'password', 'email', 'phone_number']

