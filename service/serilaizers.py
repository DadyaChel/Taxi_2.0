from statistics import mean
from rest_framework import serializers
from .models import Taxi, StatusDriver, Order, StatusType


class TaxiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Taxi
        fields = '__all__'
        read_only_fields = ['profile']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['profile', 'taxi']


class StatusDriverSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(write_only=True)

    class Meta:
        model = StatusDriver
        fields = '__all__'
        read_only_field = ['profile', 'taxi']


class StatusTypeSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField(source='get_status')

    class Meta:
        model = StatusType
        fields = '__all__'
        read_only_fields = ['profile']

    def validate_raiting(self, data):
        if data > 5:
            data = 5
        return data

    # def validate_raiting(self, data):
    #     d = list(data)
    #     data = mean(d)
    #     return data
