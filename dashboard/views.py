from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import CustomUser

# 🔵 Employer Dashboard
@login_required
def employer_dashboard(request):
    if request.user.role != 'EMPLOYER':
        return render(request, 'dashboard/access_denied.html')
    return render(request, 'dashboard/employer_dashboard.html')

# 🟢 Employee Dashboard
@login_required
def employee_dashboard(request):
    if request.user.role != 'EMPLOYEE':
        return render(request, 'dashboard/access_denied.html')
    return render(request, 'dashboard/employee_dashboard.html')
