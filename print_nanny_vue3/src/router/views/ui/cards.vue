<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Cards component
 */
export default {
  page: {
    title: 'Cards',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Cards',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Base UI',
          href: '/',
        },
        {
          text: 'Cards',
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
      <div class="col-md-6 col-lg-3">
        <!-- Simple card -->
        <b-card :img-src="require('@assets/images/small/small-1.jpg')" img-alt="Card image" img-top>
          <b-card-title>
            <h5 class="card-title">Card title</h5>
          </b-card-title>
          <b-card-text>Some quick example text to build on the card title and make up the bulk of the card's content. Some quick example text to build on the card title and make up.</b-card-text>
          <b-button href="javascript:void(0);" variant="primary">Button</b-button>
        </b-card>
      </div>
      <!-- end col -->

      <div class="col-md-6 col-lg-3">
        <b-card
          no-body
          :img-src="require('@assets/images/small/small-2.jpg')"
          img-alt="Card image"
          img-top
        >
          <b-card-body>
            <b-card-title>
              <h5 class="card-title">Card title</h5>
            </b-card-title>
            <b-card-text>Some quick example text to build on the card..</b-card-text>
          </b-card-body>
          <ul class="list-group list-group-flush">
            <li class="list-group-item">Cras justo odio</li>
          </ul>
          <div class="card-body">
            <a href="javascript:void(0);" class="card-link text-custom">Card link</a>
            <a href="javascript:void(0);" class="card-link text-custom">Another link</a>
          </div>
        </b-card>
      </div>
      <!-- end col -->

      <div class="col-md-6 col-lg-3">
        <b-card :img-src="require('@assets/images/small/small-3.jpg')" img-alt="Card image" img-top>
          <b-card-text>Some quick example text to build on the card title and make up the bulk of the card's content. Some quick example text to build on the card title and make up.</b-card-text>
          <b-button href="javascript:void(0);" variant="primary">Button</b-button>
        </b-card>
      </div>
      <!-- end col -->

      <div class="col-md-6 col-lg-3">
        <b-card no-body>
          <b-card-body>
            <b-card-title>
              <h5 class="card-title">Card title</h5>
            </b-card-title>
            <b-card-sub-title>
              <h6 class="card-subtitle text-muted">Support card subtitle</h6>
            </b-card-sub-title>
          </b-card-body>
          <img src="@assets/images/small/small-4.jpg" class="img-fluid" />
          <b-card-body>
            <b-card-text>Some quick example text to build on the card title and make up the bulk of the card's content.</b-card-text>
            <a href="javascript:void(0);" class="card-link text-custom">Card link</a>
            <a href="javascript:void(0);" class="card-link text-custom">Another link</a>
          </b-card-body>
        </b-card>
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->
    <div class="row">
      <div class="col-lg-6">
        <b-card no-body>
          <b-card-body>
            <b-card-title>
              <h5 class="card-title">Special title treatment</h5>
            </b-card-title>
            <b-card-text>
              With supporting text below as a natural lead-in to additional
              content.
            </b-card-text>
            <a href="javascript:void(0);" class="btn btn-primary btn-block">Go somewhere</a>
          </b-card-body>
        </b-card>
      </div>
      <div class="col-lg-6">
        <b-card no-body>
          <b-card-body>
            <b-card-title>
              <h5 class="card-title">Special title treatment</h5>
            </b-card-title>
            <b-card-text>
              With supporting text below as a natural lead-in to additional
              content.
            </b-card-text>
            <a href="javascript:void(0);" class="btn btn-primary btn-block">Go somewhere</a>
          </b-card-body>
        </b-card>
      </div>
    </div>
    <!-- end row -->
    <div class="row">
      <div class="col-md-4">
        <b-card>
          <b-card-title>
            <h5 class="card-title">Special title treatment</h5>
          </b-card-title>
          <h6 slot="header" class="m-0">Featured</h6>
          <b-card-text>With supporting text below as a natural lead-in to additional content.</b-card-text>
          <b-button href="#" variant="primary">Go somewhere</b-button>
        </b-card>
      </div>
      <div class="col-md-4">
        <b-card header="Quote">
          <b-card-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</b-card-text>
          <footer>
            Someone famous in
            <cite title="Source Title">Source Title</cite>
          </footer>
        </b-card>
      </div>
      <div class="col-md-4">
        <b-card header="Featured" footer="2 days ago" footer-class="text-muted">
          <b-card-text>
            <a href="#" class="btn btn-primary">Go somewhere</a>
          </b-card-text>
        </b-card>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <h4 class="mb-4">Card Colored</h4>
      </div>
      <!-- end col -->
    </div>

    <div class="row">
      <div class="col-md-4">
        <b-card bg-variant="secondary" text-variant="white">
          <b-card-title>
            <h5 class="card-title text-white">Special title treatment</h5>
          </b-card-title>
          <b-card-text>With supporting text below as a natural lead-in to additional content.</b-card-text>
          <b-button href="#" variant="primary">Button</b-button>
        </b-card>
      </div>
      <div class="col-md-4">
        <b-card bg-variant="primary" text-variant="white">
          <blockquote class="card-bodyquote">
            <b-card-text>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
              <footer>
                Someone famous in
                <cite title="Source Title">Source Title</cite>
              </footer>
            </b-card-text>
          </blockquote>
        </b-card>
      </div>
      <div class="col-md-4">
        <b-card bg-variant="success" text-variant="white">
          <blockquote class="card-bodyquote">
            <b-card-text>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
              <footer>
                Someone famous in
                <cite title="Source Title">Source Title</cite>
              </footer>
            </b-card-text>
          </blockquote>
        </b-card>
      </div>
    </div>
    <div class="row">
      <div class="col-md-4">
        <b-card bg-variant="info" text-variant="white">
          <blockquote class="card-bodyquote">
            <b-card-text>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
              <footer>
                Someone famous in
                <cite title="Source Title">Source Title</cite>
              </footer>
            </b-card-text>
          </blockquote>
        </b-card>
      </div>
      <div class="col-md-4">
        <b-card bg-variant="warning" text-variant="white">
          <blockquote class="card-bodyquote">
            <b-card-text>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
              <footer>
                Someone famous in
                <cite title="Source Title">Source Title</cite>
              </footer>
            </b-card-text>
          </blockquote>
        </b-card>
      </div>
      <div class="col-md-4">
        <b-card bg-variant="danger" text-variant="white">
          <blockquote class="card-bodyquote">
            <b-card-text>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
              <footer>
                Someone famous in
                <cite title="Source Title">Source Title</cite>
              </footer>
            </b-card-text>
          </blockquote>
        </b-card>
      </div>
    </div>
    <!-- row -->
    <div class="row">
      <div class="col-12">
        <h4 class="mt-2 mb-3">Groups</h4>
        <b-card-group>
          <b-card :img-src="require('@assets/images/small/small-1.jpg')" img-alt="Card image" img-top>
            <b-card-title>
              <h5 class="card-title">Card title</h5>
            </b-card-title>
            <b-card-text>
              <p>This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              <p>
                <small class="text-muted">Last updated 3 mins ago</small>
              </p>
            </b-card-text>
          </b-card>
          <b-card :img-src="require('@assets/images/small/small-2.jpg')" img-alt="Card image" img-top>
            <b-card-title>
              <h5 class="card-title">Card title</h5>
            </b-card-title>
            <b-card-text>
              <p>This card has supporting text below as a natural lead-in to additional content.</p>
              <p>
                <small class="text-muted">Last updated 3 mins ago</small>
              </p>
            </b-card-text>
          </b-card>
          <b-card :img-src="require('@assets/images/small/small-3.jpg')" img-alt="Card image" img-top>
            <b-card-title>
              <h5 class="card-title">Card title</h5>
            </b-card-title>
            <b-card-text>
              <p>This is a wider card with supporting text below as a natural lead-in to additional content. This card has even longer content than the first to show that equal height action.</p>
              <p>
                <small class="text-muted">Last updated 3 mins ago</small>
              </p>
            </b-card-text>
          </b-card>
        </b-card-group>
      </div>
    </div>
    <!-- row -->
    <div class="row mb-3">
      <div class="col-12">
        <h4 class="my-4">Decks</h4>
        <b-card-group deck>
          <b-card :img-src="require('@assets/images/small/small-4.jpg')" img-alt="Card image" img-top>
            <b-card-title>
              <h5 class="card-title">Card title</h5>
            </b-card-title>
            <b-card-text>
              <p>This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              <p>
                <small class="text-muted">Last updated 3 mins ago</small>
              </p>
            </b-card-text>
          </b-card>
          <b-card :img-src="require('@assets/images/small/small-1.jpg')" img-alt="Card image" img-top>
            <b-card-title>
              <h5 class="card-title">Card title</h5>
            </b-card-title>
            <b-card-text>
              <p>This card has supporting text below as a natural lead-in to additional content.</p>
              <p>
                <small class="text-muted">Last updated 3 mins ago</small>
              </p>
            </b-card-text>
          </b-card>
          <b-card :img-src="require('@assets/images/small/small-2.jpg')" img-alt="Card image" img-top>
            <b-card-title>
              <h5 class="card-title">Card title</h5>
            </b-card-title>
            <b-card-text>
              <p>This is a wider card with supporting text below as a natural lead-in to additional content. This card has even longer content than the first to show that equal height action.</p>
              <p>
                <small class="text-muted">Last updated 3 mins ago</small>
              </p>
            </b-card-text>
          </b-card>
        </b-card-group>
      </div>
    </div>
    <!-- row -->
  </Layout>
</template>