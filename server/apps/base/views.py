"""Views for the base app"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Hunt, Report, Bounty
from .serializers import HuntSerializer, ReportSerializer, BountySerializer


class HuntViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to hunt for bounties
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = HuntSerializer

    def get_queryset(self):
        return self.request.user.hunts.order_by('-created')


class BountyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows bounties to be viewed by users
    """
    queryset = Bounty.objects.all()
    serializer_class = BountySerializer
    lookup_field = 'slug'


class ReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to submit and view their reports
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = ReportSerializer

    def get_queryset(self):
        return self.request.user.reports.order_by('-created')
