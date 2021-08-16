<template>
  <div class="blocker">
    
    <div class="stdForm">
      <div class="hl">Set App Accesess for User: {{dataIn.username}}</div>
      
      <div class="spacer" ></div>
      
      <div class="accessCheckBox" v-for="(access, idx) in accesses" :key="idx">
        <input type="checkbox" v-model="access.set" :id="'access_chk_'+idx" >
        <label :for="'access_chk_'+idx">{{access.name}}</label>
      </div>

      <div class="spacer" ></div>

      <div class="btnFrame">
        <button v-on:click="submit">ok</button>
        <button v-on:click="callback">cancel</button>
      </div>

    </div>
  
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SetAccessesUser',
  props: {
    dataIn: Object,
    callback: Function,
  },
  data(){
    return{
      apps:[],
      accesses:[],
      putData:{
        username: this.dataIn.username,
        role: ""
      }
    }
  },
  methods:{
    call_apps(){
      return axios.get("/api/apps").then(response => { 
        // console.log(response.data);
        this.apps = response.data.data;
      })
      .catch(error => {
        console.log(error);
        // this.$store.state.systemMsg = error.response.data.message;
      })
      .finally(()=> { 
      });
    },
    call_accesses(){
      axios.get("/api/accesses").then(response => { 
        // console.log(response.data);
        this.build_4_user(response.data.data);
      })
      .catch(error => {
        console.log(error);
        // this.$store.state.systemMsg = error.response.data.message;
      })
      .finally(()=> { 
      });
    },
    build_4_user(data){
      this.accesses = [];
      for(let idx in this.apps){
        let curApp = this.apps[idx];
        let curAccess = {
          id: curApp.id,
          name: curApp.name,
          set: false
        }
        for(let idx2 in data){
          if(data[idx2].app_id == curApp.id && data[idx2].user_id == this.dataIn.id){
            curAccess.set = true;
          }
        }
        this.accesses.push(curAccess);
      }
      // console.log(this.accesses);
    },

    submit(){
      
      // console.log(this.accesses);
      const postData = {
        delete: true,
        user_id: this.dataIn.id,
        app_ids: []
      }
      for(let idx in this.accesses){
        let curAccess = this.accesses[idx];
        if(curAccess.set){
          postData.app_ids.push(curAccess.id);
        }
      }
      // console.log(postData);

      this.$store.state.loader = true; 
      axios.post("/api/accesses/multiple", postData).then(response => { 
        console.log(response.data);
        this.callback();
      })
      .catch(error => {
        console.log(error);
        this.$store.state.systemMsg = error.response.data.message;
        this.callback();
      })
      .finally(()=> { 
        this.$store.state.loader = false; 
      });
      
    }
  },
  mounted: async function(){
    this.$store.state.loader = true; 
    await this.call_apps();
    this.call_accesses();
    this.$store.state.loader = false; 
  }
}
</script>


<style scoped>

</style>