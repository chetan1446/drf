from django.urls import path
from .views import show_movies,show_movies_old,MoviesAPIView,ShowUsersAPIView,ShowMoviesAPIView
urlpatterns = [
    path('show/<int:movie_id>/', show_movies),
    path('show/', show_movies),
    path('show-old/', show_movies_old),
    path('api-view/',MoviesAPIView.as_view()),
    path('list-view/',ShowUsersAPIView.as_view()),
    path('list-movie/',ShowMoviesAPIView.as_view())
]