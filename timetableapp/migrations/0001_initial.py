# Generated by Django 2.0.2 on 2019-01-03 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=10)),
                ('theory_hours', models.IntegerField()),
                ('practical_hours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LoadAllocate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=10, null=True)),
                ('theory_hours', models.IntegerField()),
                ('pract_hours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('sub_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('semester', models.IntegerField()),
                ('theory_hours', models.IntegerField()),
                ('practical_hours', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='faculty',
            name='sub_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetableapp.Subject'),
        ),
    ]