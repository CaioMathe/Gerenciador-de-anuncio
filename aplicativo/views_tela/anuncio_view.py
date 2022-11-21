from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from aplicativo.serializers import AnunciosSerializers
from aplicativo.models import Anuncios


def index_anuncio(request):
    return render(request, 'anuncios/home_anuncio.html')

def cadastro_anuncio(request):
    return render(request, 'anuncios/cadastro_anuncio.html')

def editar_anuncio(request, id):
    return render(request, 'anuncios/editar_anuncio.html')

@api_view(['GET'])
def AnunciosAPI(request, id):
    if id == '':
        imoveis = Anuncios.objects.all()
    else:
        imoveis = Anuncios.objects.filter(id_anuncio = id)
    serializer = AnunciosSerializers(imoveis, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def AddAnunciosAPI(request):
    serializer = AnunciosSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def DetalhesAnuncio(request, id):
    imovel = get_object_or_404(Anuncios, id_anuncio=id)
    serializer = AnunciosSerializers(imovel, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def UpdateAnuncio(request, id):
    imovel = get_object_or_404(Anuncios, id_anuncio=id)
    serializer = AnunciosSerializers(imovel, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)

@api_view(['DELETE'])
def DeleteAnuncio(request, id):
    if request.method == 'DELETE':
        imovel = get_object_or_404(Anuncios, id_anuncio=id)
        imovel.delete()
        return Response('Deletado', status=status.HTTP_200_OK)

    return Response("Esse anúncio não existe", status=status.HTTP_204_NO_CONTENT)