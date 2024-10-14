from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import EmployeeRegistrationForm

# Employee Registration View
def employee_registration(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to success page after submission
    else:
        form = EmployeeRegistrationForm()
    return render(request, 'employee/employee_registration.html', {'form': form})

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'directory/admin_login.html', {'error': 'Invalid credentials'})
    return render(request, 'employee/admin_login.html')


from django.shortcuts import render
from .models import Employee, Location  # Assuming Location model exists


def admin_dashboard(request):
    # Fetch all locations
    locations = Location.objects.all()

    # Get the selected location from the query parameters
    selected_location_id = request.GET.get('location')

    if selected_location_id:
        # If a location is selected, filter employees by location
        employees = Employee.objects.filter(location__id=selected_location_id)
    else:
        # Otherwise, fetch all employees
        employees = Employee.objects.all()

    return render(request, 'employee/admin_dashboard.html', {
        'employees': employees,
        'locations': locations,
        'selected_location_id': selected_location_id
    })


# Edit Employee

def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = EmployeeRegistrationForm(instance=employee)
    return render(request, 'employee/employee_registration.html', {'form': form})

# Delete Employee

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('admin_dashboard')
    return render(request, 'employee/employee_confirm_delete.html', {'employee': employee})


# Landing Page with 2 buttons
def landing_page(request):
    return render(request, 'employee/landing_page.html')
from django.shortcuts import render

# Success page view
def success(request):
    return render(request, 'employee/success.html')
