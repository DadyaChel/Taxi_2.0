from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .models import Taxi, Order, StatusType
from .permissions import IsOwnerOrReadOnly, IsDriverOrReadOnly
from .serilaizers import TaxiSerializer, OrderSerializer, StatusDriverSerializer, StatusTypeSerializer


class TaxiViewSet(viewsets.ModelViewSet):
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer
    permission_classes = [IsDriverOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(taxi_id=self.kwargs.get('taxi_id'))

    def perform_create(self, serializer):
        serializer.save(
            profile=self.request.user.profile,
            taxi_id=self.kwargs.get('taxi_id')
        )


class OrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(taxi_id=self.kwargs.get('taxi_id'))

    def perform_create(self, serializer):
        serializer.save(
            profile=self.request.user.profile,
            taxi_id=self.kwargs.get('taxi_id')
        )


# class StatusTypeCreateAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = StatusType.objects.all()
#     serializer_class = StatusTypeSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_queryset(self):
#         return super().get_queryset().filter(profile_id=self.kwargs.get('id'))
#
#     def perform_create(self, serializer):
#         serializer.save(
#             profile=self.request.user.profile
#         )


class StatusTypeRetrieveUpdateDestroy(generics.ListCreateAPIView):
    queryset = StatusType.objects.all()
    serializer_class = StatusTypeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(profile_id=self.kwargs.get('id'))

    def perform_create(self, serializer):
        serializer.save(
            profile=self.request.user.profile,
            profile_id=self.kwargs.get('id')
        )
