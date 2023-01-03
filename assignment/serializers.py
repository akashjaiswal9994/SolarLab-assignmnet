from rest_framework import serializers

class CountryList(serializers.Serializer):
    flag_link=serializers.CharField(max_length=500)
    capital=serializers.CharField(max_length=500)
    largest_city=serializers.CharField(max_length=400)
    official_languages=serializers.CharField(max_length=500)
    area_total=serializers.CharField(max_length=500)
    population=serializers.CharField(max_length=400)
    GDP_nominal=serializers.CharField(max_length=500)