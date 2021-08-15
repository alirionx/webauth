import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Init from '../views/Init.vue'
import Login from '../views/Login.vue'

import store from '../store/index.js'
import axios from 'axios'


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
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/users',
    name: 'Users',
    component: function () {
      return import('../views/Users.vue')
    }
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


//-So wirds gemach!!!! und nicht anders!!!! :)---
router.beforeEach(async (to, from, next) => {
  if(to.name != "Init" && !store.state.appReady){
    if(!await check_app_ready()){
      var redirect = 'Init';
    }
  }
  //---------------
  if(to.name != "Login" && store.state.appReady && !store.state.role){
    if(!await check_login()){
      var redirect = 'Login';
    }
  }
  //---------------
  if(redirect) next({name: redirect})
  else next();
})

//-Async Backend Checks---
function check_app_ready(){
  return axios.get("/api/init").then(response => { 
    console.log(response.data);
    if(response.status == 200){
      store.commit('set_app_ready');
      return true;
    }
    else{
      store.commit('set_app_unready');
      return false;
    }
  })
  .catch(error => {
    console.log(error);
    store.commit("set_system_message", "Backend not reachable");
  });
}

//-----------------
function check_login(){
  return axios.get("/api/users/auth").then(response => { 
    console.log(response.data);
    store.commit('set_username', response.data.username);
    store.commit('set_role', response.data.role);
    return true;
  })
  .catch(error => {
    console.log(error);
    store.commit('unset_username');
    store.commit('unset_role');
    return false;
  });
}




//--------------------------------
export default router
