<script>
import { layoutComputed } from '@state/helpers'

import Horizontal from '@router/layouts/horizontal'
import Vertical from '@router/layouts/vertical'
import Detached from '@router/layouts/detached'

export default {
  components: { Horizontal, Vertical, Detached },
  computed: {
    ...layoutComputed,
  },
}
</script>

<template>
  <div>
    <vertical v-if="layoutType === 'vertical'" :layout="layoutType">
      <slot />
    </vertical>

    <Horizontal v-if="layoutType === 'horizontal'" :layout="layoutType">
      <slot />
    </Horizontal>

    <Detached v-if="layoutType === 'detached'" :layout="layoutType">
      <slot />
    </Detached>
  </div>
</template>
