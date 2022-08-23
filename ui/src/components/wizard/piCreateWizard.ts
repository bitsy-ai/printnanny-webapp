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
  {
    key: "done",
    title: "Nice work! Setup is complete.",
    detail: "Your PrintNanny device is ready to use.",
  },
];

export function PiCreateWizardSteps(): WizardStep[] {
  return [
    {
      key: stepKeys[0].key,
      path: `/connect/${stepKeys[0].key}`,
      routeName: `pi-wizard-${stepKeys[0].key}`,
      detail: stepKeys[0].detail,
      component: SdCardStep,
      title: stepKeys[0].title,
      progress: "0%",
      style: "width: 0",
      validationSchema: yup.object(),
      prevButton: undefined,
      nextButton: {
        onSubmit: undefined,
        text: `Next: ${stepKeys[1].title}`,
        link: () => ({
          name: `pi-wizard-${stepKeys[1].key}`,
        }),
      },
    },
    {
      key: stepKeys[1].key,
      path: `/connect/${stepKeys[1].key}`,
      routeName: `pi-wizard-${stepKeys[1].key}`,
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
          await store.createPi(req);
        },
        link: () => {
          const store = useWizardStore();
          return {
            name: `pi-wizard-${stepKeys[2].key}`,
            params: { piId: store.pi?.id },
          };
        },
      },
      prevButton: {
        onSubmit: undefined,
        text: `Previous: ${stepKeys[0].title}`,
        link: () => ({
          name: `pi-wizard-${stepKeys[1].key}`,
        }),
      },
    },
    {
      key: stepKeys[2].key,
      path: `/connect/${stepKeys[2].key}/:piId`,
      routeName: `pi-wizard-${stepKeys[2].key}`,
      detail: stepKeys[2].detail,
      component: DownloadLicenseStep,
      progress: "66%",
      style: "width: 66%",
      title: stepKeys[2].title,
      validationSchema: yup.object(),
      nextButton: {
        text: `Next: ${stepKeys[3].title}`,
        onSubmit: undefined,
        link: () => {
          const store = useWizardStore();
          return {
            name: `pi-wizard-${stepKeys[3].key}`,
            params: { piId: store.pi?.id },
          };
        },
      },
      prevButton: {
        text: `Previous: ${stepKeys[1].title}`,
        onSubmit: undefined,
        link: () => {
          return {
            name: `pi-wizard-${stepKeys[1].key}`,
          };
        },
      },
    },
    {
      key: stepKeys[3].key,
      path: `/connect/${stepKeys[3].key}/:piId`,
      routeName: `pi-wizard-${stepKeys[3].key}`,
      detail: stepKeys[3].detail,
      component: TestConnectionStep,
      progress: "66%",
      style: "width: 66%",
      title: stepKeys[3].title,
      validationSchema: yup.object(),
      nextButton: {
        text: `Next: ${stepKeys[4].title}`,
        onSubmit: undefined,
        link: () => {
          const store = useWizardStore();

          return {
            name: `pi-wizard-${stepKeys[4].key}`,
            params: { activeStep: stepKeys[4].key, piId: store.pi?.id },
          };
        },
      },
      prevButton: {
        text: `Previous: ${stepKeys[2].title}`,
        onSubmit: undefined,
        link: () => {
          const store = useWizardStore();
          return {
            name: `pi-wizard-${stepKeys[2].key}`,
            params: { piId: store.pi?.id },
          };
        },
      },
    },
    {
      key: stepKeys[4].key,
      path: `/connect/${stepKeys[4].key}/:piId`,
      routeName: `pi-wizard-${stepKeys[4].key}`,
      detail: stepKeys[4].detail,
      progress: "100%",
      style: "width: 100%",
      title: stepKeys[4].title,
      validationSchema: yup.object(),
      nextButton: undefined,
      component: DoneStep,
      prevButton: {
        text: `Previous: ${stepKeys[3].title}`,
        onSubmit: undefined,
        link: () => {
          const store = useWizardStore();

          return {
            name: `pi-wizard-${stepKeys[3].key}`,
            params: { piId: store.pi?.id },
          };
        },
      },
    },
  ];
}
