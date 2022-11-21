from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from aplicativo.serializers import ReservasSerializers
from aplicativo.models import Reservas


def index_reserva(request):
    return render(request, 'reservas/home_reserva.html')

def cadastro_reserva(request):
    return render(request, 'reservas/cadastro_reserva.html')

def editar_reserva(request, id):
    return render(request, 'reservas/editar_reserva.html')

@api_view(['GET'])
def ReservasAPI(request, id):
    if id == '':
        reserva = Reservas.objects.all()
    else:
        reserva = Reservas.objects.filter(id_reserva = id)

    serializer = ReservasSerializers(reserva, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def AddReservasAPI(request):
    serializer = ReservasSerializers(data=request.data)
    # print(f'{request.check_out}--------------')
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def DeleteReservas(request, id):
    if request.method == 'DELETE':
        reserva = get_object_or_404(Reservas, id_reserva=id)
        reserva.delete()
        return Response('Deletado', status=status.HTTP_200_OK)

    return Response("Essa Reserva não existe", status=status.HTTP_204_NO_CONTENT)