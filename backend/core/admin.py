from django.contrib import admin
from core.models import Session, Training, Exercise, Serie, MuscleGroup


class SessionAdmin(admin.ModelAdmin):
    pass


class TrainingAdmin(admin.ModelAdmin):
    pass


class ExerciseAdmin(admin.ModelAdmin):
    pass


class SerieAdmin(admin.ModelAdmin):
    pass


class MuscleGroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(Session, SessionAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Serie, SerieAdmin)
admin.site.register(MuscleGroup, MuscleGroupAdmin)
