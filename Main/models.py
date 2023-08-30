from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model
import datetime


class UserManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None):
        if not email:
            raise ValueError("Email is required.")
        if not phone_number:
            raise ValueError("Phone number is required.")

        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
        )
        user.set_password(password) 
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']
    
    def __str__(self):
        return self.email
    
    def create_superuser(self, email, phone_number, password=None):
        user = self.create_user(email=email, phone_number=phone_number, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UserRegistration(AbstractBaseUser):
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128, null=True, blank=True) 

 

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['password']

    objects = UserManager()

    def __str__(self):
        return self.phone_number

class Group(models.Model):
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='admin_of')
    chair = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='chair_of')
    signatories = models.ManyToManyField(CustomUser, related_name='signatories')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.admin)
    
class CreateGroup(models.Model):
    GROUP_TYPES = [
        ('savings', 'Savings Group'),
        ('loan', 'Loan Group'),
    ]
    
    GROUP_ROLES = [
        ('admin', 'Admin'),
        ('member', 'Member'),
    ]
    
    CURRENCIES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('KES', 'Kenyan Shilling'),
    ]

    group_name = models.CharField(max_length=100, null=True, blank=True)
    number_of_members = models.PositiveIntegerField()
    group_type = models.CharField(max_length=20, choices=GROUP_TYPES, null=True, blank=True)
    group_role = models.CharField(max_length=20, choices=GROUP_ROLES, null=True, blank=True)
    country_of_operation = models.CharField(max_length=50, null=True, blank=True)
    group_currency = models.CharField(max_length=3, choices=CURRENCIES, null=True, blank=True)

    def __str__(self):
        return self.group_name


class Contribution(models.Model):
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True) 
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=datetime.date.today)  # Set default to current date
        
    def __str__(self):
        return str(self.amount)


class Loan(models.Model):
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    repayment_months = models.PositiveIntegerField()
    is_repaid = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.amount)

    
class LoanFunding(models.Model):
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    amount_funded = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=datetime.date.today)  # Set default to current date

    def __str__(self):
        return str(self.amount_funded)
    
    
class LoanRepayment(models.Model):
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=datetime.date.today)  # Set default to current date

    def __str__(self):
        return str(self.amount)


class Interest(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=datetime.date.today)  # Set default to current date

    def __str__(self):
        return str(self.date)

class Fee(models.Model):
    short_name = models.CharField(max_length=50)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.description

class LoanExpenditure(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    budgeted_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_spent = models.DecimalField(max_digits=10, decimal_places=2)
    last_spent_date = models.DateField()

    def __str__(self):
        return str(self.amount_spent)

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.PositiveIntegerField()
    country=models.CharField(max_length=50)
    group = models.ForeignKey(CreateGroup, on_delete=models.DO_NOTHING, null=True, default=None)

    def __str__(self):
        return self.last_name
    
    
User = get_user_model()

class UserGroupMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(CreateGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f"{str(self.user)} - {str(self.group)}"


 
        

