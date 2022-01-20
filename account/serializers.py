from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from account.models import (
	Profile, UserLogin
)
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	group_types = SerializerMethodField()
	other_info = SerializerMethodField()
	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'group_types',
			'email',
			'other_info',
		)

	def get_group_types(self, obj):
		return [grp.name for grp in obj.groups.all()]

	def get_other_info(self, obj):
		profile = Profile.objects.get(fk_user=obj)
		return {
			'address': profile.address,
			'cp_no': profile.cp_no,
		}