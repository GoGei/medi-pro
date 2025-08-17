import django_tables2 as tables


class HrefColumn(tables.TemplateColumn):
    def __init__(self, reverse_url, record_label: str = 'id', template_code=None, template_name=None,
                 extra_context=None, **extra):
        if not template_name:
            template_name = 'Admin/base/tables/columns/id_template.html'

        if not extra_context:
            extra_context = dict()
        extra_context['reverse_url'] = reverse_url
        extra_context['record_label'] = record_label
        super().__init__(template_code=template_code, template_name=template_name, extra_context=extra_context, **extra)
