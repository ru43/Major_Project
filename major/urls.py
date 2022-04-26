"""major URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from core import views
from django.contrib.auth import views as auth_views
from core.customer import views as customer_views
from core.courier import views as courier_views
from django.conf import settings
from django.conf.urls.static import static

customer_urlpatters = [
    path('', customer_views.home, name="home"),
    path('profile/', customer_views.profile_page, name="profile"),
    # path('payment_method/', customer_views.payment_method_page, name="payment_method"),
    # path('create_job/', customer_views.create_job_page, name="create_job"),

    # path('jobs/current/', customer_views.current_jobs_page, name="current_jobs"),
    # path('jobs/archived/', customer_views.archived_jobs_page, name="archived_jobs"),
    # path('jobs/<job_id>/', customer_views.job_page, name="job"),
]

courier_urlpatters = [
    path('', courier_views.home, name="home"),
#     path('jobs/available/', courier_views.available_jobs_page, name="available_jobs"),
#     path('jobs/available/<id>/', courier_views.available_job_page, name="available_job"),
#     path('jobs/current/', courier_views.current_job_page, name="current_job"),
#     path('jobs/current/<id>/take_photo/', courier_views.current_job_take_photo_page, name="current_job_take_photo"),
#     path('jobs/complete/', courier_views.job_complete_page, name="job_complete"),
#     path('jobs/archived/', courier_views.archived_jobs_page, name="archived_jobs"),
#     path('profile/', courier_views.profile_page, name="profile"),
#     path('payout_method/', courier_views.payout_method_page, name="payout_method"),

#     path('api/jobs/available/', courier_apis.available_jobs_api, name="available_jobs_api"),
#     path('api/jobs/current/<id>/update/', courier_apis.current_job_update_api, name="current_job_update_api"),
#     path('api/fcm-token/update/', courier_apis.fcm_token_update_api, name="fcm_token_update_api"),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home), #for base page we use empty ''

    path('sign-in/', auth_views.LoginView.as_view(template_name="sign_in.html")),
    path('sign-out/', auth_views.LogoutView.as_view(next_page="/")),
    path('sign-up/', views.sign_up),
    path('customer/',include((customer_urlpatters,'customer'))  ),
    path('courier/', include((courier_urlpatters,'courier'))),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)