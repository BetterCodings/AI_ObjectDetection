from rest_framework import  serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    # image=serializers.ImageField(use_url=True)
    class Meta:
        model = Account
        fields = ("name",'ID', 'passwd')
