from django.contrib import admin
from facts.models import Fact, Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    class Meta:
        model = Tag

@admin.register(Fact)
class FactAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'description', 'proof_link', 'created_at', 'updated_at')
    list_filter = ('year', 'created_at', 'updated_at')
    search_fields = ('name', 'description', 'proof_link')
    ordering = ['-created_at']
    class Meta:
        model = Fact
        verbose_name = 'Fact'
        verbose_name_plural = 'Facts'

