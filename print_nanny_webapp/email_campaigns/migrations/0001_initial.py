# Generated by Django 3.2.12 on 2022-10-28 05:46

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Campaign",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deleted", models.DateTimeField(editable=False, null=True)),
                ("created_dt", models.DateTimeField(auto_now_add=True)),
                ("template", models.CharField(max_length=255)),
                ("subject", models.CharField(max_length=255)),
                ("send_fn", models.CharField(max_length=255)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="EmailMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deleted", models.DateTimeField(editable=False, null=True)),
                ("message_id", models.CharField(max_length=255, null=True)),
                (
                    "send_status",
                    models.CharField(
                        choices=[
                            (
                                "sent",
                                "the ESP has sent the message (though it may or may not get delivered)",
                            ),
                            (
                                "queued",
                                "the ESP has accepted the message and will try to send it (possibly later)",
                            ),
                            ("invalid", "the recipient email was not valid"),
                            ("rejected", "the recipient is denylisted"),
                            (
                                "failed",
                                "the attempt to send failed for some other reason",
                            ),
                            ("unknown", "Unknown"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "campaign",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="email_campaigns.campaign",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EmailTrackingEvent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deleted", models.DateTimeField(editable=False, null=True)),
                (
                    "event_type",
                    models.CharField(
                        choices=[
                            (
                                "queued",
                                "the ESP has accepted the message and will try to send it (possibly later)",
                            ),
                            (
                                "sent",
                                "the ESP has sent the message (though it may or may not get delivered)",
                            ),
                            (
                                "rejected",
                                "the ESP refused to send the messsage (e.g., suppression list, policy, invalid email)",
                            ),
                            (
                                "failed",
                                "the ESP was unable to send the message (e.g., template rendering error)",
                            ),
                            ("bounced", "rejected or blocked by receiving MTA"),
                            (
                                "deferred",
                                "delayed by receiving MTA; should be followed by a later BOUNCED or DELIVERED",
                            ),
                            ("delivered", "accepted by receiving MTA"),
                            ("autoresponded", "a bot replied"),
                            ("opened", "open tracking"),
                            ("clicked", "click tracking"),
                            (
                                "complained",
                                "recipient reported as spam (e.g., through feedback loop)",
                            ),
                            ("unsubscribed", "recipient attempted to unsubscribe"),
                            (
                                "subscribed",
                                "signed up for mailing list through ESP-hosted form",
                            ),
                            ("inbound", "received message"),
                            ("inbound_failed", "inbound message delivery failed"),
                            ("unknown", "Unknown"),
                        ],
                        max_length=255,
                    ),
                ),
                ("message_id", models.CharField(db_index=True, max_length=255)),
                ("ts", models.DateTimeField()),
                ("event_id", models.CharField(max_length=255, null=True)),
                ("recipient", models.CharField(max_length=255, null=True)),
                ("metadata", models.JSONField()),
                (
                    "tags",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=255),
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "reject_reason",
                    models.CharField(
                        choices=[
                            ("invalid", "bad address format"),
                            ("bounced", "(previous) bounce from recipient"),
                            (
                                "timed_out",
                                "(previous) repeated failed delivery attempts",
                            ),
                            ("blocked", "ESP policy suppression"),
                            ("spam", "(previous) spam complaint from recipient"),
                            (
                                "unsubscribed",
                                "(previous) unsubscribe request from recipient",
                            ),
                            ("other", "Other"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                ("description", models.CharField(max_length=255, null=True)),
                ("mta_response", models.CharField(max_length=255, null=True)),
                ("user_agent", models.CharField(max_length=255, null=True)),
                ("click_url", models.CharField(max_length=255, null=True)),
                ("esp_event", models.JSONField()),
                (
                    "campaign",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="email_campaigns.campaign",
                    ),
                ),
                (
                    "email_message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="email_campaigns.emailmessage",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "index_together": {("campaign", "user", "event_type")},
            },
        ),
        migrations.AddConstraint(
            model_name="emailmessage",
            constraint=models.UniqueConstraint(
                condition=models.Q(("deleted", None), ("message_id__isnull", False)),
                fields=("message_id",),
                name="unique_esp_message_id",
            ),
        ),
        migrations.AlterIndexTogether(
            name="emailmessage",
            index_together={("campaign", "user", "message_id")},
        ),
    ]
