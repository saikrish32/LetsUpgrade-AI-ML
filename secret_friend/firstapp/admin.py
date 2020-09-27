from django.contrib import admin
from firstapp.models import Question,Answer,Friends

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)


# Register your models here.
class FriendsAdmin(admin.ModelAdmin):
    list_display = ['secret_friend', 'First_name', 'Hint1','Hint2','challenge','Choice_1','secret_Hint1','secret_Hint2','task','url_link','verification','time']

admin.site.register(Friends,FriendsAdmin)
