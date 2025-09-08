from django.http import Http404
from rest_framework import status, mixins
from rest_framework.response import Response
from Api.views.base import SerializerMapBaseView


class CrmCreateModelMixin(SerializerMapBaseView, mixins.CreateModelMixin):
    WITH_SUCCESS_HEADERS = True

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)

        if self.WITH_SUCCESS_HEADERS:
            headers = self.get_success_headers(serializer.data)
        else:
            headers = {}
        return_serializer = self.get_response_serializer(instance=instance)
        return Response(return_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, **kwargs):
        instance = serializer.save(created_by=self.request.user, **kwargs)
        return instance


class CrmListModelMixin(SerializerMapBaseView, mixins.ListModelMixin):
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.active()
        return qs


class CrmRetrieveModelMixin(SerializerMapBaseView, mixins.RetrieveModelMixin):
    def check_object_permissions(self, request, obj):
        super().check_object_permissions(request, obj)
        if hasattr(obj, 'is_active') and not obj.is_active:
            raise Http404
            # self.permission_denied(
            #     request,
            #     message='Object inactive',
            #     code=None
            # )


class CrmUpdateModelMixin(SerializerMapBaseView, mixins.UpdateModelMixin):
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial,
                                         context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        instance = self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return_serializer = self.get_response_serializer(instance=instance)
        return Response(return_serializer.data)

    def perform_update(self, serializer, **kwargs):
        instance = serializer.save(**kwargs)
        instance.modify(self.request.user)
        return instance


class CrmDestroyModelMixin(SerializerMapBaseView, mixins.DestroyModelMixin):
    def perform_destroy(self, instance):
        instance.archive(self.request.user)
        return instance
