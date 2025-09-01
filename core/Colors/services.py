import json
from .const import DEFAULT_FIXTURE
from .models import EmployeeColors


def import_colors_from_fixture(archive_not_mentioned: bool = True, fixture: str = DEFAULT_FIXTURE):
    mentioned: set[int] = set()
    data = json.load(open(fixture, 'r'))

    for item in data:
        base_field = item.pop('sideline')
        obj, _ = EmployeeColors.objects.update_or_create(
            sideline=base_field,
            defaults=item
        )
        mentioned.add(obj.id)
        if not obj.is_active:
            obj.restore()

    if archive_not_mentioned:
        EmployeeColors.objects.exclude(id__in=mentioned).archive()
