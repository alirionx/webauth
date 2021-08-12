import { createStore } from 'vuex'

export default createStore({
  state: {
    appReady: false,
    username: null,
    role: null,
    systemMsg: null,
    confirmMsg: null,
  },
  mutations: {
    set_app_ready(state){
      state.appReady = true;
    },
    set_app_unready(state){
      state.appReady = false;
    },

    set_username(state, username){
      state.username = username;
    },
    unset_username(state){
      state.username = null;
    },
    set_role(state, role){
      state.role = role;
    },
    unset_role(state){
      state.role = null;
    },

    set_system_message(state, msg){
      state.systemMsg = msg;
    },
    unset_system_message(state){
      state.systemMsg = null;
    },

  },
  actions: {
    
  },
  modules: {
  }
})
