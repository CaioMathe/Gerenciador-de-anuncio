from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from aplicativo.serializers import ImoveisSerializers
from aplicativo.models import Imoveis


def index_imoves(request):
    return render(request, 'imoveis/Home_imoveis.html')

def cadastro_imoves(request):
    return render(request, 'imoveis/cadastro_imoveis.html')

def editar_imovel(request, id):
    return render(request, 'imoveis/editar_imoveis.html')

@api_view(['GET'])
def ImoveisAPI(request, id):
    if id == '':
        imoveis = Imoveis.objects.all()
    else:
        imoveis = Imoveis.objects.filter(id = id)

    serializer = ImoveisSerializers(imoveis, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def AddImoveisAPI(request):
    serializer = ImoveisSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def ImovelUpdate(request, id):
    imovel = get_object_or_404(Imoveis, id=id)
    serializer = ImoveisSerializers(imovel, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)

@api_view(['DELETE'])
def ImovelDelete(request, id):
    if request.method == 'DELETE':
        imovel = get_object_or_404(Imoveis, id=id)
        imovel.delete()
        return Response('Imóvel Deletado', status=status.HTTP_200_OK)

    return Response("Esse imóvel não existe", status=status.HTTP_204_NO_CONTENT)