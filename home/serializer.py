from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id" , "first_name", "last_name","username", "country" , "street",
                  "phone","email"]

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)

    def validate(self, data):

        email = User.objects.filter(email= data.get('email')).first()
        if email:
            raise serializers.ValidationError("Email already exit")

        return data


                  

        
class CarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Car 
        fields = "__all__"

    def validate(self, data):
        np = Car.objects.filter(number_plate = data.get('number_plate')).first()

        if np:
            raise serializers.ValidationError("this vechile is own by other person")

        return data

    

class AdsSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only = True)

    class Meta:
        model = Ads 
        fields = "__all__"

    def validate(self, data):
        print(data.get('car'))
        if (data.get('car')==""):
            raise serializers.ValidationError("please enter a atleast 1 vehcile")

        return data
        
    def to_representation(self, instance):
        self.fields['car'] = CarSerializer(read_only =True)
        self.fields['user'] = UserSerializer(read_only =True)
        return super(AdsSerializer, self).to_representation(instance)