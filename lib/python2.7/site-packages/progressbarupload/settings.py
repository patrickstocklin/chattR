from django.conf import settings

PROGRESSBARUPLOAD_INCLUDE_JQUERY = getattr(settings, 'PROGRESSBARUPLOAD_INCLUDE_JQUERY', True)