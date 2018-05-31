# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2018-05-31 12:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rdf_io', '0003_auto_20180531_1448'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(blank=True, max_length=255, null=True, verbose_name='term')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='term')),
                ('pref_label', models.CharField(blank=True, max_length=255, null=True, verbose_name='preferred label')),
                ('definition', models.TextField(blank=True, verbose_name='definition')),
                ('changenote', models.TextField(blank=True, verbose_name='change note')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Active'), (1, 'Draft'), (2, 'Double'), (3, 'Dispute'), (4, 'Not classified')], default=0, verbose_name='review status')),
                ('uri', models.CharField(blank=True, editable=False, max_length=250, verbose_name='main URI')),
                ('author_uri', models.CharField(blank=True, editable=False, max_length=250, verbose_name='main URI')),
                ('top_concept', models.BooleanField(default=False, verbose_name='is top concept')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_type', models.PositiveSmallIntegerField(choices=[(0, 'preferred'), (1, 'alternative'), (2, 'hidden')], default=0, verbose_name='label type')),
                ('label_text', models.CharField(max_length=100, verbose_name='label text')),
                ('language', models.CharField(choices=[('fr', 'French'), ('de', 'German'), ('en', 'English'), ('es', 'Spanish'), ('it', 'Italian'), ('pt', 'Portuguese')], default='fr', max_length=10, verbose_name='language')),
                ('uri', models.CharField(blank=True, max_length=250, verbose_name='author URI')),
                ('author_uri', models.CharField(blank=True, max_length=250, verbose_name='main URI')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('concept', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='labels', to='skosxl.Concept', verbose_name='main concept')),
                ('user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='django user')),
            ],
        ),
        migrations.CreateModel(
            name='MapRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.CharField(max_length=250, verbose_name='Target Concept URI')),
                ('match_type', models.PositiveSmallIntegerField(choices=[(0, 'matches exactly'), (1, 'matches closely'), (2, 'has a broader match'), (3, 'has a narrower match'), (4, 'has a related match')], default=1, verbose_name='Type of mapping relation')),
                ('origin_concept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='map_origin', to='skosxl.Concept', verbose_name='Local concept to map')),
            ],
            options={
                'verbose_name': 'Mapping relation',
                'verbose_name_plural': 'Mapping relations',
            },
        ),
        migrations.CreateModel(
            name='Notation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='notation')),
                ('concept', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notations', to='skosxl.Concept', verbose_name='main concept')),
                ('namespace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rdf_io.Namespace', verbose_name='namespace(type)')),
            ],
            options={
                'verbose_name': 'SKOS notation',
                'verbose_name_plural': 'notations',
            },
        ),
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pref_label', models.CharField(blank=True, max_length=255, verbose_name='label')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='pref_label')),
                ('uri', models.CharField(blank=True, max_length=250, verbose_name='main URI')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, null=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True, verbose_name='modified')),
                ('definition', models.TextField(blank=True, verbose_name='definition')),
                ('meta', models.TextField(blank=True, help_text='(<predicate> <object> ; list) ', verbose_name='additional metadata')),
            ],
        ),
        migrations.CreateModel(
            name='SchemeMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=500, verbose_name='value')),
                ('metaprop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rdf_io.GenericMetaProp')),
                ('scheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skosxl.Scheme')),
            ],
        ),
        migrations.CreateModel(
            name='SemRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rel_type', models.PositiveSmallIntegerField(choices=[(0, 'has a broader concept'), (1, 'has a narrower concept'), (2, 'has a related concept')], default=1, verbose_name='Type of semantic relation')),
                ('origin_concept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_origin', to='skosxl.Concept', verbose_name='Origin')),
                ('target_concept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_target', to='skosxl.Concept', verbose_name='Target')),
            ],
            options={
                'verbose_name': 'Semantic relation',
                'verbose_name_plural': 'Semantic relations',
            },
        ),
        migrations.AddField(
            model_name='concept',
            name='scheme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='skosxl.Scheme'),
        ),
        migrations.AddField(
            model_name='concept',
            name='sem_relatons',
            field=models.ManyToManyField(through='skosxl.SemRelation', to='skosxl.Concept', verbose_name='semantic relations'),
        ),
        migrations.AddField(
            model_name='concept',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='django user'),
        ),
        migrations.AlterUniqueTogether(
            name='concept',
            unique_together=set([('scheme', 'term')]),
        ),
    ]
