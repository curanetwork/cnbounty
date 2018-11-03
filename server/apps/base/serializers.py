from django.db.models import Sum
from rest_framework import serializers

from .models import Hunt, Bounty, Report, User


class UserSerializer(serializers.ModelSerializer):
    total_stakes = serializers.SerializerMethodField() 

    @classmethod
    def total_stakes(self, obj):
        stakes = 0
        for hunt in obj.hunts.filter(user=obj):
            stakes += hunt.reports.filter(
                status='approved').aggregate(
                stakes=Sum('num_of_stakes'))['stakes'] or 0
        return stakes

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'eth_address', 'is_active',
            'total_stakes', 'modified', 'date_joined')


class HuntSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hunt
        fields = ('id', 'user', 'bounty', 'num_of_stakes', 'modified',
            'created')
        read_only_fields = ('num_of_stakes',)


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = ('id', 'hunt', 'details', 'status', 'modified', 'created')
        read_only_fields = ('status',)


class BountySerializer(serializers.ModelSerializer):
    is_ongoing = serializers.SerializerMethodField()
    is_ended = serializers.SerializerMethodField()
    total_stakes = serializers.SerializerMethodField()
    num_of_hunts = serializers.SerializerMethodField()    

    @classmethod
    def is_ongoing(self, obj):
        return obj.start <= timezone.now() <= obj.end

    @classmethod
    def is_ended(self, obj):
        return obj.end < timezone.now() and not is_ongoing()

    @classmethod
    def total_stakes(self, obj):
        stakes = 0
        for hunt in obj.hunts.all():
            stakes += hunt.reports.filter(
                status='approved').aggregate(
                stakes=Sum('num_of_stakes'))['stakes'] or 0
        return stakes

    @classmethod
    def num_of_hunts(self, obj):
        return obj.hunts.all().count()

    class Meta:
        model = Bounty
        fields = ('id', 'name', 'details', 'is_ongoing', 'is_ended',
            'total_stakes', 'num_of_hunts', 'signup_fields', 'report_fields',
            'modified', 'created')
