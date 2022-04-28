from rest_framework import serializers
from .models import User, NextOfkin



class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= User
        fields=['phone_number','username','first_name','last_name','password', 'role', 'department', 'address', 'starting_date', 'salary']
        
        extra_kwargs = {
        'password': {'write_only': True}
                }

        
     # making the phone_number field unique
    def validate(self, attrs):
        print(attrs['password'])
        if len(attrs['phone_number']) == 0:
            raise serializers.ValidationError(
                {
                    'status': "failure",
                    'detail': 'you must supply a phone_number'
                })
        if User.objects.filter(phone_number=attrs['phone_number']).exists():
            print(78, 'phone_number')
            raise serializers.ValidationError(
                {
                    'status': "failure",
                    'detail': 'phone_number exist'
                }
            )

        if len(attrs['password']) < 8 or len(attrs['phone_number']) < 10:
            raise serializers.ValidationError(
                {
                    'status': 'failure',
                    'detail': 'password must be 8 characters or more'}
            )
        return super().validate(attrs)
    
    def create(self, validated_data, *args, **kwargs):
        user = User.objects.create(
        phone_number = validated_data['phone_number'],
        username = validated_data['username'],
        first_name = validated_data['first_name'],
        last_name = validated_data['last_name'],
        password=validated_data['password'],
        role=validated_data['role'],
        department=validated_data['department'],
        address=validated_data['address'],
        starting_date=validated_data['starting_date'],
        salary=validated_data['salary']
        
    )    
        user.save()

        return user


class NextOfkinSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NextOfkin
        fields=['user', 'first_name', 'last_name', 'phone_number']
        
    def create(self,validated_data, *args, **kwargs):
        kin = NextOfkin.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number']
        )
        kin.save()
        return kin
            