<script>
import simplebar from 'simplebar-vue'
import { required } from 'vuelidate/lib/validators'

/**
 * Chat list - Renders a chat list with a form to enter new message
 * 1. User specifies the title of window using the 'title' input property.
 * 2. Window height set using the 'chatWindowHeight' input property. Height would count in pixel. 
 * 3. Messages array specify the id, image, name, message, time. 
 *     id - specify the unique id of chat message.
 *     image - Specify the profile of user.
 *     name - Specify the name of chat user.
 *     message - User chat message specify using message.
 *     time - Message sended time specify using time.
 */
export default {
  components: { simplebar },
  props: {
    title: {
      type: String,
      default: 'Chat',
    },
    chatWindowHeight: {
      type: String,
      default: '200',
    },
    chatMessages: {
      type: Array,
      default: function() {
        return []
      },
    },
  },
  data() {
    return {
      chats: {
        message: '',
      },
      submitform: false,
    }
  },
  validations: {
    chats: {
      message: { required },
    },
  },
  methods: {
    /**
     * Chat form submit
     */
    saveMessage() {
      this.submitform = true

      // stop here if form is invalid
      this.$v.$touch()
      if (this.$v.$invalid) {
        return
      } else {
        var id = this.chatMessages.length
        const message = this.chats.message
        const currentDate = new Date()

        // Message Push in Chat
        this.chatMessages.push({
          image: require('@assets/images/users/avatar-5.jpg'),
          id: id + 1,
          name: 'Smith',
          message,
          time: currentDate.getHours() + ':' + currentDate.getMinutes(),
        })
      }
      this.submitform = false
      this.chats = {}
    },
  },
}
</script>

<template>
  <div class="card">
    <div class="card-body">
      <b-dropdown variant="white" class="float-right" toggle-class="arrow-none card-drop p-0" right>
        <template v-slot:button-content>
          <i class="mdi mdi-dots-vertical"></i>
        </template>
        <!-- item-->
        <a href="javascript:void(0);" class="dropdown-item">Settings</a>
        <!-- item-->
        <a href="javascript:void(0);" class="dropdown-item">Action</a>
      </b-dropdown>
      <h5 class="mb-3 header-title">{{ title }}</h5>

      <simplebar :style="`max-height:${chatWindowHeight}`">
        <div class="chat-conversation">
          <ul class="conversation-list">
            <li
              v-for="(chat, index) in chatMessages"
              :key="chat.id"
              :class="{ odd: index % 2 }"
              class="clearfix"
            >
              <div class="chat-avatar">
                <img :src="`${chat.image}`" alt="male" />
                <i>{{ chat.time }}</i>
              </div>
              <div class="conversation-text">
                <div class="ctext-wrap">
                  <i>{{ chat.name }}</i>
                  <p>{{ chat.message }}</p>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </simplebar>
      <form @submit.prevent="saveMessage">
        <div class="row mt-3 pb-1">
          <div class="col-lg-10">
            <input
              id="message"
              v-model="chats.message"
              type="text"
              class="form-control"
              placeholder="Enter your text"
              name="message"
              :class="{ 'is-invalid': submitform && $v.chats.message.$error }"
            />
            <div
              v-if="submitform && !$v.chats.message.required"
              class="invalid-feedback"
            >This value is required.</div>
          </div>

          <div class="col-lg-1">
            <button type="submit" class="btn btn-danger chat-send">Send</button>
          </div>
        </div>
        <!-- end row -->
      </form>
      <!-- end form -->
    </div>
  </div>
</template>
