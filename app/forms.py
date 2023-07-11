from django import forms

class StudentForm(forms.Form):
    sname = forms.CharField(max_length=30)
    sage = forms.IntegerField()
    email = forms.EmailField()
    remail = forms.EmailField()
    
    botcatcher = forms.CharField(max_length=10,widget=forms.HiddenInput, required=False)
    
    def clean(self):
        em = self.cleaned_data["email"]
        rem = self.cleaned_data["remail"]
        if em != rem:
            raise forms.ValidationError('email not matching')

    def clean_botcatcher(self):
        bot = self.cleaned_data["botcatcher"]
        if len(bot)>0:
            raise forms.ValidationError('Bot Detected')
    
    