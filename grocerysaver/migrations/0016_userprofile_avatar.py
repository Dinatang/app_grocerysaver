import django.core.validators
import grocerysaver.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocerysaver', '0015_devicesensorreading'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=grocerysaver.models.user_avatar_upload_to,
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=['jpg', 'jpeg', 'png', 'webp'],
                    ),
                ],
            ),
        ),
    ]
