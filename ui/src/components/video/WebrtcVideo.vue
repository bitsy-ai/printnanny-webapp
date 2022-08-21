<script setup lang="ts">
import { useWebrtcStore } from '@/stores/webrtc';

const props = defineProps({
    piId: {
        type: Number,
        required: true
    }
})

const store = useWebrtcStore();
await store.init(props.piId);
</script>

<template>
    
</template>