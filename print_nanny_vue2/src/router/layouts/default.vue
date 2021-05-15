<script>
export default {
  components: {},
  created: () => {
    document.body.classList.add('authentication-bg')
  },
}
</script>

<template>
  <div>
    <div class="account-pages mt-5 mb-5">
      <div class="container">
        <slot />
      </div>
    </div>
    <footer
      class="footer footer-alt"
    >2018 - {{ new Date().getFullYear() }} © Hyper - Coderthemes.com</footer>
  </div>
</template>
