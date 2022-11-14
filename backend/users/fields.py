from django.db.models import CharField
from django_case_insensitive_field import CaseInsensitiveFieldMixin

class CaseInsensitiveCharField(CaseInsensitiveFieldMixin, CharField):
    # Makes django CharField case insensitiv

    def __init__(self, *args, **kwargs):
        super(CaseInsensitiveFieldMixin, self).__init__(*args, **kwargs) 
        