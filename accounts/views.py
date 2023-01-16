from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProfileRegisterSerializer
from .models import Profile


class ProfileRegisterAPIView(viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileRegisterSerializer

    def create_profile(self, request, is_driver):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            serializer.save(is_driver=is_driver)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=False)
    def driver(self, request, pk=None):
        return self.create_profile(request, True)

    @action(methods=['POST'], detail=False)
    def ne_driver(self, request, pk=None):
        return self.create_profile(request, False)


class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileRegisterSerializer

    def perform_create(self, serializer):
        serializer.save(
            profile=self.request.user.profile
        )


class ProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileRegisterSerializer

    def get_queryset(self):
        return super().get_queryset().filter(id=self.kwargs.get('pk'))

    def perform_create(self, serializer):
        serializer.save(
            profile=self.request.user.profile
        )
