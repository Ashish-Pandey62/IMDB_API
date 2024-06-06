from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform,Review

#  Now we are going to look at the use of ModelSerializer

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Review
        fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:

        # custom serializer fields
        # len_name = serializers.SerializerMethodField()
        model = WatchList
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


class StreamPlatformSerializer(serializers.ModelSerializer):
    #  this is the use of nested serializers 
    #  need to look and understand in detail about this topic..
    # watchlist = WatchListSerializer(many = True,read_only = True)
    
    
    #  to return onlly the string name that we have ppassed in __str__
    # watchlist = serializers.StringRelatedField(many=True)
    
    # to return the links to that item
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='movie_details'
    )
    
    class Meta:
        model= StreamPlatform
        fields = '__all__'
 
