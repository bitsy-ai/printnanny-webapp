# Generated by Django 3.2.9 on 2022-01-14 03:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("telemetry", "0024_telemetryevent_print_nanny_beta_client_version"),
    ]

    operations = [
        migrations.AlterField(
            model_name="telemetryevent",
            name="event_type",
            field=models.CharField(
                choices=[
                    (
                        "plugin_octoprint_nanny_monitoring_start",
                        "Print Nanny Monitoring started",
                    ),
                    (
                        "plugin_octoprint_nanny_monitoring_stop",
                        "Print Nanny Monitoring stopped",
                    ),
                    (
                        "plugin_octoprint_nanny_monitoring_reset",
                        "Print Nanny Monitoring reset",
                    ),
                    (
                        "plugin_octoprint_nanny_device_register_start",
                        "Device registration started",
                    ),
                    (
                        "plugin_octoprint_nanny_device_register_done",
                        "Device registration succeeded",
                    ),
                    (
                        "plugin_octoprint_nanny_device_register_failed",
                        "Device registration failed",
                    ),
                    ("plugin_octoprint_nanny_device_reset", "Device identity reset"),
                    (
                        "plugin_octoprint_nanny_printer_profile_sync_start",
                        "Printer profile sync started",
                    ),
                    (
                        "plugin_octoprint_nanny_printer_profile_sync_done",
                        "Printer profile sync succeeded",
                    ),
                    (
                        "plugin_octoprint_nanny_printer_profile_sync_failed",
                        "Printer profile sync failed",
                    ),
                    (
                        "plugin_octoprint_nanny_connect_test_rest_api",
                        "Test connection to REST API",
                    ),
                    (
                        "plugin_octoprint_nanny_connect_test_rest_api_failed",
                        "Test connection to REST API failed",
                    ),
                    (
                        "plugin_octoprint_nanny_connect_test_rest_api_success",
                        "Test connection to REST API success",
                    ),
                    (
                        "plugin_octoprint_nanny_connect_test_mqtt_ping",
                        "Test connection to REST API",
                    ),
                    (
                        "plugin_octoprint_nanny_connect_test_mqtt_ping_failed",
                        "Test connection to REST API failed",
                    ),
                    (
                        "plugin_octoprint_nanny_connect_test_mqtt_ping_success",
                        "Test connection to REST API success",
                    ),
                    (
                        "plugin_octoprint_nanny_connect_test_mqtt_pong",
                        "Test connection to REST API",
                    ),
                    (
                        "plugin_octoprint_nanny_connect_test_mqtt_pong_failed",
                        "Test connection to REST API failed",
                    ),
                    (
                        "plugin_octoprint_nanny_connect_test_mqtt_pong_success",
                        "Test connection to REST API success",
                    ),
                    ("connect_test_noop", "A no-op test event without side effects"),
                    ("ClientAuthed", "ClientAuthed"),
                    ("ClientClosed", "ClientClosed"),
                    ("ClientDeauthed", "ClientDeauthed"),
                    ("ClientOpened", "ClientOpened"),
                    ("SettingsUpdated", "SettingsUpdated"),
                    ("UserLoggedIn", "User Logged In"),
                    ("UserLoggedOut", "User Logged Out"),
                    ("FileAdded", "FileAdded"),
                    ("FileRemoved", "FileRemoved"),
                    ("FolderAdded", "FolderAdded"),
                    ("FolderRemoved", "FolderRemoved"),
                    ("TransferDone", "TransferDone"),
                    ("TransferFailed", "TransferFailed"),
                    ("TransferStarted", "TransferStarted"),
                    ("UpdatedFiles", "UpdatedFiles"),
                    ("Upload", "Upload"),
                    ("CaptureDone", "CaptureDone"),
                    ("CaptureFailed", "CaptureFailed"),
                    ("CaptureStart", "CaptureStart"),
                    ("MovieDone", "MovieDone"),
                    ("MovieFailed", "MovieFailed"),
                    ("MovieRendering", "MovieRendering"),
                    ("PostRollEnd", "PostRollEnd"),
                    ("PostRollStart", "PostRollStart"),
                    ("SlicingCancelled", "SlicingCancelled"),
                    ("SlicingDone", "SlicingDone"),
                    ("SlicingFailed", "SlicingFailed"),
                    ("SlicingProfileAdded", "SlicingProfileAdded"),
                    ("SlicingProfileDeleted", "SlicingProfileDeleted"),
                    ("SlicingProfileModified", "SlicingProfileModified"),
                    ("SlicingStarted", "SlicingStarted"),
                    ("Connected", "Connected"),
                    ("Disconnected", "Disconnected"),
                    ("PrinterReset", "PrinterReset"),
                    ("FirmwareData", "FirmwareData"),
                    ("PrinterProfileAdded", "PrinterProfileAdded"),
                    ("PrinterProfileDeleted", "PrinterProfileDeleted"),
                    ("PrinterProfileModified", "PrinterProfileModified"),
                    ("PrintProgress", "PrintProgress"),
                    (
                        "plugin_pi_support_throttle_state",
                        "plugin_pi_support_throttle_state",
                    ),
                    ("Shutdown", "Shutdown"),
                    ("Startup", "Startup"),
                    ("plugin_backup_backup_created", "Backup Created"),
                    ("remote_command_received", "Command was received by device"),
                    (
                        "remote_command_failed",
                        "Command failed. Please download your Octoprint logs and open a Github issue to get this fixed.",
                    ),
                    ("remote_command_success", "Command succeeded"),
                    ("PrintCancelled", "PrintCancelled"),
                    ("PrintCancelling", "PrintCancelling"),
                    ("PrintDone", "PrintDone"),
                    ("PrintFailed", "PrintFailed"),
                    ("PrintPaused", "PrintPaused"),
                    ("PrintResumed", "PrintResumed"),
                    ("PrintStarted", "PrintStarted"),
                    ("PrinterStateChanged", "PrinterStateChanged"),
                ],
                db_index=True,
                default="connect_test_noop",
                max_length=255,
            ),
        ),
    ]
