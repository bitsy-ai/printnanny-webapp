<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Scrollspy component
 */
export default {
  page: {
    title: 'Scrollspy',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Scrollspy',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Extended UI',
          href: '/',
        },
        {
          text: 'Scrollspy',
          active: true,
        },
      ],
    }
  },
  methods: {
    // Convenience method to scroll a heading into view.
    scrollIntoView(evt) {
      evt.preventDefault()
      const href = evt.target.getAttribute('href')
      const el = href ? document.querySelector(href) : null
      if (el) {
        this.$refs.content.scrollTop = el.offsetTop
      }
    },
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
            <h4 class="header-title">Example in navbar</h4>
            <p class="text-muted font-14">
              Scroll the area below the navbar and watch the active
              class change. The dropdown items will be highlighted as well.
            </p>
            <b-card no-body header-class="bg-light">
              <b-nav slot="header" v-b-scrollspy:nav-scroller pills card-header>
                <b-nav-item href="#fat" @click="scrollIntoView">@fat</b-nav-item>
                <b-nav-item href="#mdo" @click="scrollIntoView">@mdo</b-nav-item>
                <b-nav-item-dropdown text="Dropdown" right-alignment>
                  <b-dropdown-item href="#one" @click="scrollIntoView">one</b-dropdown-item>
                  <b-dropdown-item href="#two" @click="scrollIntoView">two</b-dropdown-item>
                  <b-dropdown-divider></b-dropdown-divider>
                  <b-dropdown-item href="#three" @click="scrollIntoView">three</b-dropdown-item>
                </b-nav-item-dropdown>
              </b-nav>

              <b-card-body
                id="nav-scroller"
                ref="content"
                class="pt-1"
                style="position:relative; height:200px; overflow-y:scroll;"
              >
                <h4 id="fat">@fat</h4>
                <p>
                  Ad leggings keytar, brunch id art party dolor labore. Pitchfork yr
                  enim lo-fi before they sold out qui. Tumblr farm-to-table bicycle
                  rights whatever. Anim keffiyeh carles cardigan. Velit seitan
                  mcsweeney's photo booth 3 wolf moon irure. Cosby sweater lomo jean
                  shorts, williamsburg hoodie minim qui you probably haven't heard of
                  them et cardigan trust fund culpa biodiesel wes anderson aesthetic.
                  Nihil tattooed accusamus, cred irony biodiesel keffiyeh artisan
                  ullamco consequat.
                </p>
                <h4 id="mdo">@mdo</h4>
                <p>
                  Veniam marfa mustache skateboard, adipisicing fugiat velit pitchfork
                  beard. Freegan beard aliqua cupidatat mcsweeney's vero. Cupidatat
                  four loko nisi, ea helvetica nulla carles. Tattooed cosby sweater
                  food truck, mcsweeney's quis non freegan vinyl. Lo-fi wes anderson
                  +1 sartorial. Carles non aesthetic exercitation quis gentrify.
                  Brooklyn adipisicing craft beer vice keytar deserunt.
                </p>
                <h4 id="one">one</h4>
                <p>
                  Occaecat commodo aliqua delectus. Fap craft beer deserunt skateboard
                  ea. Lomo bicycle rights adipisicing banh mi, velit ea sunt next
                  level locavore single-origin coffee in magna veniam. High life id
                  vinyl, echo park consequat quis aliquip banh mi pitchfork. Vero VHS
                  est adipisicing. Consectetur nisi DIY minim messenger bag. Cred ex
                  in, sustainable delectus consectetur fanny pack iphone.
                </p>
                <h4 id="two">two</h4>
                <p>
                  In incididunt echo park, officia deserunt mcsweeney's proident master
                  cleanse thundercats sapiente veniam. Excepteur VHS elit, proident
                  shoreditch +1 biodiesel laborum craft beer. Single-origin coffee
                  wayfarers irure four loko, cupidatat terry richardson master
                  cleanse. Assumenda you probably haven't heard of them art party
                  fanny pack, tattooed nulla cardigan tempor ad. Proident wolf
                  nesciunt sartorial keffiyeh eu banh mi sustainable. Elit wolf
                  voluptate, lo-fi ea portland before they sold out four loko.
                  Locavore enim nostrud mlkshk brooklyn nesciunt.
                </p>
                <h4 id="three">three</h4>
                <p>
                  Ad leggings keytar, brunch id art party dolor labore. Pitchfork yr
                  enim lo-fi before they sold out qui. Tumblr farm-to-table bicycle
                  rights whatever. Anim keffiyeh carles cardigan. Velit seitan
                  mcsweeney's photo booth 3 wolf moon irure. Cosby sweater lomo jean
                  shorts, williamsburg hoodie minim qui you probably haven't heard of
                  them et cardigan trust fund culpa biodiesel wes anderson aesthetic.
                  Nihil tattooed accusamus, cred irony biodiesel keffiyeh artisan
                  ullamco consequat.
                </p>
                <p>
                  Keytar twee blog, culpa messenger bag marfa whatever delectus food
                  truck. Sapiente synth id assumenda. Locavore sed helvetica cliche
                  irony, thundercats you probably haven't heard of them consequat
                  hoodie gluten-free lo-fi fap aliquip. Labore elit placeat before
                  they sold out, terry richardson proident brunch nesciunt quis cosby
                  sweater pariatur keffiyeh ut helvetica artisan. Cardigan craft beer
                  seitan readymade velit. VHS chambray laboris tempor veniam. Anim
                  mollit minim commodo ullamco thundercats.
                </p>
              </b-card-body>
            </b-card>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Example with nested nav</h4>
            <p class="text-muted font-14">
              Scrollspy also works with nested
              <code>.nav</code>s.
              If a nested
              <code>.nav</code> is
              <code>.active</code>, its parents will also be
              <code>.active</code>. Scroll the area next to the navbar and watch the active
              class change.
            </p>
            <b-row>
              <b-col cols="4">
                <b-navbar v-b-scrollspy:scrollspy-nested class="flex-column">
                  <b-navbar-brand href="#">Navbar</b-navbar-brand>
                  <b-nav pills vertical>
                    <b-nav-item href="#item-1">Item 1</b-nav-item>
                    <b-nav pills vertical>
                      <b-nav-item class="ml-3 my-1" href="#item-1-1">Item 1-1</b-nav-item>
                      <b-nav-item class="ml-3 my-1" href="#item-1-2">Item 1-2</b-nav-item>
                    </b-nav>
                    <b-nav-item href="#item-2">Item 2</b-nav-item>
                    <b-nav-item href="#item-3">Item 3</b-nav-item>
                    <b-nav pills vertical>
                      <b-nav-item class="ml-3 my-1" href="#item-3-1">Item 3-1</b-nav-item>
                      <b-nav-item class="ml-3 my-1" href="#item-3-2">Item 3-2</b-nav-item>
                    </b-nav>
                  </b-nav>
                </b-navbar>
              </b-col>

              <b-col cols="8">
                <div id="scrollspy-nested" style="position:relative; height:350px; overflow-y:auto">
                  <h4 id="item-1" style>Item 1</h4>
                  <p>
                    Ex consequat commodo adipisicing exercitation aute excepteur
                    occaecat ullamco duis aliqua id magna ullamco eu. Do aute
                    ipsum ipsum ullamco cillum consectetur ut et aute
                    consectetur labore. Fugiat laborum incididunt tempor eu
                    consequat enim dolore proident. Qui laborum do non excepteur
                    nulla magna eiusmod consectetur in. Aliqua et aliqua officia
                    quis et incididunt voluptate non anim reprehenderit
                    adipisicing dolore ut consequat deserunt mollit dolore.
                    Aliquip nulla enim veniam non fugiat id cupidatat nulla elit
                    cupidatat commodo velit ut eiusmod cupidatat elit dolore.
                  </p>
                  <h5 id="item-1-1" style>Item 1-1</h5>
                  <p>
                    Amet tempor mollit aliquip pariatur excepteur commodo do ea
                    cillum commodo Lorem et occaecat elit qui et. Aliquip labore
                    ex ex esse voluptate occaecat Lorem ullamco deserunt. Aliqua
                    cillum excepteur irure consequat id quis ea. Sit proident
                    ullamco aute magna pariatur nostrud labore. Reprehenderit
                    aliqua commodo eiusmod aliquip est do duis amet proident
                    magna consectetur consequat eu commodo fugiat non quis. Enim
                    aliquip exercitation ullamco adipisicing voluptate excepteur
                    minim exercitation minim minim commodo adipisicing
                    exercitation officia nisi adipisicing. Anim id duis qui
                    consequat labore adipisicing sint dolor elit cillum anim et
                    fugiat.
                  </p>
                  <h5 id="item-1-2" style>Item 1-2</h5>
                  <p>
                    Cillum nisi deserunt magna eiusmod qui eiusmod velit
                    voluptate pariatur laborum sunt enim. Irure laboris mollit
                    consequat incididunt sint et culpa culpa incididunt
                    adipisicing magna magna occaecat. Nulla ipsum cillum eiusmod
                    sint elit excepteur ea labore enim consectetur in labore
                    anim. Proident ullamco ipsum esse elit ut Lorem eiusmod
                    dolor et eiusmod. Anim occaecat nulla in non consequat
                    eiusmod velit incididunt.
                  </p>
                  <h4 id="item-2" style>Item 2</h4>
                  <p>
                    Quis magna Lorem anim amet ipsum do mollit sit cillum
                    voluptate ex nulla tempor. Laborum consequat non elit enim
                    exercitation cillum aliqua consequat id aliqua. Esse ex
                    consectetur mollit voluptate est in duis laboris ad sit
                    ipsum anim Lorem. Incididunt veniam velit elit elit veniam
                    Lorem aliqua quis ullamco deserunt sit enim elit aliqua esse
                    irure. Laborum nisi sit est tempor laborum mollit labore
                    officia laborum excepteur commodo non commodo dolor
                    excepteur commodo. Ipsum fugiat ex est consectetur ipsum
                    commodo tempor sunt in proident.
                  </p>
                  <h4 id="item-3" style>Item 3</h4>
                  <p>
                    Quis anim sit do amet fugiat dolor velit sit ea ea do
                    reprehenderit culpa duis. Nostrud aliqua ipsum fugiat minim
                    proident occaecat excepteur aliquip culpa aute tempor
                    reprehenderit. Deserunt tempor mollit elit ex pariatur
                    dolore velit fugiat mollit culpa irure ullamco est ex
                    ullamco excepteur.
                  </p>
                  <h5 id="item-3-1" style>Item 3-1</h5>
                  <p>
                    Deserunt quis elit Lorem eiusmod amet enim enim amet minim
                    Lorem proident nostrud. Ea id dolore anim exercitation aute
                    fugiat labore voluptate cillum do laboris labore. Ex velit
                    exercitation nisi enim labore reprehenderit labore nostrud
                    ut ut. Esse officia sunt duis aliquip ullamco tempor eiusmod
                    deserunt irure nostrud irure. Ullamco proident veniam
                    laboris ea consectetur magna sunt ex exercitation aliquip
                    minim enim culpa occaecat exercitation. Est tempor excepteur
                    aliquip laborum consequat do deserunt laborum esse eiusmod
                    irure proident ipsum esse qui.
                  </p>
                  <h5 id="item-3-2" style>Item 3-2</h5>
                  <p>
                    Labore sit culpa commodo elit adipisicing sit aliquip elit
                    proident voluptate minim mollit nostrud aute reprehenderit
                    do. Mollit excepteur eu Lorem ipsum anim commodo sint labore
                    Lorem in exercitation velit incididunt. Occaecat consectetur
                    nisi in occaecat proident minim enim sunt reprehenderit
                    exercitation cupidatat et do officia. Aliquip consequat ad
                    labore labore mollit ut amet. Sit pariatur tempor proident
                    in veniam culpa aliqua excepteur elit magna fugiat eiusmod
                    amet officia.
                  </p>
                </div>
              </b-col>
            </b-row>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Example with list-group</h4>
            <p class="text-muted font-14">
              Scrollspy also works with nested
              <code>.nav</code>s.
              If a nested
              <code>.nav</code> is
              <code>.active</code>, its parents will also be
              <code>.active</code>. Scroll the area next to the navbar and watch the active
              class change.
            </p>
            <b-row>
              <b-col cols="4">
                <b-list-group v-b-scrollspy:listgroup-ex>
                  <b-list-group-item href="#list-item-1">Item 1</b-list-group-item>
                  <b-list-group-item href="#list-item-2">Item2</b-list-group-item>
                  <b-list-group-item href="#list-item-3">Item 3</b-list-group-item>
                  <b-list-group-item href="#list-item-4">Item 4</b-list-group-item>
                </b-list-group>
              </b-col>

              <b-col cols="8">
                <div id="listgroup-ex" style="position:relative; overflow-y:auto; height:200px">
                  <h4 id="list-item-1">Item 1</h4>
                  <p>
                    Ex consequat commodo adipisicing exercitation aute excepteur
                    occaecat ullamco duis aliqua id magna ullamco eu. Do aute
                    ipsum ipsum ullamco cillum consectetur ut et aute
                    consectetur labore. Fugiat laborum incididunt tempor eu
                    consequat enim dolore proident. Qui laborum do non excepteur
                    nulla magna eiusmod consectetur in. Aliqua et aliqua officia
                    quis et incididunt voluptate non anim reprehenderit
                    adipisicing dolore ut consequat deserunt mollit dolore.
                    Aliquip nulla enim veniam non fugiat id cupidatat nulla elit
                    cupidatat commodo velit ut eiusmod cupidatat elit dolore.
                  </p>
                  <h4 id="list-item-2">Item 2</h4>
                  <p>
                    Quis magna Lorem anim amet ipsum do mollit sit cillum
                    voluptate ex nulla tempor. Laborum consequat non elit enim
                    exercitation cillum aliqua consequat id aliqua. Esse ex
                    consectetur mollit voluptate est in duis laboris ad sit
                    ipsum anim Lorem. Incididunt veniam velit elit elit veniam
                    Lorem aliqua quis ullamco deserunt sit enim elit aliqua esse
                    irure. Laborum nisi sit est tempor laborum mollit labore
                    officia laborum excepteur commodo non commodo dolor
                    excepteur commodo. Ipsum fugiat ex est consectetur ipsum
                    commodo tempor sunt in proident.
                  </p>
                  <h4 id="list-item-3">Item 3</h4>
                  <p>
                    Quis anim sit do amet fugiat dolor velit sit ea ea do
                    reprehenderit culpa duis. Nostrud aliqua ipsum fugiat minim
                    proident occaecat excepteur aliquip culpa aute tempor
                    reprehenderit. Deserunt tempor mollit elit ex pariatur
                    dolore velit fugiat mollit culpa irure ullamco est ex
                    ullamco excepteur.
                  </p>
                  <h4 id="list-item-4">Item 4</h4>
                  <p>
                    Quis anim sit do amet fugiat dolor velit sit ea ea do
                    reprehenderit culpa duis. Nostrud aliqua ipsum fugiat minim
                    proident occaecat excepteur aliquip culpa aute tempor
                    reprehenderit. Deserunt tempor mollit elit ex pariatur
                    dolore velit fugiat mollit culpa irure ullamco est ex
                    ullamco excepteur.
                  </p>
                </div>
              </b-col>
            </b-row>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->
  </Layout>
</template>