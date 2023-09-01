from django.contrib import admin
from supplier.models import Supplier, Contact

# Inline Contact
class ContactInline(admin.TabularInline):
    model = Contact
    extra = 0
    fk_name = "supplier"


# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        "corporate_name",
        "address",
        "created_at",
    )
    list_filter = ("created_at",)
    search_fields = (
        "corporate_name",
        "address",
    )
    inlines = [
        ContactInline,
    ]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "created_at",
    )
    list_filter = ("created_at",)
    search_fields = (
        "name",
        "email",
    )
