from django.urls import path
from profiles import views

urlpatterns = [
  path('profiles/', view=views.ProfileList.as_view())
]