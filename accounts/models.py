from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
        NONE = "N", "None"

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(
        max_length=13,
        validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")],
        blank=True
    )
    gender = models.CharField(
        max_length=1,
        choices=GenderChoices.choices,
        default=GenderChoices.NONE,
        blank=True
    )
    avatar = models.ImageField(
        blank=True, upload_to="accounts/avatar/%Y/%m/%d",
        help_text="48px * 48px 크기의 png/jpg 파일을 업로드해주세요."
    )

    @property
    def name(self):
        return f"{self.username}"
