from django.urls import path
from hello import views
from hello.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset = LogMessage.objects.order_by("-log_date")[:5],
    context_object_name="message_list",
    template_name="hello/home.html",
)

urlpatterns = [
    path("<name>", views.hello_there, name="hello_there"),
    path("", home_list_view, name='hello_home'),
    path("log/", views.log_message, name='hello_log'),
    path("about/", views.about, name="hello_about"),
    path("contact/", views.contact, name="hello_contact"),
]
