// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import  qs from 'qs'
import Element from 'element-ui'
import EncryUtil from '@/utils/encrypt.js'
Vue.prototype.EncryUtil = EncryUtil


Vue.use(Element)

Vue.config.productionTip = false
Vue.prototype.$axios = axios
Vue.prototype.$qs = qs


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
