import store from '@state/store'

// auth related routes
const authRoutes = [
  {
    path: '/login',
    name: 'login',
    component: () => lazyLoadView(import('@views/account/login')),
    meta: {
      beforeResolve(routeTo, routeFrom, next) {
        // If the user is already logged in
        if (store.getters['auth/loggedIn']) {
          // Redirect to the home page instead
          next({ name: 'Ecommerce' })
        } else {
          // Continue to the login page
          next()
        }
      },
    },
  },
  {
    path: '/register',
    name: 'register',
    component: () => lazyLoadView(import('@views/account/register')),
    meta: {
      beforeResolve(routeTo, routeFrom, next) {
        // If the user is already logged in
        if (store.getters['auth/loggedIn']) {
          // Redirect to the home page instead
          next({ name: 'Ecommerce' })
        } else {
          // Continue to the login page
          next()
        }
      },
    },
  },
  {
    path: '/confirm-account',
    name: 'confirm-account',
    component: () => lazyLoadView(import('@views/account/confirm')),
    meta: {
      beforeResolve(routeTo, routeFrom, next) {
        // If the user is already logged in
        if (store.getters['auth/loggedIn']) {
          // Redirect to the home page instead
          next({ name: 'Ecommerce' })
        } else {
          // Continue to the login page
          next()
        }
      },
    },
  },
  {
    path: '/forget-password',
    name: 'forget-password',
    component: () =>
      lazyLoadView(import('@views/account/forgetPassword')),
    meta: {
      beforeResolve(routeTo, routeFrom, next) {
        // If the user is already logged in
        if (store.getters['auth/loggedIn']) {
          // Redirect to the home page instead
          next({ name: 'Ecommerce' })
        } else {
          // Continue to the login page
          next()
        }
      },
    },
  },
  {
    path: '/logout',
    name: 'logout',
    meta: {
      authRequired: true,
      beforeResolve(routeTo, routeFrom, next) {

        store.dispatch('auth/logOut')
        const authRequiredOnPreviousRoute = routeFrom.matched.some(
          (route) => route.meta.authRequired
        )
        // Navigate back to previous page, or home as a fallback
        next(
          authRequiredOnPreviousRoute ? { name: 'Ecommerce' } : { ...routeFrom }
        )
      },
    },
  },
]

// error pages
const errorPagesRoutes = [
  {
    path: '/404',
    name: '404',
    component: require('@views/pages/error-404').default,
    // Allows props to be passed to the 404 page through route
    // params, such as `resource` to define what wasn't found.
    props: true,
  },
  {
    path: '/500',
    name: '500',
    component: require('@views/pages/error-500').default,
    props: true,
  },
  // Redirect any unmatched routes to the 404 page. This may
  // require some server configuration to work in production:
  // https://router.vuejs.org/en/essentials/history-mode.html#example-server-configurations
  {
    path: '*',
    redirect: '404',
  },
]

// dashboard
const dashboardRoutes = [
  {
    path: '',
    name: 'Dashboards',
    header: 'Navigation',
    icon: 'uil-home-alt',
    badge: {
      text: '4',
      variant: 'success',
    },
    meta: { authRequired: true },
    redirect: { name: 'Ecommerce' },
    // create a container component
    component: {
      render(c) {
        return c('router-view')
      },
    },
    props: (route) => ({ user: store.state.auth.currentUser || {} }),
    children: [
      {
        name: 'Analytics',
        path: 'dashboard-analytics',
        meta: { authRequired: true },
        component: () =>
          lazyLoadView(import('@views/dashboards/analytics/')),
      },
      {
        name: 'CRM',
        path: 'dashboard-crm',
        meta: { authRequired: true },
        component: () =>
          lazyLoadView(import('@views/dashboards/crm/')),
      },
      {
        name: 'Ecommerce',
        path: '',
        meta: { authRequired: true },
        component: () =>
          lazyLoadView(import('@views/dashboards/ecommerce/')),
      },
      {
        name: 'Projects',
        path: 'dashboard-projects',
        meta: { authRequired: true },
        component: () =>
          lazyLoadView(import('@views/dashboards/projects/')),
      }
    ]
  }
]

// apps
const calendarAppsRoutes = [
  {
    path: '/apps/calendar',
    name: 'Calendar',
    header: 'Apps',
    icon: 'uil-calender',
    component: () => lazyLoadView(import('@views/apps/calendar/')),
    meta: { authRequired: true },
    props: (route) => ({ user: store.state.auth.currentUser || {} }),
  }
];

// apps chat
const chatAppsRoutes = [
  {
    path: '/apps/chat',
    name: 'Chat',
    icon: 'uil-comments-alt',
    component: () => lazyLoadView(import('@views/apps/chat/')),
    meta: { authRequired: true },
    props: (route) => ({ user: store.state.auth.currentUser || {} }),
  }
];

// apps ecommerce
const ecommerceAppsRoutes = [
  {
    path: '/apps/ecommerce',
    name: 'Ecommerce ',
    icon: 'uil-store',
    meta: { authRequired: true },
    // create a container component
    component: {
      render(c) {
        return c('router-view')
      },
    },
    props: (route) => ({ user: store.state.auth.currentUser || {} }),
    children: [
      {
        path: 'products',
        name: 'Products',
        component: () => lazyLoadView(import('@views/apps/ecommerce/products/'))
      },
      {
        path: 'products-detail',
        name: 'Products Detail',
        component: () => lazyLoadView(import('@views/apps/ecommerce/products-detail'))
      },
      {
        path: 'orders',
        name: 'Orders',
        component: () => lazyLoadView(import('@views/apps/ecommerce/orders/'))
      },
      {
        path: 'order-detail',
        name: 'Order Details',
        component: () => lazyLoadView(import('@views/apps/ecommerce/order-detail'))
      },
      {
        path: 'customers',
        name: 'Customers',
        component: () => lazyLoadView(import('@views/apps/ecommerce/customers/'))
      },
      {
        path: 'shopping-cart',
        name: 'Shopping Cart',
        component: () => lazyLoadView(import('@views/apps/ecommerce/shopping-cart'))
      },
      {
        path: 'checkout',
        name: 'Checkout',
        component: () => lazyLoadView(import('@views/apps/ecommerce/checkout'))
      },
      {
        path: 'sellers',
        name: 'Sellers',
        component: () => lazyLoadView(import('@views/apps/ecommerce/sellers/'))
      },
    ]
  }
]

// apps email
const emailAppsRoutes = [
  {
    path: '/apps/email',
    name: 'Email',
    icon: 'uil-envelope',
    meta: { authRequired: true },
    // create a container component
    component: {
      render(c) {
        return c('router-view')
      },
    },
    props: (route) => ({ user: store.state.auth.currentUser || {} }),
    children: [
      {
        name: 'Inbox',
        path: 'inbox',
        meta: { authRequired: true },
        component: () =>
          lazyLoadView(import('@views/apps/email/inbox/')),
      },
      {
        path: 'read',
        name: 'Read Email',
        meta: { authRequired: true },
        component: () =>
          lazyLoadView(import('@views/apps/email/read-email')),
      },
    ],
  }
];

// apps project
const projectAppsRoutes = [
  {
    path: '/apps/project',
    name: 'Project',
    icon: 'uil-briefcase',
    meta: { authRequired: true },
    // create a container component
    component: {
      render(c) {
        return c('router-view')
      },
    },
    props: (route) => ({ user: store.state.auth.currentUser || {} }),
    children: [
      {
        path: 'list',
        name: 'List',
        component: () =>
          lazyLoadView(import('@views/apps/projects/list/')),
      },
      {
        path: 'detail',
        name: 'Details',
        component: () =>
          lazyLoadView(import('@views/apps/projects/details/')),
      },
      {
        path: 'gantt',
        name: 'Gantt',
        component: () => lazyLoadView(import('@views/apps/projects/gantt'))
      },
      {
        path: 'create',
        name: 'Create Project',
        component: () => lazyLoadView(import('@views/apps/projects/create'))
      },
    ],
  }
];

// apps social-feed
const socialFeedAppsRoutes = [
  {
    path: '/apps/social-feed',
    name: 'Social Feed',
    icon: 'uil-rss',
    component: () => lazyLoadView(import('@views/apps/social-feed/')),
    meta: { authRequired: true },
    props: (route) => ({ user: store.state.auth.currentUser || {} }),
  }
];

// Apps tasks
const taskAppsRoutes = [
  {
    path: '/apps/tasks',
    name: 'Tasks',
    icon: 'uil-clipboard-alt',
    meta: { authRequired: true },
    // create a container component
    component: {
      render(c) {
        return c('router-view')
      },
    },
    props: (route) => ({ user: store.state.auth.currentUser || {} }),
    children: [
      {
        path: 'list',
        name: 'Task List',
        component: () => lazyLoadView(import('@views/apps/tasks/list/'))
      },
      {
        path: 'details',
        name: 'Detail',
        component: () => lazyLoadView(import('@views/apps/tasks/details/'))
      },
      {
        path: 'kanban',
        name: 'Kanban Board',
        component: () => lazyLoadView(import('@views/apps/tasks/kanban/'))
      },
    ]
  }
];

// pages
const pagesRoutes = [
  {
    path: '/pages',
    name: 'Pages',
    icon: 'uil-copy-alt',
    header: 'Custom',
    meta: { authRequired: true },
    // create a container component
    component: {
      render(c) {
        return c('router-view')
      },
    },
    children: [
      {
        path: 'profile',
        name: 'Profile',
        component: () => lazyLoadView(import('@views/pages/profile/'))
      },
      {
        path: 'profile2',
        name: 'Profile2',
        component: () => lazyLoadView(import('@views/pages/profile2/'))
      },
      {
        path: 'invoice',
        name: 'Invoice',
        component: () => lazyLoadView(import('@views/pages/invoice'))
      },
      {
        path: 'faq',
        name: 'FAQ',
        component: () => lazyLoadView(import('@views/pages/faq'))
      },
      {
        path: 'pricing',
        name: 'Pricing',
        component: () => lazyLoadView(import('@views/pages/pricing'))
      },
      {
        path: 'starter',
        name: 'Starter Page',
        component: () => lazyLoadView(import('@views/pages/starter'))
      },
      {
        path: 'timeline',
        name: 'Timeline',
        component: () => lazyLoadView(import('@views/pages/timeline'))
      },
    ],
  },
]

// ui
const uiRoutes = [
  {
    path: '/ui',
    name: 'UI Elements',
    icon: 'uil-box',
    header: 'Components',
    meta: { authRequired: true },
    // create a container component
    component: {
      render(c) {
        return c('router-view')
      },
    },
    children: [
      {
        path: 'base',
        name: 'Base UI',
        icon: 'uil-box',
        meta: { authRequired: true },
        component: {
          render(c) {
            return c('router-view')
          },
        },
        children: [
          {
            path: 'accordions',
            name: 'Accordions',
            component: () => lazyLoadView(import('@views/ui/accordions'))
          },
          {
            path: 'alerts',
            name: 'Alerts',
            component: () => lazyLoadView(import('@views/ui/alerts'))
          },
          {
            path: 'avatars',
            name: 'Avatars',
            component: () => lazyLoadView(import('@views/ui/avatars'))
          },
          {
            path: 'badges',
            name: 'Badges',
            component: () => lazyLoadView(import('@views/ui/badges'))
          },

          {
            path: 'breadcrumb',
            name: 'Breadcrumb',
            component: () => lazyLoadView(import('@views/ui/breadcrumb'))
          },
          {
            path: 'buttons',
            name: 'Buttons',
            component: () => lazyLoadView(import('@views/ui/buttons'))
          },
          {
            path: 'cards',
            name: 'Cards',
            component: () => lazyLoadView(import('@views/ui/cards'))
          },
          {
            path: 'carousel',
            name: 'Carousel',
            component: () => lazyLoadView(import('@views/ui/carousel'))
          },
          {
            path: 'dropdowns',
            name: 'Dropdowns',
            component: () => lazyLoadView(import('@views/ui/dropdowns'))
          },
          {
            path: 'embed-video',
            name: 'Video',
            component: () => lazyLoadView(import('@views/ui/embed-video'))
          },
          {
            path: 'grid',
            name: 'Grid',
            component: () => lazyLoadView(import('@views/ui/grid'))
          },
          {
            path: 'media-object',
            name: 'Media-object',
            component: () => lazyLoadView(import('@views/ui/media-object'))
          },
          {
            path: 'modals',
            name: 'Modals',
            component: () => lazyLoadView(import('@views/ui/modals'))
          },
          {
            path: 'notifications',
            name: 'Notifications',
            component: () => lazyLoadView(import('@views/ui/notifications'))
          },
          {
            path: 'pagination',
            name: 'Pagination',
            component: () => lazyLoadView(import('@views/ui/pagination'))
          },
          {
            path: 'popovers',
            name: 'Popovers',
            component: () => lazyLoadView(import('@views/ui/popovers'))
          },
          {
            path: 'progress',
            name: 'Progress',
            component: () => lazyLoadView(import('@views/ui/progress'))
          },
          {
            path: 'ribbons',
            name: 'Ribbons',
            component: () => lazyLoadView(import('@views/ui/ribbons'))
          },
          {
            path: 'spinners',
            name: 'Spinners',
            component: () => lazyLoadView(import('@views/ui/spinners'))
          },
          {
            path: 'tabs',
            name: 'Tabs',
            component: () => lazyLoadView(import('@views/ui/tabs'))
          },
          {
            path: 'tooltips',
            name: 'Tooltips',
            component: () => lazyLoadView(import('@views/ui/tooltips'))
          },
          {
            path: 'typography',
            name: 'Typography',
            component: () => lazyLoadView(import('@views/ui/typography'))
          },
        ],
      },
      {
        path: 'extended',
        name: 'Extended UI',
        icon: 'uil-package',
        meta: { authRequired: true },
        component: {
          render(c) {
            return c('router-view')
          },
        },
        children: [
          {
            path: 'dragula',
            name: 'Dragula',
            component: () => lazyLoadView(import('@views/extended/dragula'))
          },
          {
            path: 'range-slider',
            name: 'Range Slider',
            component: () => lazyLoadView(import('@views/extended/range-slider'))
          },
          {
            path: 'ratings',
            name: 'Ratings',
            component: () => lazyLoadView(import('@views/extended/ratings'))
          },
          {
            path: 'scrollbar',
            name: 'Scrollbar',
            component: () => lazyLoadView(import('@views/extended/scrollbar'))
          },
          {
            path: 'scrollspy',
            name: 'Scrollspy',
            component: () => lazyLoadView(import('@views/extended/scrollspy'))
          },
        ]
      },
      {
        path: 'widgets',
        name: 'Widgets',
        icon: 'uil-layer-group',
        component: () => lazyLoadView(import('@views/widgets/')),
        meta: { authRequired: true },
        props: (route) => ({ user: store.state.auth.currentUser || {} }),
      },
      {
        path: 'icons',
        name: 'Icons',
        icon: 'uil-streering',
        meta: { authRequired: true },
        component: {
          render(c) {
            return c('router-view')
          },
        },
        props: (route) => ({ user: store.state.auth.currentUser || {} }),
        children: [
          {
            path: 'dripicons',
            name: 'Dripicons',
            component: () => lazyLoadView(import('@views/icons/dripicons'))
          },
          {
            path: 'mdi',
            name: 'Material Design',
            component: () => lazyLoadView(import('@views/icons/material-design'))
          },
          {
            path: 'unicons',
            name: 'Unicons',
            component: () => lazyLoadView(import('@views/icons/unicons'))
          },
        ]
      }
    ]
  }
]

// forms
const formsRoutes = [
  {
    path: 'forms',
    name: 'Forms',
    icon: 'uil-document-layout-center',
    meta: { authRequired: true },
    // create a container component
    component: {
      render(c) {
        return c('router-view')
      },
    },
    props: (route) => ({ user: store.state.auth.currentUser || {} }),
    children: [
      {
        path: 'elements',
        name: 'Basic Elements',
        component: () => lazyLoadView(import('@views/form/elements'))
      },
      {
        path: 'advanced',
        name: 'Form Advanced',
        component: () => lazyLoadView(import('@views/form/advanced'))
      },
      {
        path: 'validation',
        name: 'Validation',
        component: () => lazyLoadView(import('@views/form/validation'))
      },
      {
        path: 'wizard',
        name: 'Wizard',
        component: () => lazyLoadView(import('@views/form/wizard/'))
      },
      {
        path: 'fileuploads',
        name: 'File Uploads',
        component: () => lazyLoadView(import('@views/form/fileuploads'))
      },
      {
        path: 'editor',
        name: 'Editors',
        component: () => lazyLoadView(import('@views/form/editor'))
      },
    ]
  }
]

// charts
const chartsRoutes = [
  {
    path: 'charts',
    name: 'Charts',
    icon: 'uil-chart',
    meta: { authRequired: true },
    // create a container component
    component: {
      render(c) {
        return c('router-view')
      },
    },
    children: [
      {
        path: 'apex',
        name: 'Apex Charts',
        // create a container component
        component: {
          render(c) {
            return c('router-view')
          },
        },
        children: [
          {
            path: 'area',
            name: 'Area',
            component: () => lazyLoadView(import('@views/charts/apex/area'))
          },
          {
            path: 'bar',
            name: 'Bar',
            component: () => lazyLoadView(import('@views/charts/apex/bar'))
          },
          {
            path: 'bubble',
            name: 'Bubble',
            component: () => lazyLoadView(import('@views/charts/apex/bubble'))
          },
          {
            path: 'candlestick',
            name: 'Candlestick',
            component: () => lazyLoadView(import('@views/charts/apex/candlestick'))
          },
          {
            path: 'column',
            name: 'Column',
            component: () => lazyLoadView(import('@views/charts/apex/column'))
          },
          {
            path: 'heatmap',
            name: 'Heatmap',
            component: () => lazyLoadView(import('@views/charts/apex/heatmap'))
          },
          {
            path: 'line',
            name: 'Line',
            component: () => lazyLoadView(import('@views/charts/apex/line'))
          },
          {
            path: 'mixed',
            name: 'Mixed',
            component: () => lazyLoadView(import('@views/charts/apex/mixed'))
          },
          {
            path: 'pie',
            name: 'Pie',
            component: () => lazyLoadView(import('@views/charts/apex/pie'))
          },
          {
            path: 'radar',
            name: 'Radar',
            component: () => lazyLoadView(import('@views/charts/apex/radar'))
          },
          {
            path: 'radialbar',
            name: 'Radialbar',
            component: () => lazyLoadView(import('@views/charts/apex/radialbar'))
          },
          {
            path: 'scatter',
            name: 'Scatter',
            component: () => lazyLoadView(import('@views/charts/apex/scatter'))
          },
        ]
      },
      {
        path: 'chartjs',
        name: 'Chartjs',
        component: () => lazyLoadView(import('@views/charts/chartjs/'))
      },
    ]
  }
]

// tables
const tablesRoutes = [
  {
    path: 'tables',
    name: 'Tables',
    icon: 'uil-table',
    meta: { authRequired: true },
    // create a container component
    component: {
      render(c) {
        return c('router-view')
      },
    },
    children: [
      {
        path: 'basic',
        name: 'Basic Tables',
        component: () =>
          lazyLoadView(import('@views/tables/basictable')),
      },
      {
        path: 'advanced',
        name: 'Advanced Tables',
        component: () =>
          lazyLoadView(import('@views/tables/advanced-table')),
      },
    ],
  },
]

// map
const mapRoutes = [
  {
    path: 'google-map',
    name: 'Google Maps',
    icon: 'uil-location-point',
    component: () => lazyLoadView(import('@views/maps/google')),
    meta: { authRequired: true },
  }
]

const componentRoutes = [
  {
    path: '/advanced-ui',
    name: 'Advanced',
    icon: 'uil-document-layout-center',
    meta: { authRequired: true },
    component: {
      render(c) {
        return c('router-view')
      },
    },
    children: [
      ...formsRoutes,
      ...chartsRoutes,
      ...tablesRoutes,
      ...mapRoutes
    ]
  }
]

const authProtectedRoutes = [
  ...dashboardRoutes,
  ...calendarAppsRoutes,
  ...chatAppsRoutes,
  ...ecommerceAppsRoutes,
  ...emailAppsRoutes,
  ...projectAppsRoutes,
  ...socialFeedAppsRoutes,
  ...taskAppsRoutes,
  ...pagesRoutes,
  ...uiRoutes,
  ...componentRoutes
]

const allRoutes = [...authRoutes, ...authProtectedRoutes, ...errorPagesRoutes]

export { allRoutes, authProtectedRoutes }
// Lazy-loads view components, but with better UX. A loading view
// will be used if the component takes a while to load, falling
// back to a timeout view in case the page fails to load. You can
// use this component to lazy-load a route with:
//
// component: () => lazyLoadView(import('@views/my-view'))
//
// NOTE: Components loaded with this strategy DO NOT have access
// to in-component guards, such as beforeRouteEnter,
// beforeRouteUpdate, and beforeRouteLeave. You must either use
// route-level guards instead or lazy-load the component directly:
//
// component: () => import('@views/my-view')
//
function lazyLoadView(AsyncView) {
  const AsyncHandler = () => ({
    component: AsyncView,
    // A component to use while the component is loading.
    loading: require('@views/_loading').default,
    // Delay before showing the loading component.
    // Default: 200 (milliseconds).
    delay: 400,
    // A fallback component in case the timeout is exceeded
    // when loading the component.
    // error: require('@views/_timeout').default,
    // Time before giving up trying to load the component.
    // Default: Infinity (milliseconds).
    timeout: 10000,
  })

  return Promise.resolve({
    functional: true,
    render(h, { data, children }) {
      // Transparently pass any props or children
      // to the view component.
      return h(AsyncHandler, data, children)
    },
  })
}
