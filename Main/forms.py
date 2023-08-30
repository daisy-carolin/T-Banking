from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = "__all__"


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = "__all__"

class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = CreateGroup
        fields = "__all__"


class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = "__all__"


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = "__all__"


class LoanFundingForm(forms.ModelForm):
    class Meta:
        model = LoanFunding
        fields = "__all__"


class LoanRepaymentForm(forms.ModelForm):
    class Meta:
        model = LoanRepayment
        fields = "__all__"


class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = "__all__"


class FeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = "__all__"


class LoanExpenditureForm(forms.ModelForm):
    class Meta:
        model = LoanExpenditure
        fields = "__all__"

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member  
        fields = "__all__" 


class DeleteMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = "__all__"
