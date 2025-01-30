from djoser.serializers import UserCreateSerializer

class MyUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password','first_name', 'last_name']