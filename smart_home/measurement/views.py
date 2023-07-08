from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer,  SensorDetailSerializer

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


class ListCreateView(ListCreateAPIView):
    """
    Создать датчик. Указываются название и описание датчика.
    Получить список датчиков.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensUpdateView(RetrieveUpdateAPIView):
    """
    Изменить датчик. Указываются название и/или описание.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementCreateView(ListCreateAPIView):
    """
    Добавить измерение. Указываются ID датчика и температура.
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensView(RetrieveUpdateAPIView):
    """
    Получить информацию по конкретному датчику.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
