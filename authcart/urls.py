from django.urls import path
from authcart import views

urlpatterns =[
    path('signup/',views.signup,name='signup'),
    path('login/',views.handlelogin,name='handlelogin'),
    path('logout/',views.handlelogout,name='handlelogout'),
    #path('activate.<uid64>/<token>',views.ActivateAccountView_as_view(),name='activate')
    path('activate/<uidb64>/<token>/', views.ActivateAccountView.as_view(), name='activate'),
]
