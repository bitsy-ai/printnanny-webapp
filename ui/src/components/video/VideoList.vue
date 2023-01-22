<template>
<Transition
    name="fade"
    mode="out-in"
    :duration="{ enter: 800, leave: 500 }"
>

    <TableEmpty v-if="store.showEmpty" :icon="VideoCameraIcon" header="No recordings found"/>
    <div class="w-full flex p-4 grid grid-cols-2 md:grid-cols-3" v-else>
        <div v-for="(video, idx) in store.videos" :key="idx" class="w-full bg-gray-100 rounded-lg border border-gray-200 shadow-2xl p-4">
            <video
            muted="true"
            controls="true"
            class="w-full rounded bg-white"
            preload="metadata"
            >
            <source
                :src="video.mp4_file"
                type="video/mp4"
            />
            </video>
            <p class="text-center text-sm text-gray-700 mt-2">Created {{ moment(video.created_dt).fromNow() }}</p>

        </div>

    </div>
</Transition>
</template>
<script setup lang="ts">
import moment from "moment";
import { onMounted } from "vue";
import { useVideoStore} from "@/stores/video";
import TableEmpty from "@/components/devices/TableEmpty.vue";
import { VideoCameraIcon } from "@heroicons/vue/solid";

const store = useVideoStore();
onMounted(async () => {
    await store.load();
})
</script>