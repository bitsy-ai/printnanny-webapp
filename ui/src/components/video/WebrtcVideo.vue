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
    <video id="janus-video" muted class="w-full aspect-video p-6"></video>
    <p class="text-sm text-gray-500 text-center">
      Raspberry Pi Camera will turn off when you leave this page.
    </p>
  </div>
</template>
