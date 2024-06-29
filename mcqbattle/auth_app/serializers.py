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
    last_name = serializers.CharField(
        max_length = 30,
        required = True,
        error_messages={
            "required":"Email is Required",
            "blank":"Email is Required"
            "invalid":"Enter a Valid Email Address"
        }
    )
    
