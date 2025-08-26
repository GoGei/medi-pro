import django_filters
from Admin.utils.filters.fields import IsActiveMixinField
from core.Medicine.models import AllergyReaction


class AllergyReactionFilter(django_filters.FilterSet):
    is_active = IsActiveMixinField(required=False)

    class Meta:
        model = AllergyReaction
        fields = ('is_active', 'source')
