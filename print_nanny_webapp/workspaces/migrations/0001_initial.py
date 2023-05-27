# Generated by Django 4.1.7 on 2023-05-22 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import organizations.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Workspace",
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
                (
                    "name",
                    models.CharField(
                        help_text="The name of the organization", max_length=200
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "created",
                    organizations.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "modified",
                    organizations.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "slug",
                    organizations.fields.SlugField(
                        blank=True,
                        editable=False,
                        help_text="The name in all lowercase, suitable for URL identification",
                        max_length=200,
                        populate_from="name",
                        unique=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "organization",
                "verbose_name_plural": "organizations",
                "ordering": ["name"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="WorkspaceUser",
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
                (
                    "created",
                    organizations.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "modified",
                    organizations.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                ("is_admin", models.BooleanField(default=False)),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organization_users",
                        to="workspaces.workspace",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "organization user",
                "verbose_name_plural": "organization users",
                "ordering": ["organization", "user"],
                "abstract": False,
                "unique_together": {("user", "organization")},
            },
        ),
        migrations.CreateModel(
            name="WorkspaceOwner",
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
                (
                    "created",
                    organizations.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "modified",
                    organizations.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "organization",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owner",
                        to="workspaces.workspace",
                    ),
                ),
                (
                    "organization_user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="workspaces.workspaceuser",
                    ),
                ),
            ],
            options={
                "verbose_name": "organization owner",
                "verbose_name_plural": "organization owners",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="WorkspaceInvitation",
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
                ("guid", models.UUIDField(editable=False)),
                (
                    "invitee_identifier",
                    models.CharField(
                        help_text="The contact identifier for the invitee, email, phone number, social media handle, etc.",
                        max_length=1000,
                    ),
                ),
                (
                    "created",
                    organizations.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "modified",
                    organizations.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "invited_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_sent_invitations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "invitee",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_invitations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organization_invites",
                        to="workspaces.workspace",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="workspace",
            name="users",
            field=models.ManyToManyField(
                related_name="%(app_label)s_%(class)s",
                through="workspaces.WorkspaceUser",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
