from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Employee,Location


# Define a custom admin class for Employee to control how it is displayed in the admin interface
class EmployeeAdmin(admin.ModelAdmin):
    # Specify the fields to display in the employee list
    list_display = ('name', 'phone','location', 'email', 'department', 'dob')

    # Add a search field to search employees by name or email
    search_fields = ('name', 'email')

    # Enable filtering options for the department
    list_filter = ('department',)

    # Set fields that can be clicked to go to the detail view
    list_display_links = ('name', 'email')

    # Customize the order in which fields appear on the edit page
    fields = ('name', 'phone', 'location', 'email', 'dob', 'department', 'emergency_contact', 'home_address', 'work_address', 'employee_type', 'travel_document', 'social_security')


# Register the Employee model and the custom admin class
admin.site.register(Employee, EmployeeAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Location, LocationAdmin)
