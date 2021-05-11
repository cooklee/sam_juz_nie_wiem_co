# Generated by Django 3.2.2 on 2021-05-11 10:17

from django.db import migrations, models
import django.db.models.deletion
import filmy.models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0003_auto_20210511_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directed_by', to='filmy.person', verbose_name='reżyser'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='screen_play',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='written_by', to='filmy.person', verbose_name='scenażysta'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(null=True, validators=[filmy.models.check_year], verbose_name='rok'),
        ),
        migrations.CreateModel(
            name='TvShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('year', models.IntegerField()),
                ('owner', models.IntegerField(choices=[(1, 'Netflix'), (2, 'HBO'), (3, 'Amazon'), (4, 'Disney')])),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filmy.person')),
            ],
        ),
    ]