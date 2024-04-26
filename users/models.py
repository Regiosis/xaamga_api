# from django.conf import settings
# from django.db import models
# from events.models import Event
# from django.contrib.auth.models import BaseUserManager, AbstractUser


# class Profile(models.Model):
#     profileTypes = [
#         ('Owner', 'Owner'),
#         ('Super', 'Supervisor'),
#         ('Admin', 'Administrator'),
#         ('Talent', 'Talent'),
#         ('Client', 'Client'),
#     ]

#     id = models.BigAutoField(primary_key=True)
#     profile_name = models.CharField(max_length=255, choices=profileTypes)
#     profile_description = models.TextField(null=True, default="")

#     class Meta:
#         db_table = 'profiles'
#         verbose_name = ("profiles")
#         verbose_name_plural = ("profiles")

#     def __str__(self):
#         return (f"{self.profile_name}"
#             f"{self.profile_description}")


# class UserInfoManager(BaseUserManager):
#     def create_user(self, name, surname, username, email, phone_number, password=None, is_admin=False, is_staff=False, is_active=True):
#         if not email:
#             raise ValueError("Users must have an email address")

#         user = self.model(
#             email=self.normalize_email(email),
#             name = name,
#             surname = surname,
#             username = username,
#             phone_number=phone_number,
#         )

#         user.set_password(password)
#         user.admin = is_admin
#         user.staff = is_staff
#         user.active = is_active
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, name, surname, username, email, phone_number, password=None, **extra_fields):
#         user = self.create_user(
#             email = email,
#             password = password,
#             name = name,
#             surname = surname,
#             phone_number = phone_number,
#             username = username,
#             is_staff= True,
#             is_admin = True
#         )
#         user.is_admin = True,
#         user.is_staff= True,
#         user.is_active= True,
#         user.is_superuser = True,
#         user.save(using=self._db)
#         return user


# class User(AbstractUser):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     surname = models.CharField(max_length=255)
#     username = models.CharField(max_length=255, default="")
#     phone_number = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)
#     contract_active = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     profile_id =  models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

#     REQUIRED_FIELDS = ["name", "surname", "username", "phone_number", "password"]
#     USERNAME_FIELD = "email"
#     list_display = ('name', 'surname', 'phone_number', 'email', 'username', 'profile_id', 'contract_active')
    
#     objects = UserInfoManager()

#     class Meta:
#         db_table = 'users_info'
#         verbose_name = ("users_info")
#         verbose_name_plural = ("users_info")

#     # def __str__(self):
#     #     return (f"{self.name} "
#     #         f"{self.surname}"
#     #         f"{self.id}"
#     #         f"{self.email}"
#     #         f"{self.contract_active}"
#     #         f"{self.password}"
#     #         f"{self.phone_number}"
#     #     )
    

# class LoginInfo(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     email = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=255, default="")
#     password = models.CharField(max_length=255)
#     user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     event_id = models.ForeignKey(Event, on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'logins_info'
#         verbose_name = ("logins_info")
#         verbose_name_plural = ("logins_info")
        
#     def __str__(self):
#         return (f"{self.id} "
#             f"{self.email}"
#             f"{self.phone_number}"
#             f"{self.user_id}"
#             f"{self.event_id}"
#             f"{self.password}"
#         )
