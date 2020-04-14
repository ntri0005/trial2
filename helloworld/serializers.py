from rest_framework import serializers
from .models import trialTable, HospitalTable, BeachTable

class trialTableSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = trialTable
		fields = ('trialtable_title', 'trialtable_content', 'trialtable_published')
		
class HospitalTableSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = HospitalTable
		fields = ('hospital_id', 'hospital_name', 'hospital_address', 'hospital_wt', 'hospital_latitude', 'hospital_longitude')
		
class BeachTableSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = BeachTable
		fields = ('beach_id', 'beach_name', 'beach_latitude', 'beach_longitude')