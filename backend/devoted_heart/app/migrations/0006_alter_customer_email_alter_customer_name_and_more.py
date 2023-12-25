# Generated by Django 4.2.8 on 2023-12-17 20:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0005_alter_customer_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="email",
            field=models.EmailField(
                help_text="Email", max_length=254, unique=True, verbose_name="Email"
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="name",
            field=models.CharField(help_text="Имя", max_length=254, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="customer",
            name="phone",
            field=models.CharField(
                help_text="Телефон", max_length=11, unique=True, verbose_name="Телефон"
            ),
        ),
    ]
