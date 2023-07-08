from django.urls import path

from measurement.views import ListCreateView, SensUpdateView, SensView, MeasurementCreateView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('list_sensor/', ListCreateView.as_view()),
    path('sensor_up/<int:pk>/', SensUpdateView.as_view()),
    path('temp_set/', MeasurementCreateView.as_view()),
    path('sensor/<int:pk>/', SensView.as_view()),

]
