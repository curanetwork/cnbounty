from django import forms
from django.contrib import admin
from django_admin_json_editor import JSONEditorWidget

from .models import Bounty, Hunt, Report, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'eth_address', 'is_active',
    	'is_admin', 'is_staff', 'date_joined')
    list_filter = ('is_active', 'is_admin', 'is_staff', 'date_joined')
    search_fields = ('email', 'username')


class BountyAdminForm(forms.ModelForm):
    class Meta:
        model = Bounty
        fields = '__all__'
        widgets = {
            'signup_form': JSONEditorWidget({
                'type': 'array', 'format': 'table' }, collapsed=False),
            'report_form': JSONEditorWidget({
                'type': 'array', 'format': 'table' }, collapsed=False)
        }


@admin.register(Bounty)
class BountyAdmin(admin.ModelAdmin):
    form = BountyAdminForm
    list_display = ('name', 'percent_share', 'intro', 'start', 'end', 'signup_form',
    	'report_form', 'modified', 'created')
    list_filter = ('modified', 'created',)
    search_fields = ('name',)


@admin.register(Hunt)
class HuntAdmin(admin.ModelAdmin):
    list_display = ('user', 'bounty', 'details', 'modified', 'created')
    list_filter = ('modified', 'created',)
    search_fields = ('bounty__name', 'user__email', 'user__username')


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('hunt', 'details', 'num_of_stakes', 'status',
    	'modified', 'created')
    list_filter = ('modified', 'created',)
    search_fields = ('name',)
