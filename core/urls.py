from django.contrib import admin
from django.urls import path
from home.views import home, about, contact
from vege.views import add_recipe, manage_recipe, delete_recipe, update_recipe, login_page, register_page, logout_page
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", home),
    path("", add_recipe),
    path("delete-recipe/<int:id>/", delete_recipe),
    path("update-recipe/<int:id>/", update_recipe),
    path("manage-recipe/", manage_recipe),
    path("about/", about),
    path("contact/", contact),
    path("login/", login_page),
    path("register/", register_page),
    path("logout/", logout_page),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
