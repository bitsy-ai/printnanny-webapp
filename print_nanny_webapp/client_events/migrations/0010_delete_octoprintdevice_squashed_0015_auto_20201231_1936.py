# Generated by Django 3.1.7 on 2021-04-28 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('client_events', '0010_delete_octoprintdevice'), ('client_events', '0011_predicteventimage'), ('client_events', '0012_auto_20201230_1710'), ('client_events', '0013_auto_20201231_1522'), ('client_events', '0014_auto_20201231_1909'), ('client_events', '0015_auto_20201231_1936')]

    dependencies = [
        ('client_events', '0002_predictsession_channel_name_squashed_0009_auto_20201228_1434'),
        ('remote_control', '0007_auto_20201229_2309'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.DeleteModel(
            name='OctoPrintDevice',
        ),
        migrations.CreateModel(
            name='ObjectDetectEventImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField()),
                ('uuid', models.CharField(db_index=True, max_length=255)),
                ('original_image', models.ImageField(upload_to='uploads/predict_event_original_image/%Y/%m/%d/')),
                ('annotated_image', models.ImageField(upload_to='uploads/predict_annotated_image/%Y/%m/%d/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='octoprintevent',
            name='event_type',
            field=models.CharField(choices=[('ClientAuthed', 'ClientAuthed'), ('ClientClosed', 'ClientClosed'), ('ClientDeauthed', 'ClientDeauthed'), ('ClientOpened', 'ClientOpened'), ('SettingsUpdated', 'SettingsUpdated'), ('FileAdded', 'FileAdded'), ('FileRemoved', 'FileRemoved'), ('FolderAdded', 'FolderAdded'), ('FolderRemoved', 'FolderRemoved'), ('TransferDone', 'TransferDone'), ('TransferFailed', 'TransferFailed'), ('TransferStarted', 'TransferStarted'), ('UpdatedFiles', 'UpdatedFiles'), ('Upload', 'Upload'), ('CaptureDone', 'CaptureDone'), ('CaptureFailed', 'CaptureFailed'), ('CaptureStart', 'CaptureStart'), ('MovieDone', 'MovieDone'), ('MovieFailed', 'MovieFailed'), ('MovieRendering', 'MovieRendering'), ('PostRollEnd', 'PostRollEnd'), ('PostRollStart', 'PostRollStart'), ('SlicingCancelled', 'SlicingCancelled'), ('SlicingDone', 'SlicingDone'), ('SlicingFailed', 'SlicingFailed'), ('SlicingProfileAdded', 'SlicingProfileAdded'), ('SlicingProfileDeleted', 'SlicingProfileDeleted'), ('SlicingProfileModified', 'SlicingProfileModified'), ('SlicingStarted', 'SlicingStarted'), ('Connected', 'Connected'), ('Disconnected', 'Disconnected'), ('PrinterReset', 'PrinterReset'), ('PrinterProfileAdded', 'PrinterProfileAdded'), ('PrinterProfileDeleted', 'PrinterProfileDeleted'), ('PrinterProfileModified', 'PrinterProfileModified'), ('PrintProgress', 'PrintProgress'), ('Error', 'Error'), ('PrintCancelled', 'PrintCancelled'), ('PrintCancelling', 'PrintCancelling'), ('PrintDone', 'PrintDone'), ('PrintFailed', 'PrintFailed'), ('PrintPaused', 'PrintPaused'), ('PrintResumed', 'PrintResumed'), ('PrintStarted', 'PrintStarted'), ('Shutdown', 'Shutdown'), ('Startup', 'Startup')], db_index=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='octoprintevent',
            name='event_type',
            field=models.CharField(choices=[('ClientAuthed', 'ClientAuthed'), ('ClientClosed', 'ClientClosed'), ('ClientDeauthed', 'ClientDeauthed'), ('ClientOpened', 'ClientOpened'), ('SettingsUpdated', 'SettingsUpdated'), ('FileAdded', 'FileAdded'), ('FileRemoved', 'FileRemoved'), ('FolderAdded', 'FolderAdded'), ('FolderRemoved', 'FolderRemoved'), ('TransferDone', 'TransferDone'), ('TransferFailed', 'TransferFailed'), ('TransferStarted', 'TransferStarted'), ('UpdatedFiles', 'UpdatedFiles'), ('Upload', 'Upload'), ('CaptureDone', 'CaptureDone'), ('CaptureFailed', 'CaptureFailed'), ('CaptureStart', 'CaptureStart'), ('MovieDone', 'MovieDone'), ('MovieFailed', 'MovieFailed'), ('MovieRendering', 'MovieRendering'), ('PostRollEnd', 'PostRollEnd'), ('PostRollStart', 'PostRollStart'), ('SlicingCancelled', 'SlicingCancelled'), ('SlicingDone', 'SlicingDone'), ('SlicingFailed', 'SlicingFailed'), ('SlicingProfileAdded', 'SlicingProfileAdded'), ('SlicingProfileDeleted', 'SlicingProfileDeleted'), ('SlicingProfileModified', 'SlicingProfileModified'), ('SlicingStarted', 'SlicingStarted'), ('Connected', 'Connected'), ('Disconnected', 'Disconnected'), ('PrinterReset', 'PrinterReset'), ('PrinterStateChanged', 'PrinterStateChanged'), ('FirmwareData', 'FirmwareData'), ('PrinterProfileAdded', 'PrinterProfileAdded'), ('PrinterProfileDeleted', 'PrinterProfileDeleted'), ('PrinterProfileModified', 'PrinterProfileModified'), ('PrintProgress', 'PrintProgress'), ('Error', 'Error'), ('PrintCancelled', 'PrintCancelled'), ('PrintCancelling', 'PrintCancelling'), ('PrintDone', 'PrintDone'), ('PrintFailed', 'PrintFailed'), ('PrintPaused', 'PrintPaused'), ('PrintResumed', 'PrintResumed'), ('PrintStarted', 'PrintStarted'), ('Shutdown', 'Shutdown'), ('Startup', 'Startup')], db_index=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='octoprintevent',
            name='event_type',
            field=models.CharField(choices=[('ClientAuthed', 'ClientAuthed'), ('ClientClosed', 'ClientClosed'), ('ClientDeauthed', 'ClientDeauthed'), ('ClientOpened', 'ClientOpened'), ('SettingsUpdated', 'SettingsUpdated'), ('UserLoggedIn', 'User Logged In'), ('UserLoggedOut', 'User Logged Out'), ('FileAdded', 'FileAdded'), ('FileRemoved', 'FileRemoved'), ('FolderAdded', 'FolderAdded'), ('FolderRemoved', 'FolderRemoved'), ('TransferDone', 'TransferDone'), ('TransferFailed', 'TransferFailed'), ('TransferStarted', 'TransferStarted'), ('UpdatedFiles', 'UpdatedFiles'), ('Upload', 'Upload'), ('CaptureDone', 'CaptureDone'), ('CaptureFailed', 'CaptureFailed'), ('CaptureStart', 'CaptureStart'), ('MovieDone', 'MovieDone'), ('MovieFailed', 'MovieFailed'), ('MovieRendering', 'MovieRendering'), ('PostRollEnd', 'PostRollEnd'), ('PostRollStart', 'PostRollStart'), ('SlicingCancelled', 'SlicingCancelled'), ('SlicingDone', 'SlicingDone'), ('SlicingFailed', 'SlicingFailed'), ('SlicingProfileAdded', 'SlicingProfileAdded'), ('SlicingProfileDeleted', 'SlicingProfileDeleted'), ('SlicingProfileModified', 'SlicingProfileModified'), ('SlicingStarted', 'SlicingStarted'), ('Connected', 'Connected'), ('Disconnected', 'Disconnected'), ('PrinterReset', 'PrinterReset'), ('PrinterStateChanged', 'PrinterStateChanged'), ('FirmwareData', 'FirmwareData'), ('PrinterProfileAdded', 'PrinterProfileAdded'), ('PrinterProfileDeleted', 'PrinterProfileDeleted'), ('PrinterProfileModified', 'PrinterProfileModified'), ('PrintProgress', 'PrintProgress'), ('Error', 'Error'), ('PrintCancelled', 'PrintCancelled'), ('PrintCancelling', 'PrintCancelling'), ('PrintDone', 'PrintDone'), ('PrintFailed', 'PrintFailed'), ('PrintPaused', 'PrintPaused'), ('PrintResumed', 'PrintResumed'), ('PrintStarted', 'PrintStarted'), ('Shutdown', 'Shutdown'), ('Startup', 'Startup')], db_index=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='octoprintevent',
            name='event_type',
            field=models.CharField(choices=[('ClientAuthed', 'ClientAuthed'), ('ClientClosed', 'ClientClosed'), ('ClientDeauthed', 'ClientDeauthed'), ('ClientOpened', 'ClientOpened'), ('SettingsUpdated', 'SettingsUpdated'), ('UserLoggedIn', 'User Logged In'), ('UserLoggedOut', 'User Logged Out'), ('FileAdded', 'FileAdded'), ('FileRemoved', 'FileRemoved'), ('FolderAdded', 'FolderAdded'), ('FolderRemoved', 'FolderRemoved'), ('TransferDone', 'TransferDone'), ('TransferFailed', 'TransferFailed'), ('TransferStarted', 'TransferStarted'), ('UpdatedFiles', 'UpdatedFiles'), ('Upload', 'Upload'), ('CaptureDone', 'CaptureDone'), ('CaptureFailed', 'CaptureFailed'), ('CaptureStart', 'CaptureStart'), ('MovieDone', 'MovieDone'), ('MovieFailed', 'MovieFailed'), ('MovieRendering', 'MovieRendering'), ('PostRollEnd', 'PostRollEnd'), ('PostRollStart', 'PostRollStart'), ('SlicingCancelled', 'SlicingCancelled'), ('SlicingDone', 'SlicingDone'), ('SlicingFailed', 'SlicingFailed'), ('SlicingProfileAdded', 'SlicingProfileAdded'), ('SlicingProfileDeleted', 'SlicingProfileDeleted'), ('SlicingProfileModified', 'SlicingProfileModified'), ('SlicingStarted', 'SlicingStarted'), ('Connected', 'Connected'), ('Disconnected', 'Disconnected'), ('PrinterReset', 'PrinterReset'), ('PrinterStateChanged', 'PrinterStateChanged'), ('FirmwareData', 'FirmwareData'), ('PrinterProfileAdded', 'PrinterProfileAdded'), ('PrinterProfileDeleted', 'PrinterProfileDeleted'), ('PrinterProfileModified', 'PrinterProfileModified'), ('PrintProgress', 'PrintProgress'), ('plugin_pi_support_throttle_state', 'plugin_pi_support_throttle_state'), ('Error', 'Error'), ('PrintCancelled', 'PrintCancelled'), ('PrintCancelling', 'PrintCancelling'), ('PrintDone', 'PrintDone'), ('PrintFailed', 'PrintFailed'), ('PrintPaused', 'PrintPaused'), ('PrintResumed', 'PrintResumed'), ('PrintStarted', 'PrintStarted'), ('Shutdown', 'Shutdown'), ('Startup', 'Startup')], db_index=True, max_length=255),
        ),
    ]
