# Generated by Django 4.0.4 on 2022-04-27 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video_hosting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='video_hosting.video'),
            preserve_default=False,
        ),
    ]
