# Generated by Django 5.0.1 on 2024-01-23 06:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBlogs', '0004_blog_post_alter_blog_category_blogcat_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='blog_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]