from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CompanyForm

@login_required
def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.created_by = request.user
            company.save()
            return redirect('create_company')
    else:
        form = CompanyForm()
    return render(request, 'company/create_company.html', {'form': form})