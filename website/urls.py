from django.urls import path

from website import views


app_name = 'website'
urlpatterns = [
	path('', views.Homepage.as_view(), name='homepage'),
	path('about-wealthykate/', views.About.as_view(), name='about'),
]



