from rest_framework import serializers

#creating serializers

class OptionSerializer(serializers.Serializer):
    body = serializers.CharField(max_length=1000)
    is_correct = serializers.BooleanField()
    
    
#main mcq serializer
class MCQSerializer(serializers.Serializer):   
    id = serializers.UUIDField(max_length = 1000),
    body = serializers.TextField(max_length=2000),
    explanation = serializers.CharField(max_length=2000),
    # options is class data type(contains body and boolean value)
    options = OptionSerializer(many=True)
