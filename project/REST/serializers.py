from rest_framework import serializers
from common.models import User,Book,Person,Student

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        fileds = ('urls','username','password')

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        fileds = ('url','b_name','b_price')

class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    p_name = serializers.CharField(max_length = 32)
    p_age = serializers.IntegerField(default=1)
    p_sex = serializers.BooleanField(default=False)

    def create(self,validated_data):
        return Person.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.p_name = validated_data.get('p_name',instance.p_name)
        instance.p_age = validated_data.get('p_age',instance.p_age)
        instance.p_sex = validated_data.get('p_sex',instance.p_sex)
        instance.save()
        return instance

class StudentSerializer(serializers.ModelSerializer):
    def update(self,instance,validated_data):
        instance.s_name = validated_data.get('s_name',instance.s_name)
        instance.s_age = validated_data.get('s_age',instance.s_age)
        instance.save()
        return instance
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ('s_name','s_age')

