# Generated by Django 5.0 on 2023-12-24 18:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0006_alter_customer_email_alter_customer_name_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customer",
            options={
                "ordering": ("id",),
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
            },
        ),
        migrations.AlterModelOptions(
            name="faq",
            options={
                "ordering": ("order",),
                "verbose_name": "Часто задаваемые вопросы",
                "verbose_name_plural": "Часто задаваемые вопросы",
            },
        ),
        migrations.AddField(
            model_name="customer",
            name="registration_date",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Дата регистрации",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="faq",
            name="category",
            field=models.CharField(
                choices=[
                    ("DON", "Пожертвование"),
                    ("GUA", "Опекунство"),
                    ("ABT", "О нас"),
                    ("PRG", "Программы"),
                    ("GNR", "Общие вопросы"),
                ],
                default="GNR",
                max_length=3,
            ),
        ),
    ]