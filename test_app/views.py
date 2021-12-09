import datetime
from django.http import Http404
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from test_app.models import *
from test_app.serializers import *


class HomePage(TemplateView):
    """Home page view."""
    template_name = "home_page.html"


class DriversListAPI(APIView):
    """
    Get list of all drivers, filter them by creation date or create new one.
    """
    def get_date(self):
        try:
            if self.request.GET.get("created_at__gte"):
                date_field = datetime.datetime.strptime(self.request.GET.get("created_at__gte"), "%d-%m-%Y")
            elif self.request.GET.get("created_at__lte"):
                date_field = datetime.datetime.strptime(self.request.GET.get("created_at__lte"), "%d-%m-%Y")
        except ValueError:
            raise Http404
        return date_field

    def get_objects(self):
        if self.request.GET.get("created_at__gte"):
            drivers = Driver.objects.filter(created_at__gte=self.get_date())
        elif self.request.GET.get("created_at__lte"):
            drivers = Driver.objects.filter(created_at__lte=self.get_date())
        else:
            drivers = Driver.objects.all()
        return drivers

    def get(self, request):
        drivers = self.get_objects()
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DriverAPI(APIView):
    """
    Get, update or delete specified driver.
    """
    def get_object(self, pk):
        try:
            return Driver.objects.get(id=pk)
        except Driver.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        driver = self.get_object(pk)
        serializer = DriverSerializer(driver)
        return Response(serializer.data)

    def patch(self, request, pk):
        driver = self.get_object(pk)
        serializer = DriverSerializer(driver, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)

    def delete(self, request, pk):
        driver = self.get_object(pk)
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VehiclesListAPI(APIView):
    """
    Get list of all vehicles, filter them by driver value null/not null or create new vehicle.
    """
    def get_objects(self):
        if self.request.GET.get("with_drivers") == "yes":
            vehicles = Vehicle.objects.filter(driver__isnull=False)
        elif self.request.GET.get("with_drivers") == "no":
            vehicles = Vehicle.objects.filter(driver__isnull=True)
        else:
            vehicles = Vehicle.objects.all()
        return vehicles

    def get(self, request):
        vehicles = self.get_objects()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VehicleAPI(APIView):
    """
    Get, update or delete specified vehicle.
    """
    def get_object(self, pk):
        try:
            return Vehicle.objects.get(id=pk)
        except Vehicle.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        vehicle = self.get_object(pk)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)

    def patch(self, request, pk):
        vehicle = self.get_object(pk)
        serializer = VehicleSerializer(vehicle, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)

    def delete(self, request, pk):
        vehicle = self.get_object(pk)
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VehicleSetDriverAPI(VehicleAPI):
    """Set/remove driver from vehicle."""
    def patch(self, request, pk):
        vehicle = self.get_object(pk)
        serializer = VehicleSerializer(vehicle, data={"driver": request.data.get("driver")}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)
