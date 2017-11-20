from django.conf.urls import url,include
from firstapp import views
from firstapp.views import AboutViewSet

urlpatterns = [
 
    url(r'^$',views.payment),
    url(r'^about/', 'payment.views.about', name='about'),
  
    
    
]