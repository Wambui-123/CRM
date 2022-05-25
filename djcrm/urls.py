from django.contrib import admin
from django.urls import path, include
from leads.views import landing_page, LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name="landing_page"),
    # path('', landing_page, name="landing_page"),
    path('leads/', include('leads.urls', namespace="leads"))
]
