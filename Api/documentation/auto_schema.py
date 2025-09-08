from drf_spectacular.openapi import AutoSchema


class TaggedSpectacularAutoSchema(AutoSchema):
    def get_tags(self):
        tags = getattr(self.view, 'VIEW_TAGS', None)
        if tags:
            return list(tags)
        return super().get_tags()
