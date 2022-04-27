from rest_framework import serializers
from .models import User



class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= User
        fields=['phone_number','username','first_name','last_name','password', 'role']
        
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

        if len(attrs['password']) < 8:
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
        role=validated_data['role']
    )    
        # user.set_password(validated_data['password'])
        user.save()

        return user
