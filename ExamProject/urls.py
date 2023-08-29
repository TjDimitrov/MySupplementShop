from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ExamProject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ExamProject.common.urls')),
    path('accounts/', include('ExamProject.accounts.urls')),
    path('products/', include('ExamProject.products.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'ExamProject.common.views.custom_404'
