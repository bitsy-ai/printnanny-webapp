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
    <video id="janus-video" muted class="aspect-video h-80 m-auto" aria-placeholder="PrintNanny Cam is paused" poster="@/assets/video/video-paused.svg"></video>
    <p class="text-sm text-gray-500 text-center" v-if="store.loading">
      Raspberry Pi camera is loading.
    </p>
    <p class="text-sm text-gray-500 text-center" v-if="!store.loading">
      Raspberry Pi camera will turn off automatically when you finish the setup wizard.
    </p>
  </div>
</template>
