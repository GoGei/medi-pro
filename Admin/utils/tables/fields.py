import django_tables2 as tables
from django.utils.translation import gettext_lazy as _


class HrefColumn(tables.TemplateColumn):
    def __init__(self, reverse_url, record_label: str = 'id', template_code=None, template_name=None,
                 extra_context=None, **extra):
        if not template_name:
            template_name = 'Admin/base/tables/columns/id_template.html'

        if not extra_context:
            extra_context = dict()
        extra_context.setdefault('reverse_url', reverse_url)
        extra_context.setdefault('record_label', record_label)
        extra.setdefault('verbose_name', _('ID'))
        extra.setdefault('orderable', True)
        super().__init__(template_code=template_code, template_name=template_name, extra_context=extra_context, **extra)


class ManyToManyHrefColumn(tables.TemplateColumn):
    def __init__(self, reverse_url: str, related_qs_param: str, item_label: str = 'id',
                 template_code=None, template_name=None, extra_context=None, **extra):
        if not template_name:
            template_name = 'Admin/base/tables/columns/many_id_template.html'

        if not extra_context:
            extra_context = dict()
        extra_context['reverse_url'] = reverse_url
        extra_context['related_qs_param'] = related_qs_param
        extra_context.setdefault('item_label', item_label)
        extra.setdefault('verbose_name', _('ID'))
        extra.setdefault('orderable', False)
        super().__init__(template_code=template_code, template_name=template_name, extra_context=extra_context, **extra)


class DefaultActionFields(tables.TemplateColumn):
    def __init__(self, base_url, view_only: bool = False, template_code=None, template_name=None, extra_context=None,
                 **extra):
        if not template_name:
            template_name = 'Admin/base/tables/columns/actions_template.html'

        if not extra_context:
            extra_context = dict()
        extra_context.setdefault('view_url', f'{base_url}-view')
        if not view_only:
            extra_context.setdefault('edit_url', f'{base_url}-edit')
            extra_context.setdefault('archive_url', f'{base_url}-archive')
            extra_context.setdefault('restore_url', f'{base_url}-restore')
        extra.setdefault('verbose_name', _('Actions'))
        extra.setdefault('orderable', False)
        super().__init__(template_code=template_code, template_name=template_name, extra_context=extra_context, **extra)
