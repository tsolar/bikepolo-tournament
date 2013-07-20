from django_coverage import settings as settings_dc


TEST_RUNNER = 'django_coverage.coverage_runner.CoverageRunner'

settings_dc.COVERAGE_MODULE_EXCLUDES.extend([
    'static$',
    '.\.templates',
    '^debug_toolbar',
    '^social_auth',
    '\.tests',
    '^(south|djcelery)',
    'django.contrib.auth',
])
