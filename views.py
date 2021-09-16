from django.shortcuts import render

from .models import Users,My_Booking,Seats_Data
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


def login(request):
	if request.method=="POST":
		email=request.POST["email"]
		password=request.POST["password"]
		print(email)
		print(password)
		try:
			user=Users.objects.get(email=email,password=password)
			return HttpResponseRedirect(reverse("polls:mybooking",args=[user.id]))

		except Users.DoesNotExist:
			return HttpResponseRedirect(reverse("polls:signup"))

	else: 	
		return render(request,"polls/login.html")

def my_booking(request, user_id):
	try :
		user_obj=Users.objects.get(id=user_id)
		print(user_obj)
		items=My_Booking.objects.filter(user_id=user_id)
		print(items)
	except Users.DoesNotExist:
		return HttpResponseRedirect(reverse("polls:signup"))

	return render(request,"polls/my_booking.html",{"user_id":user_id,"username":user_obj.firstName+ " "+user_obj.lastName,"items":items })

def signup(request):
	if request.method == "POST":
		firstName=request.POST["firstname"]
		lastName=request.POST["lastname"]
		email=request.POST["email"]
		password=request.POST["password"]
		data={"firstName":firstName,"lastName":lastName,"email":email,"password":password}
		Users.objects.create(**data)
		
		return HttpResponseRedirect(reverse("polls:login"))

	return render(request,"polls/signup.html")





def create_booking(request,user_id):
	try:
		user = Users.objects.get(pk=user_id)
		name=user.firstName+ " " + user.lastName
		
	except Users.DoesNotExist:
		return(HttpResponse("your account does not exit , so please firest signupo the page  "))
	
	else:

		if request.method == "POST":
			print(type(request.POST["seats"]))	
			seats=int(request.POST["seats"])
			date=request.POST["date"]
			seat_data=Seats_Data.objects.all().order_by('date').first()
			print(seat_data)
			current_price=seat_data.pricePerSeat
			
			if seat_data.totalSeats>=seats:
				seat_data.totalSeats=seat_data.totalSeats-seats
				seat_data.save() 
				total_amount=seats*current_price
				mybooking_data={"seats":seats,"date":date,"amount":total_amount,"user_id":user}
				My_Booking.objects.create(**mybooking_data)
				print("hello ================================================")

				return render(request,"polls/create_booking.html",{"username":name,"total_amount":total_amount,"user_id":user_id})
			else:
			
				return(HttpResponse("no seats avalable"))
 


			
			
			
		else:
			return render(request,"polls/create_booking.html",{"user_id":user_id,"username":name})
			