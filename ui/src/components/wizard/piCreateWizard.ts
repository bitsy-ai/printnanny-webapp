import * as yup from "yup";
import { useWizardStore } from "@/stores/wizard";
import type * as api from "printnanny-api-client";
import SdCardStep from "./steps/SdCardStep.vue";
import PiCreateStep from "./steps/PiCreateStep.vue";
import DownloadLicenseStep from "./steps/DownloadLicenseStep.vue";
import TestConnectionStep from "./steps/TestConnectionStep.vue";
import DoneStep from "./steps/DoneStep.vue";
import type { WizardStep } from "@/types";

export const stepKeys = [
  {
    key: "customize-sd-card",
    title: "Customize SD Card",
    detail:
      "Configure your Pi's hostname and wifi with the Raspberry Pi imager.",
  },
  { key: "raspberry-pi", title: "Register My Raspberry Pi", detail: "" },
  {
    key: "download-license",
    title: "Download PrintNanny.zip",
    detail:
      "This section will help you copy your PrintNanny license to your SD card.",
  },
  {
    key: "test-connection",
    title: "Test PrintNanny Setup",
    detail:
      "Almost done! This section will double-check your PrintNanny setup.",
  },
  { key: "done", title: "Finish Setup", detail: "" },
];

export function PiCreateWizardSteps(): WizardStep[] {
  const store = useWizardStore();
  return [
    {
      key: stepKeys[0].key,
      detail: stepKeys[0].detail,
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
      detail: stepKeys[1].detail,
      component: PiCreateStep,
      title: stepKeys[1].title,
      progress: "33%",
      style: "width: 33%",
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
      detail: stepKeys[2].detail,
      component: DownloadLicenseStep,
      progress: "66%",
      style: "width: 66%",
      title: stepKeys[2].title,
      validationSchema: yup.object(),
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
          params: { activeStep: stepKeys[1].key, piId: store.pi?.id },
        }),
      },
      onSubmit: (_formData: any) => {
        // handle form data
      },
    },
    {
      key: stepKeys[3].key,
      detail: stepKeys[3].detail,
      component: TestConnectionStep,
      progress: "66%",
      style: "width: 66%",
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
      detail: stepKeys[4].detail,
      progress: "100%",
      style: "width: 100%",
      title: "Setup is Complete - Nice Work!",
      validationSchema: yup.object(),
      nextButton: undefined,
      component: DoneStep,
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
