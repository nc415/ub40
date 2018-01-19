from django.shortcuts import render
from django.http import HttpResponse
from repo.models import Company, BU
from repo.forms import PLstandardForm
# Create your views here.

def home(request):
    
	company_list=Company.objects.order_by('created_at')
	BU_list=BU.objects.order_by('Parent_Company')
	context_dict = {'Company': company_list, 'BU':BU_list}
	
	return render(request, 'repo/index.html', context=context_dict)

def company_profile(request, Company_Name):
	context_dict = {}
	try: 
		p1 = Company.objects.get(id=Company_Name)
		print(p1)

		
		context_dict['p1']=p1

	except Company.DoesNotExist:
		print("no page")
		context_dict['p1']=None

	
	return render(request, 'repo/company_page.html', context_dict)


def BU_Profile(request, BU_Name,Company_Name):
	context_dict = {}, 
	try: 
		b1 = BU.objects.get(id=BU_Name)
		print(b1)
		form=PLstandardForm()
		if request.method =='POST':
			form=PLstandardForm(request.POST)

			if form.is_valid():
				if b1:	
					b1=form.save(commit=False)
					
					b1.save()
					return home(request)
			else:
				print (form.errors)
		context_dict={"form":form, "b1":b1}	
		

	except Company.DoesNotExist:
		print("no page")
		context_dict['b1']=None

	

	
	return render(request, 'repo/BU_page.html', context_dict)