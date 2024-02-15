from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'total_tasks', 'undone_tasks', 'recent_tasks', 'owner']
    list_display_links = ['name']
    list_filter = ['owner']
    search_fields = ['name', 'project_name', 'owner__last_name', 'owner__username']
    fieldsets = (
        (None, {
            "fields": (
                'name', 'owner',
            ),
        }),
    )
    
    # def priority(self, obj: models.Projects):
    #     return obj.

    def total_tasks(self, obj: models.Project):
        return obj.tasks.count()
    total_tasks.short_description = _("total tasks")

    def undone_tasks(self, obj: models.Project):
        return obj.tasks.filter(is_done=False).count()
    undone_tasks.short_description = _('undone tasks')

    def recent_tasks(self, obj: models.Project):
        return "; ".join(obj.tasks.order_by('-created_at').values_list('name', flat=True)[:3])
    recent_tasks.short_description = _('recent tasks')        
    

class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_done', 'deadline', 'project', 'owner', 'recent_tasks', 'created_at']
    list_filter = ['is_done', 'project', 'deadline', 'created_at', 'owner']
    search_fields = ['name', 'description', 'project__name', 'owner__last_name', 'owner__username']
    list_editable = ['is_done', 'owner', 'project']
    readonly_fields = ['id', 'created_at', 'updated_at']
    fieldsets = (
        (_('general').title(), {
            "fields": (
                ('name', 'deadline'), 
                'description', 'is_done',
            ),
        }),
        (_('ownership').title(), {
            "fields": (
                ('owner', 'project'),
            ),
        }),
        (_('temporal tracking').title(), {
            "fields": (
                ('created_at', 'updated_at', 'id'),
            ),
        }),
    )
    
    def recent_tasks(self, obj: models.Task):
        undone_tasks = obj.project.tasks.filter(is_done=False).order_by('-created_at')[:3]
        task_names = [task.name for task in undone_tasks]
        return ", ".join(task_names)
    recent_tasks.short_description = _('recent tasks')


admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Task, TaskAdmin)