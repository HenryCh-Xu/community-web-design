from django.contrib import admin

# Register your models here.

from web_v.models import lost_find_topic
from web_v.models import lost_find_entry
from web_v.models import electronics_topic
from web_v.models import electronics_entry
from web_v.models import necessary_topic
from web_v.models import necessary_entry


admin.site.register(lost_find_topic)
admin.site.register(lost_find_entry)
admin.site.register(electronics_topic)
admin.site.register(electronics_entry)
admin.site.register(necessary_topic)
admin.site.register(necessary_entry)
