from .models import contact_detail
from rest_framework import serializers

class HomePageSerializer(serializers.ModelSerializer):
    update = serializers.HyperlinkedIdentityField(
        view_name='update',
        lookup_field = 'pk'
    )
    class Meta:
        model = contact_detail
        fields = [
            'update',
            'telephone',
            'telephone2',
            'whatsapp',
            'instagram',
            'twitter',
            'telegram',
        ]