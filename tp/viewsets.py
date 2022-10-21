from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from tp.models import Furniture, Shop, ShopOwner
from tp.serializers import FurnitureSerializer, ShopSerializer, ShopOwnerSerializer


class FurnitureViewSet(ModelViewSet):
    serializer_class = FurnitureSerializer
    queryset = Furniture.objects.all()

    @action(detail=True, methods=['get'], url_path='sell')
    def sell(self, request, pk=None):
        furniture = self.get_object()
        print(furniture)
        furniture.status = 'Sold'
        furniture.save()
        furniture.location.turnover += furniture.price
        furniture.location.save()
        return Response({'status': 'ok'})

    @action(detail=True, methods=['get'], url_path='set-condition')
    def update_status(self, request, pk=None):
        furniture = self.get_object()
        furniture.status = self.request.query_params.get('condition')
        furniture.save()
        return Response({'status': 'ok'})


class ShopViewSet(ModelViewSet):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()


class ShopOwnerViewSet(ModelViewSet):
    serializer_class = ShopOwnerSerializer
    queryset = ShopOwner.objects.all()