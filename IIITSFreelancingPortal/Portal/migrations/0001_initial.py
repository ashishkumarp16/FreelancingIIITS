# Generated by Django 2.1.1 on 2018-10-14 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_application', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommunicationLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isCreditVerified', models.BooleanField(default=False)),
                ('time_of_selection', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField(default=None)),
                ('bio', models.TextField(default=None, max_length=500)),
                ('image', models.ImageField(upload_to='profiles')),
                ('batchYear', models.CharField(choices=[('None', 'None'), ('UG-1', 'UG-1'), ('UG-2', 'UG-2'), ('UG-3', 'UG-3'), ('UG-4', 'UG-4'), ('MS', 'MS'), ('Ph.D', 'Ph.D')], default='None', max_length=4)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HoursOfWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(blank=True, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default=None, max_length=300)),
                ('hasRead', models.BooleanField(default=False)),
                ('receivingTime', models.DateTimeField()),
                ('_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.CustomUser')),
                ('_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_from', to='Portal.CustomUser')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=30)),
                ('description', models.CharField(default=None, max_length=100)),
                ('postedOn', models.DateTimeField(auto_now_add=True)),
                ('isCompleted', models.BooleanField(default=False)),
                ('deadline', models.DateField()),
                ('task_count', models.IntegerField(default=0)),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.CustomUser')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=30)),
                ('addedOn', models.DateTimeField(auto_now_add=True)),
                ('credits', models.CharField(max_length=20)),
                ('task_description', models.CharField(default=None, max_length=100)),
                ('isCompleted', models.BooleanField(default=False)),
                ('deadline', models.DateField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.Project')),
            ],
        ),
        migrations.CreateModel(
            name='TaskRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(choices=[(1, 'Worst'), (1.5, 'Bad'), (2, 'NotSoGood'), (2.5, 'Average'), (3, 'OK'), (3.5, 'QuietGood'), (4, 'Better'), (4.5, 'Great'), (5, 'Amazing')], decimal_places=1, default=3.5, max_digits=2)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.Task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.CustomUser')),
            ],
        ),
        migrations.CreateModel(
            name='TaskSkillsRequired',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proficiency_level_required', models.IntegerField(choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced')], default=1)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.Skill')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.Task')),
            ],
        ),
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(choices=[(1, 'Worst'), (1.5, 'Bad'), (2, 'NotSoGood'), (2.5, 'Average'), (3, 'OK'), (3.5, 'QuietGood'), (4, 'Better'), (4.5, 'Great'), (5, 'Amazing')], decimal_places=1, default=3.5, max_digits=2)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.Project')),
                ('rating_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.CustomUser')),
                ('rating_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_by', to='Portal.CustomUser')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.Task')),
            ],
        ),
        migrations.CreateModel(
            name='UsersCommunicationLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_of_fluency', models.IntegerField(choices=[(1, 'Good'), (2, 'VeryGood'), (3, 'Excellent')], default=1)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.CommunicationLanguage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.CustomUser')),
            ],
        ),
        migrations.CreateModel(
            name='UsersSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_of_proficiency', models.IntegerField(choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced')], default=1)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.Skill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.CustomUser')),
            ],
        ),
        migrations.AddField(
            model_name='hoursofwork',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.Task'),
        ),
        migrations.AddField(
            model_name='hoursofwork',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.CustomUser'),
        ),
        migrations.AddField(
            model_name='contributor',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.Task'),
        ),
        migrations.AddField(
            model_name='contributor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.CustomUser'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.Task'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.CustomUser'),
        ),
    ]