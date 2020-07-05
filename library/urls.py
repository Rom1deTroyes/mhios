from django.urls import include, path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:storyId>/', views.watchStory, name='watchStory'),
    path('voteStory', views.voteStory, name='voteStory'),
    path('addStory/',views.addStory, name='addStory'),
    path('addStory/uploadStoryFile',views.uploadStoryFile, name='uploadStoryFile'),
    path('i18n/', include('django.conf.urls.i18n')),
]
