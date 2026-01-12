"""
URL configuration for devProject project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from testApp import views  # ← 【重要】これを追加して views を使えるようにします

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('testApp.urls')),
    # ↓ これを追加しないと、timelineページにアクセスできません
    path("timeline/", views.timeline, name="timeline"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns