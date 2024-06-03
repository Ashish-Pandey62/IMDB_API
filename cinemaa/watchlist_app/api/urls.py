from django.urls import path
from watchlist_app.api.views import WatchListAV,WatchListDetailAV,StreamPlatformAV,StreamPlatformDetailAV

 
 
# from watchlist_app.api.views import  movie_list,movie_details


urlpatterns = [
    path('list/',WatchListAV.as_view(),name='movie_list'),
    path('<int:pk>',WatchListDetailAV.as_view(),name='movie_details'),
    path('stream/',StreamPlatformAV.as_view(),name='stream'),
    path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name='stream_details'),

    
]
 