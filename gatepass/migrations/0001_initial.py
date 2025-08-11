from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='GatePass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gate_pass_number', models.CharField(max_length=50, unique=True)),
                ('visitor_name', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=15)),
                ('purpose', models.TextField()),
                ('date_of_entry', models.DateField()),
                ('time_of_entry', models.TimeField()),
                ('approved_by', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=10)),
                ('notes', models.TextField(blank=True, null=True)),
                ('visitor_photo', models.FileField(blank=True, null=True, upload_to='visitor_photos/')),
                ('qr_code', models.FileField(blank=True, null=True, upload_to='qr_codes/')),
            ],
        ),
    ]