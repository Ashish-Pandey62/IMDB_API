from django.urls import path,include
from watchlist_app.api.views import WatchListAV,WatchListDetailAV,StreamPlatformVS,StreamPlatformAV,StreamPlatformDetailAV,ReviewList,ReviewDetail,ReviewCreate
from rest_framework.routers import DefaultRouter

 
 
# from watchlist_app.api.views import  movie_list,movie_details
router = DefaultRouter()
router.register('stream',StreamPlatformVS,basename='streamplatform')

urlpatterns = [
    path('list/',WatchListAV.as_view(),name='movie_list'),
    
    path('<int:pk>/',WatchListDetailAV.as_view(),name='movie_detail'),
    
    path('',include(router.urls)),  
    
    # stream list and stream detail are commented due to routers
    
    # path('stream/',StreamPlatformAV.as_view(),name='stream-list'),
    
    # path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name='stream_detail'),   
    
    # path('review/',ReviewList.as_view(),name='review_list') ,
    
    # path('review/<int:pk>',ReviewDetail.as_view(),name='review_detail'),
    
     path('<int:pk>/review-create/',ReviewCreate.as_view(),name='review_create'),
    
    path('<int:pk>/reviews/',ReviewList.as_view(),name='review_list'),
    
   
    
    path('review/<int:pk>/',ReviewDetail.as_view(),name='review_detail'),
  

    
]
 