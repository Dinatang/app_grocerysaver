import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grocerysaver', '0014_cart_and_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceSensorReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accelerometer_x', models.FloatField()),
                ('accelerometer_y', models.FloatField()),
                ('accelerometer_z', models.FloatField()),
                ('gyroscope_x', models.FloatField()),
                ('gyroscope_y', models.FloatField()),
                ('gyroscope_z', models.FloatField()),
                ('is_shaking', models.BooleanField(default=False)),
                ('captured_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_sensor_readings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-captured_at', '-id'],
            },
        ),
        migrations.AddIndex(
            model_name='devicesensorreading',
            index=models.Index(fields=['user', '-captured_at'], name='grocerysave_user_id_f28409_idx'),
        ),
    ]
