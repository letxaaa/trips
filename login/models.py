from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
  def get_all_by_email(self):
        return self.order_by('email')

  #def register(self, form_data):()
   # pw_hash = bcrypt.hashpw(form_data['password'].encode(), bcrypt.genstalt()).decode()
    #return self.create(
     # fisrt_name=form_data['first_name'],
      #last_name=form_data['last_name'],
      #password=pw_hash,
      #email=form_data['email'],
    #)      

  #def authenticate(self, email, password):
   #     users_with_email = self.filter(email=email)
    #    if not isers_with_email:
     #         return False
      #  user = users_with_email[0]
       # return bcrypt.checkpw(password.encode(), user.password.encode())

  def validate(self, form_data):
    errors = {}
    if len(form_data['first']) < 2:
      errors['first'] = 'First name should be at least 2 characters.'
    if len(form_data['last']) < 2:
      errors['last'] = 'Last name should be at least 2 characters.'

    
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(form_data['email']):             
        errors['email'] = ("Invalid email address!")

    exist_email = self.filter(email=form_data['email'])
    if exist_email:
      errors['email'] = 'Email in use already!'

    if len(form_data['password']) < 8:
      errors['password'] = "Password must be at least 3 Characters."
    
    if form_data['cpassword'] != form_data['password']:
      errors['cpassword'] = "Password did not match. "
    return errors


class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = UserManager()

  def __stf__(self):
    return f"{self.first_name}"