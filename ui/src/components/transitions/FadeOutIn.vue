<template>
  <Transition name="fade" mode="out-in" :duration="{ enter: 800, leave: 500 }">
    <v-slot></v-slot>
</Transition>
</template>
<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>