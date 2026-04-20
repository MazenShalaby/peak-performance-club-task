from django.contrib import admin

from .models import Member, Trainer, Branch, GymClass, Equipment

# Register your models here.


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", "balance", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("name", "created_at", "updated_at")


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("name", "specialization", "created_at", "updated_at")
    search_fields = ("name", "specialization")
    list_filter = ("name", "specialization", "created_at", "updated_at")


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "created_at", "updated_at")
    search_fields = ("name", "location")
    list_filter = ("name", "created_at", "updated_at")


@admin.register(GymClass)
class GymClassAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "base_price",
        "start_date",
        "trainer",
        "created_at",
        "updated_at",
    )
    search_fields = ("title", "trainer")
    list_filter = ("title", "start_date", "created_at", "updated_at")


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ("name", "is_damaged", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("name", "is_damaged", "created_at", "updated_at")
