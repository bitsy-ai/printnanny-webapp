<script>
import simplebar from 'simplebar-vue'

export default {
  components: { simplebar },
  data() {
    return {
      chatData: [
        {
          image: require('@assets/images/users/avatar-5.jpg'),
          name: 'Shreyu N',
          time: '10:00',
          message: 'Hello!',
        },
        {
          image: require('@assets/images/users/avatar-1.jpg'),
          name: 'Dominic',
          time: '10:01',
          message: 'Hi, How are you? What about our next meeting?',
          odd: 'true',
        },
        {
          image: require('@assets/images/users/avatar-5.jpg'),
          name: 'Shreyu N',
          time: '10:01',
          message: 'Yeah everything is fine',
        },
        {
          image: require('@assets/images/users/avatar-1.jpg'),
          name: 'Dominic',
          time: '10:02',
          message: "Wow that's great",
          odd: 'true',
        },
        {
          image: require('@assets/images/users/avatar-5.jpg'),
          name: 'Shreyu N',
          time: '10:02',
          message: "Let's have it today if you are free",
        },
        {
          image: require('@assets/images/users/avatar-1.jpg'),
          name: 'Dominic',
          time: '10:03',
          message: 'Sure thing! let me know if 2pm works for you',
          odd: 'true',
        },
        {
          image: require('@assets/images/users/avatar-5.jpg'),
          name: 'Shreyu N',
          time: '10:04',
          message:
            'Sorry, I have another meeting scheduled at 2pm. Can we have it at 3pm instead?',
        },
        {
          image: require('@assets/images/users/avatar-5.jpg'),
          name: 'Shreyu N',
          time: '10:04',
          message:
            'We can also discuss about the presentation talk format if you have some extra mins',
        },
        {
          image: require('@assets/images/users/avatar-1.jpg'),
          name: 'Dominic',
          time: '10:05',
          message:
            "3pm it is. Sure, let's discuss about presentation format, it would be great to finalize today. I am attaching the last year format and assets here...",
          odd: 'true',
          file: true,
        },
      ],
    }
  },
}
</script>

<template>
  <div class="card">
    <div class="card-body">
      <simplebar style="max-height: 535px">
        <ul class="conversation-list">
          <li
            v-for="chat of chatData"
            :key="chat.message"
            :class="{ 'odd': `${chat.odd}` === 'true' }"
            class="clearfix"
          >
            <div class="chat-avatar">
              <img :src="`${chat.image}`" class="rounded" alt="user-image" />
              <i>{{ chat.time }}</i>
            </div>
            <div class="conversation-text">
              <div class="ctext-wrap">
                <i>{{ chat.name }}</i>
                <p>{{ chat.message }}</p>
              </div>
              <div v-if="chat.file" class="card mt-2 mb-1 shadow-none border text-left">
                <div class="p-2">
                  <div class="row align-items-center">
                    <div class="col-auto">
                      <div class="avatar-sm">
                        <span class="avatar-title rounded">.ZIP</span>
                      </div>
                    </div>
                    <div class="col pl-0">
                      <a
                        href="javascript:void(0);"
                        class="text-muted font-weight-bold"
                      >Hyper-admin-design.zip</a>
                      <p class="mb-0">2.3 MB</p>
                    </div>
                    <div class="col-auto">
                      <!-- Button -->
                      <a href="javascript:void(0);" class="btn btn-link btn-lg text-muted">
                        <i class="dripicons-download"></i>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <b-dropdown
              menu-class
              right
              class="conversation-actions"
              toggle-class="btn-sm btn-link arrow-none"
              variant="white"
            >
              <template v-slot:button-content>
                <i class="uil uil-ellipsis-v"></i>
              </template>
              <a class="dropdown-item" href="#">Copy Message</a>
              <a class="dropdown-item" href="#">Edit</a>
              <a class="dropdown-item" href="#">Delete</a>
            </b-dropdown>
          </li>
        </ul>
      </simplebar>

      <div class="row">
        <div class="col">
          <div class="mt-3 bg-light p-3 rounded">
            <form id="chat-form" class="needs-validation" novalidate name="chat-form">
              <div class="row">
                <div class="col mb-2 mb-sm-0">
                  <input
                    type="text"
                    class="form-control border-0"
                    placeholder="Enter your text"
                    required
                  />
                  <div class="invalid-feedback">Please enter your messsage</div>
                </div>
                <div class="col-sm-auto">
                  <div class="btn-group">
                    <a href="#" class="btn btn-light">
                      <i class="uil uil-paperclip"></i>
                    </a>
                    <a href="#" class="btn btn-light">
                      <i class="uil uil-smile"></i>
                    </a>
                    <button type="submit" class="btn btn-success chat-send btn-block">
                      <i class="uil uil-message"></i>
                    </button>
                  </div>
                </div>
                <!-- end col -->
              </div>
              <!-- end row-->
            </form>
          </div>
        </div>
        <!-- end col-->
      </div>
      <!-- end row -->
    </div>
    <!-- end card-body -->
  </div>
  <!-- end card -->
</template>