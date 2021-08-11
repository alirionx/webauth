import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Init from '../views/Init.vue'

import store from '../store/index.js'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/init',
    name: 'Init',
    component: Init
  },
  {
    path: '/apps',
    name: 'Apps',
    component: function () {
      return import('../views/Apps.vue')
    }
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  setTimeout(function(){
    if (to.name !== 'Init' && !store.state.appReady){
      next({ name: 'Init' })
    }
    else{
      next()
    } 
  }, 200)
  
})

export default router
