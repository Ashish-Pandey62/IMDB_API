from rest_framework.response import Response
from watchlist_app.models import WatchList,StreamPlatform,Review
from watchlist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
# from rest_framework import mixins
from rest_framework import generics,viewsets
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from watchlist_app.api.permissions import AdminOrReadOnly,ReviewUserorReadOnly


#  USING GENERIVC VIEWS TO GET THE COMPLETE LIST THE DETAILS OF REVIEWS

class ReviewCreate(generics.CreateAPIView):
    

    def get_queryset(self):
        return Review.objects.all()
    
    
    serializer_class = ReviewSerializer
    #  here we need to override the default 
    # queryset because i need to pass the id of specific movie 
    
    
    def perform_create(self,serializer):
        pk = self.kwargs['pk']
        watchlist = WatchList.objects.get(pk=pk)
        
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist,review_user = review_user)
        
        if review_queryset.exists():
            raise ValidationError("You are not allowed to post multiple reviews for a singl Watchlist.")
        
        serializer.save(watchlist=watchlist,review_user=review_user)
      


class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all() note: by default they are accessing all the movies but we need the review for the particular selected movie,
    # so we need to override this method to get the review for the selected movie 
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
    
    
    serializer_class = ReviewSerializer
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    
    
    permission_clasees = [ReviewUserorReadOnly] # this is an example of custom permission classes

    # permission_classes = [IsAuthenticated]  # this is an example of object level permission 
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer    


#   USING MIXINS TO GET THE COMPLETE LIST AND THE DETAILS OF REVIEWS

# class ReviewDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
#   queryset = Review.objects.all()
#   serializer_class = ReviewSerializer
  
#   def get(self, request, *args, **kwargs):
#       return self.retrieve(request, *args, **kwargs)

# class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all() 
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# #### LET'S LEARN ABOUT MODEL VIEWSET ###

class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

    
    #   LET'S LEARN ABOUT THE VIEWSET :

# class StreamPlatformVS(viewsets.ViewSet):
    
#     def list(self,request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset,many=True) 
#         return Response(serializer.data)
    
#     def retrieve(self,request,pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset,pk=pk)
#         serializer = StreamPlatformSerializer(watchlist)
#         return Response(serializer.data)
    

#     def create(self,request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request, pk):
#         try:
#             stream = StreamPlatform.objects.get(pk=pk)
#         except StreamPlatform.DoesNotExist:
#             return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

#         stream.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class StreamPlatformAV(APIView):
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform,many=True,context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class StreamPlatformDetailAV(APIView):

    def get(self, request, pk):
        try:
            stream = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(stream,context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            stream = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(stream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            stream = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        stream.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class WatchListAV(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WatchListDetailAV(APIView):
    

    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
