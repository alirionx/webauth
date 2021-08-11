import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    appReady: false
  },
  mutations: {
    set_app_ready(state){
      state.appReady = true;
    },
    set_app_unready(state){
      state.appReady = false;
    },

  },
  actions: {
    check_app_ready(context){
      axios.get("/api/init").then(response => { 
        console.log(response.data);
        if(response.status == 200){
          context.commit('set_app_ready');
        }
        else{
          context.commit('set_app_unready');
        }
      })
      .catch(error => {
        console.log(error);
      });
    }
  },
  modules: {
  }
})
