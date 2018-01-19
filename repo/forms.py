from django import forms
from repo.models import PLstandard
from datetime import datetime
from django.db.models import Q
import itertools
from django.utils.text import slugify
from django.contrib.auth.models import User
import re


class PLstandardForm(forms.ModelForm):

	TotalRevenue=forms.DecimalField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Total_Revenue'}), max_digits=10, decimal_places=2)
	
	class Meta:
		model = PLstandard
		fields=('TotalRevenue',)

	