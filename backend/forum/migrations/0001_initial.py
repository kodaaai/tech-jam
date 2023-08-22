# Generated by Django 4.2.4 on 2023-08-22 08:00

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
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, editable=False, null=True, verbose_name='deleted date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('name', models.CharField(max_length=20, verbose_name='タグ名')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
            ],
            options={
                'verbose_name': 'タグ',
                'verbose_name_plural': 'タグ',
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, editable=False, null=True, verbose_name='deleted date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('body', models.TextField(max_length=1000, verbose_name='質問内容')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '未解決'), (1, '解決しました')], default=0, verbose_name='ステータス')),
                ('tags', models.ManyToManyField(to='forum.tags', verbose_name='担当教員名')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='投稿者')),
            ],
            options={
                'verbose_name': '質問記事',
                'verbose_name_plural': '質問記事',
                'db_table': 'questions',
            },
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, editable=False, null=True, verbose_name='deleted date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('body', models.TextField(max_length=1000, verbose_name='コメント')),
                ('questions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='forum.questions', verbose_name='質問記事')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='回答者')),
            ],
            options={
                'verbose_name': '回答コメント',
                'verbose_name_plural': '回答コメント',
                'db_table': 'answers',
            },
        ),
    ]