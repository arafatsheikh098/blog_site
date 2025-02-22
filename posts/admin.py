from django.contrib import admin
from posts.models import Post,comment
class PostAdmin (admin.ModelAdmin):
    list_display=["id","title","publish_date"]
# Register your models here.

admin.site.register(Post,PostAdmin)



class CommnetAdmin (admin.ModelAdmin):
    list_display=["id","text","post_id"]
admin.site.register(comment,CommnetAdmin)
