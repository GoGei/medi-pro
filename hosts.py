from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host('', 'Public.urls', name='public'),
    host('api', 'Api.urls', name='api'),
    host('clinic', 'Clinic.urls', name='clinic'),
    host('admin', 'Admin.urls', name='admin'),
)
