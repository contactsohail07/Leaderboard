from django import forms
from .models import Board
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BoardForm(forms.ModelForm):

	class Meta:
		model = Board
		fields = ('name','score')


