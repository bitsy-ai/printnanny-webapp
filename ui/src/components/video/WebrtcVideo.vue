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
  <video
    id="janus-video"
    autoplay
    muted
    class="w-full aspect-video p-6"
  ></video>
</template>
