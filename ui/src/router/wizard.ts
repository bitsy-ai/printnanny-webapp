import type { RouteRecordRaw } from "vue-router";

import PiCreateWizardProgress from "@/components/wizard/PiCreateWizardProgress.vue";
import { PiCreateWizardSteps } from "@/components/wizard/piCreateWizard";

const piWizardSteps = PiCreateWizardSteps();

export default piWizardSteps.map((step) => {
  return {
    path: step.path,
    name: `pi-wizard-${step.key}`,
    components: {
      default: step.component,
      TopBar: PiCreateWizardProgress,
    },
    props: { default: true, TopBar: true },
  };
}) as Array<RouteRecordRaw>;
