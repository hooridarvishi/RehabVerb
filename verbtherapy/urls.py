from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='home'),
    path('card/<int:card_id>/page/<int:page_number>/', views.card_detail, name='card_detail'),
    path('toggle-image/<int:card_id>/', views.toggle_image, name='toggle_image'),
    path('toggle-text/<int:card_id>/<str:field_type>/', views.toggle_text, name='toggle_text'),
    path('update-blank/', views.update_blank, name='update_blank'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)