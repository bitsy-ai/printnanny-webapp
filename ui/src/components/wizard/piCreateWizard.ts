import * as yup from "yup";
import { useWizardStore } from "@/stores/wizard";
import type * as api from "printnanny-api-client";
import SdCardStep from "./steps/SdCardStep.vue";
import PiCreateStep from "./steps/PiCreateStep.vue";
import DownloadLicenseStep from "./steps/DownloadLicenseStep.vue";
import TestConnectionStep from "./steps/TestConnectionStep.vue";

const stepKeys = [
  {
    key: "customize-sd-card",
    title: "Customize SD Card",
  },
  { key: "raspberry-pi", title: "Connect Raspberry Pi" },
  { key: "download-zip", title: "Download PrintNanny.zip" },
  { key: "test-connection", title: "Test PrintNanny Connection" },
  { key: "done", title: "Finish Setup" },
];

export function PiCreateWizardSteps() {
  const store = useWizardStore();
  return [
    {
      key: stepKeys[0].key,
      component: SdCardStep,
      title: stepKeys[0].title,
      progress: "0%",
      style: "width: 0",
      validationSchema: yup.object(),
      prevButton: undefined,
      nextButton: {
        text: `Next: ${stepKeys[1].title}`,
        link: () => ({
          name: "pi-wizard",
          params: { activeStep: stepKeys[1].key },
        }),
      },
      onSubmit: (_formData: any) => {
        console.debug("create-sd-card onSubmit");
      },
    },
    {
      key: stepKeys[1].key,
      component: PiCreateStep,
      title: "Add Raspberry Pi",
      progress: "25%",
      style: "width: 25%",
      validationSchema: yup.object({
        hostname: yup.string().required(),
        edition: yup.string().required(),
        sbc: yup.string().required(),
      }),
      nextButton: {
        text: `Next: ${stepKeys[2].title}`,
        link: () => ({
          name: "pi-wizard",
          params: { activeStep: stepKeys[2].key, piId: store.pi?.id },
        }),
      },
      prevButton: {
        text: `Previous: ${stepKeys[0].title}`,
        link: () => ({
          name: "pi-wizard",
          params: { activeStep: stepKeys[0].key },
        }),
      },
      onSubmit: async (formData: any) => {
        const store = useWizardStore();
        console.log("add-pi onSubmit", formData);
        // WIREGUARD TODO: allow user to specify fqdn
        const { hostname, edition, sbc } = formData;
        const req: api.PiRequest = {
          fqdn: `${hostname}.local`,
          favorite: false,
          hostname,
          edition,
          sbc,
        };
        const pi = await store.createPi(req);
        if (pi) {
          store.downloadLicenseZip(pi.id);
        }
      },
    },
    {
      key: stepKeys[2].key,
      component: DownloadLicenseStep,
      title: stepKeys[2].title,
      progress: "50%",
      style: "width: 50%",
      validationSchema: yup.object({
        tos: yup.boolean(),
      }),
      nextButton: {
        text: `Next: ${stepKeys[3].title}`,
        link: () => ({
          name: "pi-wizard",
          params: { activeStep: stepKeys[3].key, piId: store.pi?.id },
        }),
      },
      prevButton: {
        text: `Previous: ${stepKeys[1].title}`,
        link: () => ({
          name: "pi-wizard",
          params: { activeStep: stepKeys[1].key },
        }),
      },
      onSubmit: (_formData: any) => {
        // handle form data
      },
    },
    {
      key: stepKeys[3].key,
      component: TestConnectionStep,
      progress: "75%",
      style: "width: 75%",
      title: stepKeys[3].title,
      validationSchema: yup.object(),
      nextButton: {
        text: `Next: ${stepKeys[4].title}`,
        link: () => ({
          name: "pi-wizard",
          params: { activeStep: stepKeys[4].key, piId: store.pi?.id },
        }),
      },
      prevButton: {
        text: `Previous: ${stepKeys[2].title}`,
        link: () => ({
          name: "pi-wizard",
          params: { activeStep: stepKeys[2].key, piId: store.pi?.id },
        }),
      },
      onSubmit: (_formData: any) => {
        // handle form data
      },
    },
    {
      key: stepKeys[4].key,
      progress: "100%",
      style: "width: 100%",
      title: "Setup is Complete - Nice Work!",
      validationSchema: yup.object(),
      nextButton: undefined,
      prevButton: {
        text: `Previous: ${stepKeys[3].title}`,
        link: () => ({
          name: "pi-wizard",
          params: { activeStep: stepKeys[3].key, piId: store.pi?.id },
        }),
      },
      onSubmit: (_formData: any) => {
        // handle form data
      },
    },
  ];
}
