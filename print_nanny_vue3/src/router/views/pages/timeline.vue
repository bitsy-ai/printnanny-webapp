<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Timeline component
 */
export default {
  page: {
    title: 'Timeline',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Timeline',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Pages',
          href: '/',
        },
        {
          text: 'Timeline',
          active: true,
        },
      ],
      timelineData: [
        {
          buttonText: 'Today',
        },
        {
          title: 'Completed UX design project for our client',
          date: '22 July, 2019',
          text:
            'Dolorum provident rerum aut hic quasi placeat iure tempora laudantium ipsa ad debitis unde?',
          button: '👍 17',
          align: 'left',
        },
        {
          title: 'Yay! We are celebrating our first admin release.',
          date: '22 July, 2019',
          text: `Consectetur adipisicing elit. Iusto, optio, dolorum John deon provident rerum aut hic quasi placeat iure tempora laudantium`,
          button: '🎉 148',
        },
        {
          buttonText: 'Yesterday',
        },
        {
          title: 'We released new version of our theme Ubold.',
          date: '21 July, 2019',
          text: '3 new photo Uploaded on facebook fan page',
          button: '🏆 94',
          align: 'left',
        },
        {
          title: 'We have archieved 25k sales in our themes.',
          date: '21 July, 2019',
          text:
            'Outdoor visit at California State Route 85 with John Boltana & Harry Piterson regarding to setup a new show room.',
          button: '👍 1.4k',
        },
        {
          title: 'Conference call with UX team',
          date: '21 July, 2019',
          text:
            'Jonatha Smith added new milestone Pathek Lorem ipsum dolor sit amet consiquest dio',
          button: '❤️ 89',
          align: 'left',
        },
        {
          buttonText: '2018',
        },
        {
          title: 'Join new team member Alex Smith',
          date: '10 December, 2018',
          text:
            'Alex Smith is a Senior Software (Full Stack) engineer with a deep passion for building usable, functional & pretty web applications.',
        },
        {
          title: 'First release of Hyper admin dashboard template',
          date: '16 July, 2018',
          text:
            'Outdoor visit at California State Route 85 with John Boltana & Harry Piterson regarding to setup a new show room.',
          button: '🎉 10k',
          align: 'left',
        },
      ],
    }
  },
}
</script>

<template>
  <Layout>
    <PageHeader :title="title" :items="items" />
    <div class="row">
      <div class="col-12">
        <div class="timeline">
          <div v-for="item of timelineData" :key="item.title">
            <div v-if="item.buttonText" class="timeline-show my-3 text-center">
              <h5 class="m-0 time-show-name">{{item.buttonText}}</h5>
            </div>
            <div
              v-if="!item.buttonText"
              class="timeline-lg-item d-flex"
              :class=" { 'timeline-item-left': item.align === 'left' } "
            >
              <div class="timeline-desk">
                <div class="timeline-box">
                  <span class="arrow-alt" :class="{ 'arrow': item.align !== 'left' }"></span>
                  <span class="timeline-icon">
                    <i class="mdi mdi-adjust"></i>
                  </span>
                  <h4 class="mt-0 mb-1 font-16">{{item.title}}</h4>
                  <p class="text-muted">
                    <small>{{item.date}}</small>
                  </p>
                  <p>{{item.text}}</p>

                  <a
                    v-if="item.button"
                    href="javascript: void(0);"
                    class="btn btn-sm btn-light"
                  >{{ item.button }}</a>
                
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- end timeline -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->
  </Layout>
</template>