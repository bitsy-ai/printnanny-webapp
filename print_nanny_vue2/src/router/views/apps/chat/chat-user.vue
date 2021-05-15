<script>
import simplebar from 'simplebar-vue'

export default {
  components: { simplebar },
  data() {
    return {
      chatData: [
        {
          image: require('@assets/images/users/avatar-2.jpg'),
          name: 'Brandon Smith',
          message: 'How are you today?',
          time: '4:30am',
          text: 3,
        },
        {
          image: require('@assets/images/users/avatar-5.jpg'),
          name: 'Shreyu N',
          message: "Hey! a reminder for tomorrow's meeting...",
          time: '5:30am',
        },
        {
          image: require('@assets/images/users/avatar-7.jpg'),
          name: 'Maria C',
          message: "Are we going to have this week's planning meeting today?",
          time: 'Thu',
          text: 2,
        },
        {
          image: require('@assets/images/users/avatar-10.jpg'),
          name: 'Rhonda D',
          message: 'Please check these design assets...',
          time: 'Wed',
        },
        {
          image: require('@assets/images/users/avatar-3.jpg'),
          name: 'Michael H',
          message:
            'Are you free for 15 min? I would like to discuss something...',
          time: 'Tue',
          text: 6,
        },
        {
          image: require('@assets/images/users/avatar-6.jpg'),
          name: 'Thomas R',
          message: "Let's have meeting today between me, you and Tony...",
          time: 'Tue',
        },
        {
          image: require('@assets/images/users/avatar-8.jpg'),
          name: 'Thomas J',
          message: 'Howdy?',
          time: 'Tue',
        },
        {
          image: require('@assets/images/users/avatar-1.jpg'),
          name: 'Ricky J',
          message: 'Are you interested in learning?',
          time: 'Tue',
          text: 28,
        },
      ],
    }
  },
}
</script>

<template>
  <div class="card">
    <div class="card-body p-0">
      <b-tabs nav-class="nav-tabs nav-bordered" content-class="p-3">
        <b-tab title="All">
          <!-- start search box -->
          <div class="app-search">
            <form>
              <div class="form-group position-relative">
                <input type="text" class="form-control" placeholder="People, groups & messages..." />
                <span class="mdi mdi-magnify"></span>
              </div>
            </form>
          </div>
          <!-- end search box -->
          <simplebar style="max-height: 545px">
            <a
              v-for="chat of chatData"
              :key="chat.name"
              href="javascript:void(0);"
              class="text-body"
            >
              <div class="media mt-1 p-2">
                <img
                  :src="`${chat.image}`"
                  class="mr-2 rounded-circle"
                  height="48"
                  alt="Brandon Smith"
                />
                <div class="media-body">
                  <h5 class="mt-0 mb-0 font-14">
                    <span class="float-right text-muted font-12">{{chat.time}}</span>
                    {{chat.name}}
                  </h5>
                  <p class="mt-1 mb-0 text-muted font-14">
                    <span class="w-25 float-right text-right">
                      <span class="badge badge-danger-lighten">{{chat.text}}</span>
                    </span>
                    <span class="w-75">{{chat.message}}</span>
                  </p>
                </div>
              </div>
            </a>
          </simplebar>
        </b-tab>
        <b-tab title="Favourites">
          <!-- start search box -->
          <div class="app-search">
            <form>
              <div class="form-group position-relative">
                <input type="text" class="form-control" placeholder="People, groups & messages..." />
                <span class="mdi mdi-magnify"></span>
              </div>
            </form>
          </div>
          <!-- end search box -->
          <simplebar style="max-height: 545px">
            <a
              v-for="chat of chatData"
              :key="chat.name"
              href="javascript:void(0);"
              class="text-body"
            >
              <div class="media mt-1 p-2">
                <img
                  :src="`${chat.image}`"
                  class="mr-2 rounded-circle"
                  height="48"
                  alt="Brandon Smith"
                />
                <div class="media-body">
                  <h5 class="mt-0 mb-0 font-14">
                    <span class="float-right text-muted font-12">{{chat.time}}</span>
                    {{chat.name}}
                  </h5>
                  <p class="mt-1 mb-0 text-muted font-14">
                    <span class="w-25 float-right text-right">
                      <span class="badge badge-danger-lighten">{{chat.text}}</span>
                    </span>
                    <span class="w-75">{{chat.message}}</span>
                  </p>
                </div>
              </div>
            </a>
          </simplebar>
        </b-tab>
        <b-tab title="Friends">
          <!-- start search box -->
          <div class="app-search">
            <form>
              <div class="form-group position-relative">
                <input type="text" class="form-control" placeholder="People, groups & messages..." />
                <span class="mdi mdi-magnify"></span>
              </div>
            </form>
          </div>
          <!-- end search box -->
          <simplebar style="max-height: 545px">
            <a
              v-for="chat of chatData"
              :key="chat.name"
              href="javascript:void(0);"
              class="text-body"
            >
              <div class="media mt-1 p-2">
                <img
                  :src="`${chat.image}`"
                  class="mr-2 rounded-circle"
                  height="48"
                  alt="Brandon Smith"
                />
                <div class="media-body">
                  <h5 class="mt-0 mb-0 font-14">
                    <span class="float-right text-muted font-12">{{chat.time}}</span>
                    {{chat.name}}
                  </h5>
                  <p class="mt-1 mb-0 text-muted font-14">
                    <span class="w-25 float-right text-right">
                      <span class="badge badge-danger-lighten">{{chat.text}}</span>
                    </span>
                    <span class="w-75">{{chat.message}}</span>
                  </p>
                </div>
              </div>
            </a>
          </simplebar>
        </b-tab>
      </b-tabs>
    </div>
    <!-- end card-body-->
  </div>
  <!-- end card-->
</template>