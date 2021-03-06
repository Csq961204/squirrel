"""squirrel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import sightings.views as sightings_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('map', sightings_views.map, name='map'),
    path('sightings', sightings_views.sighting_list, name='sighting_list'),
    path('sightings/add', sightings_views.sighting_add, name='sighting_add'),
    path('sightings/stats', sightings_views.sighting_stats, name='sighting_stats'),
    path('sightings/<unique_squirrel_id>', sightings_views.sighting_update, name='sighting_update'),

    path('sightings/delete/<unique_squirrel_id>', sightings_views.sighting_delete, name='sighting_delete'),
]
