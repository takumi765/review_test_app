from rest_framework import serializers

class TestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    que = serializers.CharField()
    ans = serializers.CharField()