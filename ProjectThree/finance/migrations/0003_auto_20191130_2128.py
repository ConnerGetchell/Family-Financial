# Generated by Django 2.2.4 on 2019-11-30 21:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finance', '0002_auto_20191130_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='debt',
            name='user',
        ),
        migrations.RemoveField(
            model_name='earning',
            name='user',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='user',
        ),
        migrations.RemoveField(
            model_name='investment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='spending',
            name='user',
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Family')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='debt',
            name='Member_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='debt', to='finance.Member'),
        ),
        migrations.AddField(
            model_name='earning',
            name='Member_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='earning', to='finance.Member'),
        ),
        migrations.AddField(
            model_name='goal',
            name='Member_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='goal', to='finance.Member'),
        ),
        migrations.AddField(
            model_name='investment',
            name='Member_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='investment', to='finance.Member'),
        ),
        migrations.AddField(
            model_name='spending',
            name='Member_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='spending', to='finance.Member'),
        ),
    ]
