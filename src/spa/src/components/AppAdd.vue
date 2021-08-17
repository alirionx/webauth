<template>
  <div class="blocker">
    
    <div class="stdForm">
      <div class="hl">{{title}}</div>

      <form @submit="submit">
      <div v-for="(col, idx) in defi" :key="idx">
        <div class="iptHl">{{col.hl}}</div>
        <input v-if="col.typ=='static'" type="text" disabled :required="col.manda" v-model="appData[col.col]" />
        <input v-if="col.typ=='text'" type="text" :required="col.manda" v-model="appData[col.col]" />
        <input v-if="col.typ=='url'" type="url" :required="col.manda" v-model="appData[col.col]" />
        <input v-if="col.typ=='number'" type="number" :required="col.manda" v-model="appData[col.col]" />
      </div>

      <div class="btnFrame">
        <button type="submit">submit</button>
        <button type="button" v-on:click="callback">cancel</button>
      </div>
      
      </form>
    </div>
  
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'AppAdd',
  props: {
    dataIn: Array,
    callback: Function
  },
  data(){
    return{
      title: "Add new App",
      appData: {},
      defi:[
        {
          col: "name",
          hl: "App Name",
          typ: "text",
          manda: true,
        },
        {
          col: "description",
          hl: "Description",
          typ: "text",
          manda: false,
        },
        {
          col: "app_url",
          hl: "App Url",
          typ: "url",
          manda: true,
        },
        {
          col: "auth_url",
          hl: "Authentification Url",
          typ: "url",
          manda: true,
        },
        {
          col: "session_key",
          hl: "Session Key",
          typ: "text",
          manda: true,
        }

      ]
    }
  },
  methods:{
    submit(){
      console.log(this.appData);
      this.$store.state.loader = true;
      axios.post("/api/apps", this.appData).then(response => { 
        console.log(response.data);
        this.dataIn.push(this.appData);
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
    },
   
  },
  mounted: function(){
    for(let idx in this.defi){
      this.appData[this.defi[idx].col] = "";
    }
  }
}
</script>


<style scoped>

</style>