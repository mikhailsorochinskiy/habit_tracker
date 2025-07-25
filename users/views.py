from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsOwnerOrAdmin


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'login']:
            return [AllowAny()]
        if self.action in ['list']:
            return [IsAdminUser()]
        return [IsAuthenticated(), IsOwnerOrAdmin()]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return User.objects.all()
        return User.objects.filter(pk=user.pk)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()
