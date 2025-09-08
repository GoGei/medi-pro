from Api.views.base import SerializerMapBaseView
from Api.views.mixins import (
    CrmCreateModelMixin, CrmListModelMixin, CrmRetrieveModelMixin, CrmUpdateModelMixin, CrmDestroyModelMixin
)

from core.User.models import User


class ReadOnlyCrmMixinViewSet(CrmListModelMixin,
                              CrmRetrieveModelMixin,
                              ):
    pass


class CrmMixinViewSet(CrmCreateModelMixin,
                      CrmListModelMixin,
                      CrmRetrieveModelMixin,
                      CrmUpdateModelMixin,
                      CrmDestroyModelMixin
                      ):
    pass


class UserRelatedViewSet(SerializerMapBaseView):
    user_field = 'user_id'

    def get_queryset_filter(self):
        user = self.get_user()
        if not user:
            return {}
        return {self.user_field: user.id}

    def get_user(self) -> User | None:
        user = self.request.user
        if user.is_authenticated:
            return user
        return None

    def get_serializer_context(self):
        context = super().get_serializer_context()
        user = self.get_user()
        if user:
            context.update({'user': user, 'user_id': user.id})
        return context

    def get_queryset(self):
        user = self.get_user()
        if not user:
            return self.queryset.none()
        return super().get_queryset().filter(**self.get_queryset_filter())
