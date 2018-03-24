# Generated by Django 2.0.3 on 2018-03-24 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_title', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, default='uploads/200/default.png', upload_to='uploads/200/')),
                ('is_active', models.BooleanField(default=True)),
                ('activation_code', models.CharField(max_length=50)),
                ('password_reset_code', models.CharField(default=0, max_length=50)),
                ('role', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Users.Role')),
            ],
        ),
    ]