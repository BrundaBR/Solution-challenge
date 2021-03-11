from django.shortcuts import render,redirect

# Create your views here.
#signup function with render's from sigup.html page
user=[]
def signUp(request):
	if request.method=="POST":
		username_data=request.POST.get('username')
		email_data=request.POST.get('email')
		password_data=request.POST.get('password')
# save data from user to form

		save_data=SignupForm(username=username_data,email=email_data,password=password_data)
		save_data.save()
	
		return redirect('/signin')
	else:
		return render(request,'signup.html')
   

#signin function with render's from sigin.html page
def signIn(request):
	if user!=[]:user.pop()
	if request.method=="POST":
		user_name=request.POST.get('username')
		password_data=request.POST.get('password')
		if SignupForm.objects.filter(username=user_name,password=password_data):
			user.append(user_name)
			return redirect('/home')
		else:
			return redirect('/signuppage')
	return render(request,'signin.html')