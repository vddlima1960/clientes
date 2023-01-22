from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
     
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"O Nome não pode ter dígitos numéricos."})

        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"O CPF não é válido."})

        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O RG deve ter 9 dígitos."})

        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O Celular deve seguir o formato : '99 99999-9999'"})

        return data
 