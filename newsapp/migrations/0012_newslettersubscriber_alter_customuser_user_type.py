# Generated by Django 5.2.1 on 2025-07-26 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0011_alter_customuser_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterSubscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subscribed_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Newsletter Subscriber',
                'verbose_name_plural': 'Newsletter Subscribers',
            },
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'admin'), (2, 'subadmin')], default=1, max_length=50),
        ),
    ]
