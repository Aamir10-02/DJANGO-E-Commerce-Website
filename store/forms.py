from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile

class UserInfoForm(forms.ModelForm):
	phone = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}), required=False)
	address = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}), required=False)
	address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 2'}), required=False)
	city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), required=False)
	state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}), required=False)
	zip_code = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}), required=False)
	country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}), required=False)

	class Meta:
		model = Profile
		fields = ('phone', 'address', 'address2', 'city', 'state', 'zip_code', 'country')

class ChangePasswordForm(SetPasswordForm):
	class Meta:
		model = User
		fields = ['new_password1', 'new_password2']
	def __init__(self, *args, **kwargs):
		super(ChangePasswordForm, self).__init__(*args, **kwargs)

		self.fields['new_password1'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Password'
        })
		
		self.fields['new_password1'].help_text = '''
            <ul class="form-help-list">
                <li>Your password can't be too similar to your other personal information.</li>
                <li>Your password must contain at least 8 characters.</li>
                <li>Your password can't be a commonly used password.</li>
                <li>Your password can't be entirely numeric.</li>
            </ul>
        '''
		
		self.fields['new_password2'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Confirm Password'
        })
		
		self.fields['new_password2'].help_text = '<span class="form-help">Enter the same password as before, for verification.</span>'
class UpdateUserForm(UserChangeForm):
    password = None
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Email Address'
        })
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'First Name'
        })
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Last Name'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'User Name'
        })
        self.fields['username'].label = ''
       
        self.fields['username'].help_text = 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
		
class SignUpForm(UserCreationForm):
	    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Email Address'
        }),
        required=False
    )
first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'First Name'
        }),
        required=False
    )

last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Last Name'
        }),
        required=False
    )
class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
		
		def __init__(self, *args, **kwargs):
			super(SignUpForm, self).__init__(*args, **kwargs)
			
			self.fields['username'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Username'
        })
			self.fields['username'].label = ''
			self.fields['username'].help_text = '<div class="form-help">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</div>'
			
			self.fields['password1'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Password'
        })
			self.fields['password1'].label = ''
			self.fields['password1'].help_text = '''
            <ul class="form-help-list">
                <li>Your password can't be too similar to your other personal information</li>
                <li>Your password must contain at least 8 characters</li>
                <li>Your password can't be a commonly used password</li>
                <li>Your password can't be entirely numeric</li>
            </ul>
        '''
			self.fields['password2'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Confirm Password'
        })
			self.fields['password2'].label = ''
			self.fields['password2'].help_text = '<div class="form-help">Enter the same password as before, for verification.</div>'