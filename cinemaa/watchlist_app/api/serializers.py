from rest_framework import serializers
from watchlist_app.models import Movie

#  Now we are going to look at the use of ModelSerializer

class MovieSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        
        # custom serializer fields
        
        # len_name = serializers.SerializerMethodField()
        
        
        model = Movie
        fields = '__all__'
        
        # fields = ['id', 'name', 'description']
        # exclude = ['active']
        #  custom methods:
        # def get_len_name(self,object):
        #     length = len(object.name)
        #     return length
        
    # def validate(self,data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError('Title and description cannot be same')                                
    #     else:
    #         return data
        
    # def validate_name(self,value):
    #     if len(value)<2:
    #         raise serializers.ValidationError("name is too short")
    #     else:
    #         return value    


























# THIS IS THE EXAMPLE USING serializers.Serializer


# def name_length(value):
#     if len(value)<2:
#         raise serializers.ValidationError("Name is too short")
    

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     # field level validators can be applied with the help of validators
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self,instance, validated_data):
#          instance.name = validated_data.get('name',instance.name)
#          instance.description = validated_data.get('description',instance.description)
#          instance.active = validated_data.get('active',instance.active)
#          instance.save()
#          return instance
         
#     #  this section contains the use of validation functions
    
#     # let's validate the information of the object
    
#     def validate(self,data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Title and description cannot be same')                                
#         else:
#             return data
        
#     # field level validation
#     # def validate_name(self,value):
#     #     if len(value)<2:
#     #         raise serializers.ValidationError("name is too short")
#     #     else:
#     #         return value           