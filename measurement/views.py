from rest_framework.decorators import api_view
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorsSerializer


@api_view(['GET', 'POST'])
def sensors_get_create(request):
    if request.method == 'GET':
        sensors = Sensor.objects.all()
        serialize_sensors = SensorsSerializer(sensors, many=True)
        return Response(serialize_sensors.data)

    if request.method == 'POST':
        name = request.data.get('name')
        descr = request.data.get('description')
        if not Sensor.objects.filter(name=name).filter(description=descr):
            new_sensor = Sensor(name=name, description=descr)
            new_sensor.save()
            resp_data = {
                'id': new_sensor.id,
                'name': new_sensor.name,
                'description': new_sensor.description,
            }
            return Response(status=200, data=resp_data)
        else:
            resp_data = {
                'status': 'already exists',
            }
            return Response(status=409, data=resp_data)


@api_view(['GET', 'PATCH'])
def sensors_update_get(request, sid):
    if request.method == 'GET':
        sensors = Sensor.objects.filter(id=sid)
        if sensors:
            serialize_sensors = SensorsSerializer(sensors, many=True)
            return Response(serialize_sensors.data)
        else:
            return Response(status=404)
    if request.method == 'PATCH':
        descr = request.data.get('description')
        res = Sensor.objects.filter(id=sid).update(description=descr)
        resp_data = {
            'id': sid,
            'status': 'updated',
            'lines': res,
        }
        return Response(status=200, data=resp_data)


@api_view(['POST'])
def add_measurements(request):
    if request.method == 'POST':
        sid = request.data.get('sensor')
        temp = request.data.get('temperature')
        sens = Sensor.objects.get(id=sid)
        new_measurement = Measurement(sensor_id=sens, mes_temperature=temp)
        new_measurement.save()
        return Response(status=200)

