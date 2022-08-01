
import * as yup from "yup";
import { useWizardStore } from "@/stores/wizard";



export function PiCreateWizardSteps() {
    const store = useWizardStore()
    return [
        {
            key: "create-sd-card",
            title: "Burn PrintNanny OS Image",
            progress: "0%",
            style: "width: 0",
            validationSchema: yup.object(),
            prevButton: undefined,
            nextButton: { text: "Next: Connect New Pi", link: () => ({ name: "device-connect", params: { activeStep: "create-new-device" } }) },
            onSubmit: (_formData: any) => {
                console.debug("create-sd-card onSubmit")
            },
        },
        {
            key: "create-new-device",
            title: "Connect New Device",
            progress: "25%",
            style: "width: 25%",
            validationSchema: yup.object({
                hostname: yup.string().required(),
                edition: yup.string().required(),
                sbc: yup.string().required(),
            }),
            nextButton: { text: "Next: Download PrintNanny.zip", link: () => ({ name: "device-connect", params: { activeStep: "download-printnanny-zip", piId: store.pi?.id } }) },
            prevButton: { text: "Previous: Burn PrintNanny OS Image", link: () => ({ name: "device-connect", params: { activeStep: "create-new-device" } }) },
            onSubmit: async (formData: any) => {
                const store = useWizardStore();
                console.log("create-new-device onSubmit", formData)
                // WIREGUARD TODO: allow user to specify fqdn
                const { hostname, edition, sbc } = formData
                const req: api.PiRequest = {
                    fqdn: `${hostname}.local`,
                    favorite: false,
                    hostname,
                    edition,
                    sbc,
                };
                const pi = await store.createPi(req);
                store.downloadLicenseZip(parseInt(pi.id))
            }
        },
        {
            key: "download-printnanny-zip",
            title: "Download PrintNanny.zip",
            progress: "50%",
            style: "width: 50%",
            validationSchema: yup.object({
                tos: yup
                    .boolean(),
            }),
            nextButton: { text: "Next: Test Connection", link: () => ({ name: "device-connect", params: { activeStep: "test-connection", piId: store.pi?.id } }) },
            prevButton: { text: "Previous: Connect New Device", link: () => ({ name: "device-connect", params: { activeStep: "create-new-device" } }) },
            onSubmit: async (_formData: any) => {
                // tosChecked.value = true
            }
        },
        {
            key: "test-connection",
            progress: "75%",
            style: "width: 75%",
            title: "Test Raspberry Pi Connection",
            validationSchema: yup.object(),
            nextButton: { text: "Finish Setup", link: () => ({ name: "device-connect", params: { activeStep: "done", piId: store.pi?.id } }) },
            prevButton: { text: "Previous: Download PrintNanny.zip", link: () => ({ name: "device-connect", params: { activeStep: "download-printnanny-zip", piId: store.pi?.id } }) },
            onSubmit: async (formData) => {
                // await deviceStore.
            },

        },
        {
            key: "done",
            progress: "100%",
            style: "width: 100%",
            title: "Setup is Complete - Nice Work!",
            validationSchema: yup.object(),
            nextButton: undefined,
            prevButton: { text: "Test Connection", link: () => ({ name: "device-connect", params: { activeStep: "test-connection", piId: store.pi?.id } }) },
            onSubmit: async (formData) => {
                // await deviceStore.
            },

        },
    ]
};