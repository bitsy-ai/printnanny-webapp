<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * FAQ component
 */
export default {
  page: {
    title: 'FAQ',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'FAQ',
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
          text: 'FAQ',
          active: true,
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
      <div class="col-sm-12">
        <div class="text-center">
          <h3 class>Frequently Asked Questions</h3>
          <p class="text-muted mt-3">
            Nisi praesentium similique totam odio obcaecati, reprehenderit,
            dignissimos rem temporibus ea inventore alias!
            <br />Beatae animi nemo ea
            tempora, temporibus laborum facilis ut!
          </p>

          <button type="button" class="btn btn-success btn-sm mt-2">
            <i class="mdi mdi-email-outline mr-1"></i> Email us your question
          </button>
          <button type="button" class="btn btn-info btn-sm mt-2 ml-2">
            <i class="mdi mdi-twitter mr-1"></i> Send us a tweet
          </button>
        </div>
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row pt-5">
      <div class="col-lg-5 offset-lg-1">
        <!-- Question/Answer -->
        <div>
          <div class="faq-question-q-box">Q.</div>
          <h4 class="faq-question" data-wow-delay=".1s">What is Lorem Ipsum?</h4>
          <p
            class="faq-answer mb-4"
          >Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.</p>
        </div>

        <!-- Question/Answer -->
        <div>
          <div class="faq-question-q-box">Q.</div>
          <h4 class="faq-question">Why use Lorem Ipsum?</h4>
          <p
            class="faq-answer mb-4"
          >Lorem ipsum dolor sit amet, in mea nonumes dissentias dissentiunt, pro te solet oratio iriure. Cu sit consetetur moderatius intellegam, ius decore accusamus te. Ne primis suavitate disputando nam. Mutat convenirete.</p>
        </div>

        <!-- Question/Answer -->
        <div>
          <div class="faq-question-q-box">Q.</div>
          <h4 class="faq-question">How many variations exist?</h4>
          <p
            class="faq-answer mb-4"
          >Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.</p>
        </div>

        <!-- Question/Answer -->
        <div>
          <div class="faq-question-q-box">Q.</div>
          <h4 class="faq-question" data-wow-delay=".1s">What is Lorem Ipsum?</h4>
          <p
            class="faq-answer mb-4"
          >Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.</p>
        </div>
      </div>
      <!--/col-md-5 -->

      <div class="col-lg-5">
        <!-- Question/Answer -->
        <div>
          <div class="faq-question-q-box">Q.</div>
          <h4 class="faq-question">Is safe use Lorem Ipsum?</h4>
          <p
            class="faq-answer mb-4"
          >Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.</p>
        </div>

        <!-- Question/Answer -->
        <div>
          <div class="faq-question-q-box">Q.</div>
          <h4 class="faq-question">When can be used?</h4>
          <p
            class="faq-answer mb-4"
          >Lorem ipsum dolor sit amet, in mea nonumes dissentias dissentiunt, pro te solet oratio iriure. Cu sit consetetur moderatius intellegam, ius decore accusamus te. Ne primis suavitate disputando nam. Mutat convenirete.</p>
        </div>

        <!-- Question/Answer -->
        <div>
          <div class="faq-question-q-box">Q.</div>
          <h4 class="faq-question">License &amp; Copyright</h4>
          <p
            class="faq-answer mb-4"
          >Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.</p>
        </div>

        <!-- Question/Answer -->
        <div>
          <div class="faq-question-q-box">Q.</div>
          <h4 class="faq-question">Is safe use Lorem Ipsum?</h4>
          <p
            class="faq-answer mb-4"
          >Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.</p>
        </div>
      </div>
      <!--/col-md-5-->
    </div>
    <!-- end row -->
  </Layout>
</template>