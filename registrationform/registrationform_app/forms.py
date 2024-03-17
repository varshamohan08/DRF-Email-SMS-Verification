from django import forms
from datetime import datetime, timezone


class OTPForm(forms.Form):
    username = forms.CharField()
    otp = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        dob = cleaned_data.get("dob")

        if datetime.now().year - dob.replace(tzinfo=None).year  < 18:
            msg = "User age must be over 18."
            # self.add_error("dob", msg)
            self._errors['dob'] = self.error_class([ msg])

class UserForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    user_type = forms.CharField()
    mobile = forms.IntegerField()
    email = forms.CharField()
    dob = forms.DateTimeField()
    address = forms.TextInput()

    def clean(self):
        # import pdb;pdb.set_trace()
        cleaned_data = super().clean()
        dob = cleaned_data.get("dob")

        if datetime.now().year - dob.replace(tzinfo=None).year  < 18:
            msg = "User age must be over 18."
            # self.add_error("dob", msg)
            self._errors['dob'] = self.error_class([ msg])
