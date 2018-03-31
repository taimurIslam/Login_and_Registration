from django.db import models
from imagekit.conf import ImageKitConf
from imagekit.models import ImageSpecField
from imagekit.processors import SmartResize

# User Role models
class Role(models.Model):
    role_title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.role_title
    def as_json(self):
        return dict(
            role_title = str(self.role_title),
        )
#------------------------------------------------#
# User models
class User(models.Model):
    ImageKitConf.CACHEFILE_DIR = 'uploads/200/'

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    photo = models.ImageField(upload_to='uploads/200/', default='uploads/200/default.png', blank=True)
    thumb = ImageSpecField(source = 'photo', processors=[SmartResize(200,200)],)

    role = models.ForeignKey('Role', default=1, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    activation_code = models.CharField(max_length=50)
    password_reset_code = models.CharField(max_length=50, default=0)

    def as_json(self):
        return dict(
            first_name=str(self.first_name),
            last_name=str(self.last_name),
            username=str(self.username),
            email=str(self.email),
            phone=str(self.phone),
            address=str(self.address),
            photo=str(self.photo),
            role_id=self.role_id,
            is_active=(self.is_active),
        )

    def as_json_with_password(self):
        return dict(
            id=int(self.pk),
            password=str(self.password)
        )
    def is_authenticated(self):
        pass
#------------------------------------------------------#