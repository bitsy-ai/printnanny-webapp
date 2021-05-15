<script>
import CKEditor from '@ckeditor/ckeditor5-vue'
import ClassicEditor from '@ckeditor/ckeditor5-build-classic'
import VueSimplemde from 'vue-simplemde'

import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Editors component
 */
export default {
  page: {
    title: 'Editors',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: {
    Layout,
    PageHeader,
    ckeditor: CKEditor.component,
    VueSimplemde,
  },
  data() {
    return {
      title: 'Editors',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Forms',
          href: '/',
        },
        {
          text: 'Editors',
          active: true,
        },
      ],
      editor: ClassicEditor,
      editorData:
        '<h3>Hello World!</h3><h5><b>This is an simple editable area.</b></h5>',
      content: '',
      configs: {
        spellChecker: false,
        autosave: {
          enabled: true,
          unique_id: 'simplemde1',
        },
      },
    }
  },
}
</script>

<template>
  <Layout>
    <PageHeader :title="title" :items="items" />
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">CK Editor</h4>
            <p class="text-muted font-14">Example of CK Editor.</p>
            <!-- Editor -->
            <ckeditor v-model="editorData" :editor="editor"></ckeditor>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">SimpleMDE</h4>
            <p
              class="text-muted font-14"
            >SimpleMDE is a light-weight, simple, embeddable, and beautiful JS markdown editor</p>

            <vue-simplemde v-model="content" :configs="configs" />
          </div>
          <!-- end card-body-->
        </div>
        <!-- end card-->
      </div>
      <!-- end col-->
    </div>
    <!-- end row -->
  </Layout>
</template>