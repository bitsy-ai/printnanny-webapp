<template>
<Transition
    name="fade"
    mode="out-in"
    :duration="{ enter: 800, leave: 500 }"
>

    <TableEmpty v-if="store.showEmpty" :icon="VideoCameraIcon" header="No recordings found"/>

</Transition>
</template>
<script setup lang="ts">
import { useVideoStore } from "@/stores/video";
import TableEmpty from "@/components/devices/TableEmpty.vue";
import { VideoCameraIcon } from "@heroicons/vue/solid";

const store = useVideoStore();

</script>