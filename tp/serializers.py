from rest_framework.serializers import ModelSerializer

from tp.models import Furniture, Shop, ShopOwner


class FurnitureSerializer(ModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'
        depth = 1


class ShopSerializer(ModelSerializer):

    class Meta:
        model = Shop
        fields = '__all__'
        depth = 1


class ShopOwnerSerializer(ModelSerializer):
    class Meta:
        model = ShopOwner
        fields = '__all__'
        depth = 1