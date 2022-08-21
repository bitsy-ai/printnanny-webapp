<script setup lang="ts">
import { useWebrtcStore } from '@/stores/webrtc';


const store = useWebrtcStore();
await store.init();
</script>

<template>
    
</template>