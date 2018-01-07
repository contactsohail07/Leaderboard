
from django.shortcuts import redirect
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from .models import Board
from .forms import BoardForm

def front_page(request):
	board=Board.objects.order_by('-score')
	return render(request,'leaderboard/front_page.html',{'board':board})

def link_page(request,pk):
	board=get_object_or_404(Board, pk=pk)
	return render(request,'leaderboard/link_page.html',{'board':board})

def form_page(request):
	if request.method == "POST":
		form=BoardForm(request.POST)
		if form.is_valid():
			board=form.save(commit=False)
			board.creator=request.user
			board.save()
			print(board.creator)
			return redirect('link_page' , pk=board.pk)
	else:
		form=BoardForm()
		return render(request,'leaderboard/form_page.html',{'form':form})

def form_edit(request,pk):
	board=get_object_or_404(Board,pk=pk)
	if request.method == "POST":
		form=BoardForm(request.POST,instance=board)
		if form.is_valid() and request.user == board.creator:
			board=form.save(commit=False)
			board.save()
			return redirect('link_page' , pk=board.pk)
		else:
			message = "Sorry,we couldn't process the request"
			return render(request, 'leaderboard/failure.html',{'message':message})
	else:
		form=BoardForm(instance=board)
		return render(request,'leaderboard/form_page.html',{'form':form})
	
def del_page(request,pk):
	board = Board.objects.get(pk=pk)
	print(board.creator)
	print(request.user)
	if board.creator == request.user:
		board=Board.objects.get(pk=pk)
		board.delete()
		return redirect('front_page')
	else:
		message = "Sorry,we couldn't process the request"
		return render(request, 'leaderboard/failure.html',{'message':message})

def form_signup(request):
	if request.method == "POST":
		print(request.POST)
		form=UserCreationForm(request.POST)
		print(form)
		if form.is_valid():
			obj = form.save(commit=False)
			username=form.cleaned_data.get("username")
			password=form.cleaned_data.get("password1")
			obj = form.save()
			user=authenticate(username=username,password=password)
		
			login(request,user)
			return redirect('front_page')
	else:
		form=UserCreationForm()
		return render(request,'leaderboard/form_signup.html',{'form':form})

def form_signin(request):
	if request.method == "POST":
		form=AuthenticationForm(request.POST)
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('front_page')
	else:
		form=AuthenticationForm()
		return render(request,'leaderboard/form_signin.html',{'form':form})


def form_signout(request):
	logout(request)
	return redirect('form_signin')








