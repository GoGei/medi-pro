import django_tables2 as tables


class HrefColumn(tables.TemplateColumn):
    def __init__(self, reverse_url, record_label: str = 'id', template_code=None, template_name=None,
                 extra_context=None, **extra):
        if not template_code:
            template_code = '<a href="{% host_url \'%s\' record.id host "admin" %}" class="btn btn-xs btn-info">%s</a>' % (
                reverse_url, record_label)
        super().__init__(template_code=template_code, template_name=template_name, extra_context=extra_context, **extra)
