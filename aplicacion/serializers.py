from aplicacion.models import Cliente
from aplicacion2.models import Promocion
from rest_framework import serializers

class ClienteSerializar(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PromocionSerializar(serializers.ModelSerializer):
    class Meta:
        model = Promocion
        fields = '__all__'