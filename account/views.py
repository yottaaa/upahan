from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.serializers import AuthTokenSerializer

from django.contrib.auth import login
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from knox.views import LoginView as KnoxLoginView

from account.models import (
	Profile, UserLogin,
)
from upahan.service import (
	validate_required_fields,
	validate_required_data,
	validate_phonenum,
)

# Create your views here.
@api_view(['POST'])
def register(request):
	if request.method == 'POST':
		try:
			validate_required_fields(request.data,(
				'username','first_name','last_name','password',
				'email', 'phone_num', 'group',
			))
			validate_required_data(request.data, (
				'username','first_name','last_name','password',
				'email', 'phone_num', 'group',
			))
			if User.objects.filter(username=request.data['username']).exists():
				raise Exception("Username is already taken")

			if validate_phonenum(request.data.get('phone_num')) == False:
				raise Exception('Invalid phone number')

			validate_email(request.data.get('email'))

			_group = Group.objects.get_or_create(name=request.data.get('group'))
			_user = User.objects.create(
				username=request.data.get('username'),
				password=make_password(request.data.get('password')),
				first_name=request.data.get('first_name'),
				last_name=request.data.get('last_name'),
				email=request.data.get('email'),
				group=_group,
			)
			Profile.objects.create(
				fk_user=_user,
				cp_no=request.data.get('phone_num')
			)
		except ValidationError as ve:
			return Response({"detail":str(ve)},status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({"detail":str(e)}, status=status.HTTP_400_BAD_REQUEST)

		return Response({"detail":"Successfully created"})

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def get_post_response_data(self, request, token, instance):
        UserSerializer = self.get_user_serializer_class()

        data = {
            'expiry': self.format_expiry_datetime(instance.expiry),
            'token': token
        }
        if UserSerializer is not None:
            data["user"] = UserSerializer(
                request.user,
                context=self.get_context()
            ).data
        return data

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        login(request, user)
        userloginlog = UserLogin.objects.create(
            fk_user=user
        )
        userloginlog.save()

        return super(LoginAPI, self).post(request, format=None)