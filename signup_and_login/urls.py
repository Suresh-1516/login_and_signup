
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.loginpage,name='login'),
    path('signup/',views.signup,name='signup'),
    path('patient/<slug:user>',views.patient,name='patient'),
    path('docter/<slug:user>',views.docter,name='docter'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
