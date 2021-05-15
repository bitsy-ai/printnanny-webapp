<script>
import Message from '@components/widgets/message'

export default {
  components: { Message },
  data() {
    return {
      messages: [
        {
          image: require('@assets/images/users/avatar-2.jpg'),
          name: 'Tomaslau',
          message: "I've finished it! See you so...",
        },
        {
          image: require('@assets/images/users/avatar-3.jpg'),
          name: 'Stillnotdavid',
          message: 'This theme is awesome!',
        },
        {
          image: require('@assets/images/users/avatar-4.jpg'),
          name: 'Kurafire',
          message: 'Nice to meet you',
        },
        {
          image: require('@assets/images/users/avatar-5.jpg'),
          name: 'Shahedk',
          message: "Hey! there I'm available...",
        },
        {
          image: require('@assets/images/users/avatar-6.jpg'),
          name: 'Adhamdannaway',
          message: 'This theme is awesome!',
        },
      ],
    }
  },
}
</script>

<template>
  <Message :messages="messages" />
</template>