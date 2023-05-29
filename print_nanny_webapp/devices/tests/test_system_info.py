from typing import Optional
from django.test import TestCase
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth import get_user_model
from print_nanny_webapp.devices.models import Pi, SystemInfo
from print_nanny_webapp.devices.enum import (
    SingleBoardComputerType,
)

User = get_user_model()


class TestSystemInfoDiskUsage(TestCase):
    """
    Tests SystemInfo disk utilization display
    """

    user: Optional[AbstractBaseUser] = None
    pi: Optional[Pi] = None

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = User.objects.create(
            email="admin@test.com",
            password="testing1234",
            is_superuser=False,
            is_active=True,
        )

        cls.pi = Pi.objects.create(
            user=cls.user,
            hostname="test",
            favorite=True,
            setup_finished=True,
            sbc=SingleBoardComputerType.RPI_4,
        )

    def test_system_info_disk_usage_display(self):
        if self.pi:
            sysinfo = SystemInfo.objects.create(
                machine_id="test",
                model="test",
                serial="test",
                cores=2,
                ram=2048,
                pi=self.pi,
                os_version_id="test",
                os_build_id="2022-12-21T12:36:49Z",
                uptime=100,
                rootfs_size=1e9,
                rootfs_used=round(1e9 / 2),
                bootfs_size=1e7,
                bootfs_used=round(1e7 / 2),
                datafs_size=3 * 1e9,
                datafs_used=round(2 * 1e9),
            )

            assert sysinfo.datafs_size_pretty == "2.79 GB"
            assert sysinfo.datafs_used_pretty == "1.86 GB (67% used)"

            assert sysinfo.bootfs_size_pretty == "9.54 MB"
            assert sysinfo.bootfs_used_pretty == "4.77 MB (50% used)"

            assert sysinfo.rootfs_size_pretty == "953.67 MB"
            assert sysinfo.rootfs_used_pretty == "476.84 MB (50% used)"
