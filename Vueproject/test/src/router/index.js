import Vue from 'vue'
import shouye from '@/components/shouye'
import VueRouter from 'vue-router'

Vue.use(VueRouter)


const routes = [
  {
    path: '/',
    name: 'shouye',
    component: shouye
  },
  {
    path: '/dingdan',
    name: 'dingdan',
    component: () => import('../components/dingdan.vue') 
  },
  {
    path: '/wode',
    name: 'wode',
    component: () => import('../components/wode.vue')
  },
  {
    path: '/faxian',
    name: 'faxian',
    component: () => import('../components/faxian.vue')
  },
]

const router = new VueRouter({
  linkActiveClass: 'active',
  routes
})

export default router
