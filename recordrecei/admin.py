from django.contrib import admin
from .models import docitem_rfid,doc_items,items,documents

admin.site.register(docitem_rfid)
admin.site.register(doc_items)
admin.site.register(items)
admin.site.register(documents)
