import os


class FileLocator:
    INSTALL_PATH = "/opt/printnanny/"
    ANSIBLE_FACT_PATH = os.path.join(INSTALL_PATH, "facts.d")
    BOOT_PATH = "/boot"

    DATA_PATH = os.path.join(INSTALL_PATH, "data")

    FACT_PATH = ANSIBLE_FACT_PATH
    FACT_DEVICE_PATH = ANSIBLE_FACT_PATH.join("device.fact")
    FACT_LICENSE_PATH = ANSIBLE_FACT_PATH.join("license.fact")

    CA_CERTS_PATH = INSTALL_PATH.join("ca-certificates")
    DATA_PATH = DATA_PATH
    INSTALL_PATH = INSTALL_PATH
    LICENSE_ZIP_FILENAME = "printnanny_license.zip"
    LICENSE_ZIP_PATH = BOOT_PATH.join(LICENSE_ZIP_FILENAME)

    KEY_PRIVATE_PKCS8_FILENAME = "ecdsa256_pkcs8.pem"
    KEY_PRIVATE_SEC1_FILENAME = "ecdsa256_sec1.pem"
    KEY_PUBLIC_FILENAME = "ecdsa_public.pem"

    KEY_PRIVATE_PKCS8_PATH = DATA_PATH.join(KEY_PRIVATE_PKCS8_FILENAME)
    KEY_PRIVATE_SEC1_PATH = DATA_PATH.join(KEY_PRIVATE_SEC1_FILENAME)
    KEY_PUBLIC_PATH = DATA_PATH.join(KEY_PUBLIC_FILENAME)

    CA_CERTS_FILENAME = "ca_certs.pem"
    CA_CERTS_PATH = INSTALL_PATH.join("ca-certificates").join(CA_CERTS_FILENAME)
