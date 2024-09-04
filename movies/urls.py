from django.urls import path
from . import views

app_name = 'movies'
# url configuraion
#  By specifying a name, you can later refer to that URL by its name instead of hardcoding the path in multiple places.
urlpatterns = [
    path('', views.index, name='index'),

    # <movie_id> - is a URL parameter. When a user visits a URL like /movies/123,
    #  the value 123 (or any other value in place of <movie_id>) will be captured and passed to the
    #  view function as an argument.
    path('<int:movie_id>', views.detail, name='detail')

]
