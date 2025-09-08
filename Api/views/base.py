from rest_framework import viewsets
from rest_framework.serializers import Serializer
from Api.serializers import EmptySerializer
from django.conf import settings


class TaggedViewSet:
    class CommonTags:
        pass

    VIEW_TAGS = tuple()


class SerializerMapBaseView(viewsets.GenericViewSet):
    serializer_map: dict[str, Serializer] = dict()
    empty_serializer_actions: tuple[str, ...] = tuple()

    response_serializer_map: dict[str, Serializer] = dict()
    empty_response_serializer_actions: tuple[str, ...] = tuple()
    response_serializer_class: Serializer = None

    def get_serializer_class(self):
        if self.action in self.empty_serializer_actions:
            return EmptySerializer
        return self.serializer_map.get(self.action, self.serializer_class)

    def get_response_serializer_class(self):
        if self.action in self.empty_response_serializer_actions:
            return EmptySerializer
        response_class = self.response_serializer_map.get(self.action, self.response_serializer_class)
        basic_class = response_class or self.serializer_class
        if basic_class:
            return basic_class
        return self.serializer_map.get(self.action, None)

    def get_response_serializer(self, *args, **kwargs):
        serializer_class = self.get_response_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)
