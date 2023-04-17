from rest_framework import serializers

from .models import CustomUser


class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "nickname",
            "is_singer",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        is_singer = validated_data.get("is_singer", False)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        if is_singer:
            # logic for payment if singer
            pass
        instance.save()
        return instance
