from rest_framework import serializers


class RegistrationSerializer(serializers.Serializer):
    first_name = serializers.CharField(
        max_length = 30,
        required = True,
        error_messages={
            "required":"First Name is Required",
            "blank":"First Name is Required"
        }
    )
    last_name = serializers.CharField(
        max_length = 30,
        required = True,
        error_messages={
            "required":"Last Name is Required",
            "blank":"Last Name is Required"
        }
    )
    email = serializers.EmailField(
        max_length = 30,
        required = True,
        error_messages={
            "required":"Email is Required",
            "blank":"Email is Required",
            "invalid":"Enter a Valid Email Address"
        }
    )
    password = serializers.CharField(
        write_only =True,
        required = True,
        error_messages={
            "required":"Email is Required",
            "blank":"Email is Required",
        }
    )

    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        write_only =True,
        required = True,
        error_messages={
            "required":"Email is Required",
            "blank":"Email is Required",
            "invalid":"Enter a Valid Email Address"
        }
    )
    password = serializers.CharField(
        max_length = 30,
        required = True,
        error_messages={
            "required":"Email is Required",
            "blank":"Email is Required",
        }
    )
