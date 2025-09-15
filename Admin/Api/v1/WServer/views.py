from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, AuthUser, T

from Api.permissions import AdminPermissions

from Api.views.base import SerializerMapBaseView


class AdminAccessToken(AccessToken):
    @classmethod
    def for_user(cls: type[T], user: AuthUser) -> T:
        token = super().for_user(user)
        token['is_active'] = user.is_active
        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser
        return token


class WServerAPIView(SerializerMapBaseView):
    permission_classes = (AdminPermissions,)
    pagination_class = None
    filter_backends = ()

    @action(methods=['get'], detail=False, url_path='token/obtain', url_name='token/obtain')
    def obtain_token(self, request, *args, **kwargs):
        token = AdminAccessToken.for_user(request.user)
        return Response({'token': str(token)})
