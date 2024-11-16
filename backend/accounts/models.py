from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, work_email, phone_number, password=None):
        if not work_email:
            raise ValueError('Users must provide an email address')
        
        if not password:
            raise ValueError("Password must be provided")
        
        user=self.model(
            work_email=self.normalize_email(work_email),
            #it will take the email uppercase and convert it to lowercase
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        #this method encodes the password provided by the user
        user.save(using=self._db)
        #this define the database which the system will use to store the model data
        return user
    
    #this is the method to create a super user whoch comes after creating a basic user
    def create_superuser(self, first_name, last_name, work_email, phone_number, password):
        
        #calls the create-user to create a user then assign superuser permissions
        user=self.create_user(
            work_email=self.normalize_email(work_email),
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class RecordsUserAccount(AbstractBaseUser):
    
    #this provides choice to choose a user for the proxy model
    class UserTypes(models.TextChoices):
        RECORDSMANAGER = "RECORDS MANAGER", "Records Manager"
        RECORDSOFFICER = "RECORDS OFFICER", "Records Officer"

    type = models.CharField(max_length=20, choices=UserTypes.choices, default=UserTypes.RECORDSOFFICER)
    work_email = models.EmailField(max_length=50, unique=True, blank=False)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    phone_number = PhoneNumberField(region = 'KE')

    #booleanfields can track user permissions and roles
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    #these will be special permissions that will define whether
    #the user is a records officer or a records manager
    is_recordsofficer = models.BooleanField(default=False)
    is_recordsmanager = models.BooleanField(default=False)

    USERNAME_FIELD = 'work_email'

    #defining the manager for the RecordsUserAccount model
    objects = UserAccountManager()

    def __str__ (self):
        return self.work_email
    
    #checks if the user has specific permissions and returns true if an admin and false if not
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return self.is_admin or self.is_staff
    #app = module
    #this line is used to determine whether a user has permission to access a particular module in the app
    #setting return to True means all user have access to permissions
    #but by setting return to the above this restricts access to users who do not have these roles

    def save(self, *args, **kwargs):
        #the type below refers to the type model field in the RecordsUserAccount model
        if not self.type or self.type == None :
            self.type = RecordsUserAccount.UserTypes.RECORDSOFFICER
            return super ().save(self, *args, **kwargs)
        #this ensures that a user type is assigned as records officer by default when a user is not assigned


#after adding the AUTH_USER_MODEL in the settings.py file i will create separate models
#for records officer and records manager each with their manager models 
#this prevents the proxy model from inheriting the parent model which is the RecordsUserAccount model

#in the managers of the users below i have used create user to create the records manager and officer users
class RecordsOfficerManager(models.Manager):
    def create_user(self, first_name, last_name, work_email, phone_number, password=None):
        if not work_email or len(work_email) <= 0 :
            raise ValueError('Users must provide an email address')
        
        if not password:
            raise ValueError("Password must be provided")
        
        work_email = work_email.lower()

        user = self.model(
            work_email=self.normalize_email(work_email),
            #it will take the email uppercase and convert it to lowercase
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        #this method encodes the password provided by the user
        user.save(using=self._db)
        #this define the database which the system will use to store the model data
        return user
    
    def get_queryset(self, *args, **kwargs):
            queryset = super().get_queryset(*args, **kwargs)
            queryset = queryset.filter(type = RecordsUserAccount.UserTypes.RECORDSOFFICER)
            return queryset
    #customizes the queryset to return records officer instances from the databases

#a proxy model will not operate from its own database but from the original database table that has been inherited
class RecordsOfficer(RecordsUserAccount):
    class Meta:
        proxy = True

    #defining the manager for this model
    objects  = RecordsOfficerManager

    def save(self, *args, **kwargs):
        self.type = RecordsUserAccount.UserTypes.RECORDSOFFICER
        self.is_recordsofficer = True
        return super () .save(*args, **kwargs)
    


class RecordsManagerManager(models.Manager):
    def create_user(self, first_name, last_name, work_email, phone_number, password=None):
        if not work_email:
            raise ValueError('Users must provide an email address')
        
        if not password:
            raise ValueError("Password must be provided")
        
        user=self.model(
            work_email=self.normalize_email(work_email),
            #it will take the email uppercase and convert it to lowercase
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        #this method encodes the password provided by the user
        user.save(using=self._db)
        #this define the database which the system will use to store the model data
        return user
    
    def get_queryset(self, *args, **kwargs):
            queryset = super().get_queryset(*args, **kwargs)
            queryset = queryset.filter(type = RecordsUserAccount.UserTypes.RECORDSMANAGER)
            return queryset
    #customizes the queryset to return records officer instances from the databases

class RecordsManager(RecordsUserAccount):
    class Meta:
        proxy = True

    #defining the manager for this model
    objects  = RecordsManagerManager

    def save(self, *args, **kwargs):
        self.type = RecordsUserAccount.UserTypes.RECORDSMANAGER
        self.is_recordsmanager = True
        return super().save(*args, **kwargs)