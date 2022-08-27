<script setup lang="ts">
import { useWebrtcStore } from "@/stores/webrtc";

const props = defineProps({
  piId: {
    type: Number,
    required: true,
  },
});

const store = useWebrtcStore();
const stream = await store.getStream(props.piId);
if (stream !== undefined) {
  store.initWebrtcStream(stream);
}
</script>

<template>
  <div>
    <video
      id="janus-video"
      muted
      class="aspect-video h-80 mx-auto my-4 border-double border-4 border-grey-200"
      aria-placeholder="PrintNanny Cam is paused"
      poster="@/assets/video/video-paused.svg"
    ></video>
    <p v-if="store.loading" class="text-sm text-gray-500 text-center">
      Raspberry Pi camera is loading.
    </p>
    <p v-if="!store.loading" class="text-sm text-gray-500 text-center">
      Raspberry Pi camera will turn off automatically when you finish the setup
      wizard.
    </p>
  </div>
</template>
