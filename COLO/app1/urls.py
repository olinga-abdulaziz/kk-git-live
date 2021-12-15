from django.urls import path
from . import views

urlpatterns = [
    path('kk-home',views.HomeView.as_view(),name='home'),
    path('category-wedding-photos',views.WeddingView.as_view(),name='wedding'),
    path('category-commercia-photos',views.CommerciaView.as_view(),name='commercia'),
    path('category-corporate-photos',views.CorporateView.as_view(),name='corporate'),
    path('category-events-photos',views.EventsView.as_view(),name='events'),
    path('category-fasion-photos',views.FasionView.as_view(),name='fasion'),
    path('category-potraits-photos',views.PotraitsView.as_view(),name='potraits'),
    path('upload-photo-photos/',views.AddPostView.as_view(),name='post')
]