from rest_framework import serializers

from .models import Hunt, Bounty, Report, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'eth_address', 'is_active',
            'modified', 'date_joined')


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

    @classmethod
    def is_ongoing(self, obj):
        return obj.start <= timezone.now() <= obj.end

    @classmethod
    def is_ended(self, obj):
        return obj.end < timezone.now() and not is_ongoing()

    class Meta:
        model = Bounty
        fields = ('id', 'name', 'details', 'is_ongoing', 'is_ended',
            'signup_fields', 'report_fields', 'modified', 'created')
