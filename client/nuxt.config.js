import webpack from 'webpack'
const pkg = require('./package')
require('dotenv').config()

module.exports = {
  mode: 'spa',

  /*
  ** Headers of the page
  */
  head: {
    title: 'Cura Network Bounty',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: pkg.description }
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }]
  },

  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },

  /*
  ** Global CSS
  */
  css: [],

  /*
  ** Plugins to load before mounting the App
  */
  plugins: [],

  /*
  ** Nuxt.js modules
  */
  modules: [
    // Doc: https://github.com/nuxt-community/axios-module#usage
    '@nuxtjs/axios',
    // Doc: https://auth.nuxtjs.org/
    '@nuxtjs/auth',
    [
      'nuxt-validate',
      {
        locale: 'en'
      }
    ],
    // Doc: https://bootstrap-vue.js.org/docs/
    'bootstrap-vue/nuxt',
    'nuxt-fontawesome'
  ],

  /*
  ** Axios module configuration
  */
  axios: {
    // See https://github.com/nuxt-community/axios-module#options
    https: false,
    baseURL: process.env.BASE_URL,
    credentials: true,
    retry: { retries: 3 }
  },

  /*
  ** Authentication module configuration
  */
  auth: {
    // See https://auth.nuxtjs.org/
    redirect: {
      login: '/',
      logout: '/',
      home: '/in',
      callback: false,
      user: '/profile'
    },
    cookie: {
      options: {
        secure: false
      }
    },
    resetOnError: false,
    fullPathRedirect: true,
    scopeKey: 'roles',
    strategies: {
      local: {
        endpoints: {
          login: {
            url: '/auth/jwt/create',
            method: 'post',
            propertyName: 'token'
          },
          logout: false,
          user: { url: '/auth/me', method: 'get', propertyName: '' }
        },
        tokenRequired: true,
        tokenType: 'JWT'
      }
    }
  },

  /*
  ** Build configuration
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    extend(config, ctx) {
      // Run ESLint on save
      if (ctx.isDev && ctx.isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    },
    plugins: [
      new webpack.ProvidePlugin({
        _: 'lodash'
        // ...etc.
      })
    ]
  }
}
