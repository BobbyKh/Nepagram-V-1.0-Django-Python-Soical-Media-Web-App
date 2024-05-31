# Generated by Django 5.0.6 on 2024-05-31 11:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0007_profile_following'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myuser.comment')),
                ('follow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myuser.follow')),
                ('like', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myuser.like')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myuser.post')),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myuser.reply')),
                ('share', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myuser.share')),
            ],
        ),
    ]