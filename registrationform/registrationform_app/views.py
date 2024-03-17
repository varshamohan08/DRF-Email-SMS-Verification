from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from registrationform_app.forms import UserForm
from django.contrib.auth.models import User
from django.db import transaction
from registrationform_app.models import UserDetails
from django.core.mail import send_mail
from random import randint
from datetime import datetime
from django.utils.timezone import make_aware
from twilio.rest import Client
from django.conf import settings

# Create your views here.


def send_sms_view(to, otp, username):
    body = """Registration done successfully
    Your username is {username}
    Your one time password is {otp}
    """.format(username = username, otp = otp)
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(to='+91'+str(to), from_=settings.TWILIO_PHONE_NUMBER, body=body)
    return message.sid

def send_reg_mail(to_mail, msg):
    subject = "User registered Successfully"
    msg = msg
    
    send_mail(
        subject,
        msg,
        "varshamohan654@gmail.com",
        [to_mail],
        fail_silently=False,
    )


class userLogout(APIView):
    def get(self, request):
        logout(request)
        return redirect('')

class UserAPI(APIView):
    def get(self, request):
        return render(template_name="registration_form.html", request=request)
    
    def post(self, request):
        try:
            with transaction.atomic():
                user_details =  UserForm(request.POST)
                if user_details.is_valid():
                    otp = ''.join([str(randint(0, 9)) for _ in range(4)])
                    user = User.objects.create(username=request.data.get('email'))
                    user.email = request.data.get('email')
                    user.set_password(otp)
                    user.save()
                    UserDetails.objects.create(
                        user=user,
                        first_name=request.data.get('first_name'),
                        last_name=request.data.get('last_name'),
                        user_type=request.data.get('user_type'),
                        dob=make_aware(datetime.strptime(request.data.get('dob'), '%Y-%m-%d')),
                        email=user.email,
                        mobile=request.data.get('mobile'),
                        address=request.data.get('address')
                    )
                    request.session['username'] = user.username
                    request.session[user.username] = otp
                    if request.data.get('user_type') == 'Admin':
                        send_sms_view(request.data.get('mobile'), otp, user.username)
                        return render(request, 'otp_verification.html', {'otp': otp})
                    return render(template_name="success.html", request=request)
                return render(request, "registration_form.html", {'form':user_details})
        except Exception as e:
            return Response({"message" : e}, status = status.HTTP_400_BAD_REQUEST)
                
class OtpVerification(APIView):
    def get(self, request):
        return render(request, "otp_verification.html", {'msg':'Invalid OTP'})
    
    def post(self, request):
        try:
            with transaction.atomic():
                username = request.data.get('username')
                otp = request.session[username]
                if request.data.get('otp') == otp:
                    UserDetails.objects.filter(user_username = username).update(bln_verified = True)
                    user = authenticate(username=username, password=otp)
                    if user is not None:
                        login(request, user)
                        if user.user_details.user_type == 'Admin':
                            return redirect('/list_api')
                    return render(template_name="success.html", request=request)
                else:
                    return render(request, "otp_verification.html", {'msg':'Invalid OTP'})

        except Exception as e:
            return Response({"message" : e}, status = status.HTTP_400_BAD_REQUEST)
        
class ListAPI(APIView):
    def get(self, request):
        data = UserDetails.objects.filter(user_type = 'User').values()
        return render(request, "list.html", {'data':data})
    
    def post(self, request, user_id=None):
        details = UserDetails.objects.get(user_id = user_id)
        msg = """
        Registration done successfully
        Your username is {username}
        Your one time password is {otp}
        """.format(
            otp = request.session[details.user.username],
            username = details.user.username
        )
        send_reg_mail(details.email, msg)
        data = UserDetails.objects.filter(user_type = 'User').values()
        return render(request, "list.html", {'data':data})