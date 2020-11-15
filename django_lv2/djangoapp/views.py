from django.shortcuts import render
from djangoapp.forms import NewUserForm
# from djangoapp.models import User

# Create your views here.

def index(request):
	return render(request, 'djangoapp/index.html')


def users(request):
	# user_list = User.objects.order_by('first_name')
	# user_dict = {'users': user_list}
	# return render(request, 'djangoapp/users.html', context=user_dict)

	form = NewUserForm()

	if request.method == "POST":
		form = NewUserForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)

		else:
			print('Error form invalid')

	return render(request, 'djangoapp/users.html', {'form': form})





