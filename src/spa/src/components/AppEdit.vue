<template>
  <div class="blocker">
    
    <div class="stdForm">
      <div class="hl">{{title}}</div>

      <form @submit="submit">
      <div v-for="(col, idx) in defi" :key="idx">
        <div class="iptHl">{{col.hl}}</div>
        <input v-if="col.typ=='static'" type="text" disabled :required="col.manda" v-model="dataIn[col.col]" />
        <input v-if="col.typ=='text'" type="text" :required="col.manda" v-model="dataIn[col.col]" />
        <input v-if="col.typ=='url'" type="url" :required="col.manda" v-model="dataIn[col.col]" />
        <input v-if="col.typ=='number'" type="number" :required="col.manda" v-model="dataIn[col.col]" />
        <select v-if="col.typ=='select'" :required="col.manda" v-model="dataIn[col.col]" >
          <option v-for="(opt, idx2) in col.dd" :key="idx2" :value="opt.key">{{opt.val}}</option>
        </select>
      </div>

      <div class="btnFrame">
        <button type="submit">submit</button>
        <button type="button" v-on:click="cancel">cancel</button>
      </div>
      
      </form>
    </div>
  
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'AppEdit',
  props: {
    dataIn: {},
    callback: Function
  },
  data(){
    return{
      title: "Edit App: "+this.dataIn.name,
      tmpData: {},
      defi:[
        {
          col: "name",
          hl: "App Name",
          typ: "static",
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
        },
        // {
        //   col: "jwt_algorithm",
        //   hl: "JWT Algorithm",
        //   typ: "select",
        //   dd:[
        //     {
        //       key: "HS256",
        //       val: "HMAC (HS256)"
        //     },
        //     {
        //       key: "RS256",
        //       val: "RSA (RS256)"
        //     }
        //   ],
        //   manda: true,
        // }
      ]
    }
  },
  methods:{
    submit(){
      // console.log(this.dataIn);
      this.$store.state.loader = true;
      axios.put("/api/apps/"+this.dataIn.name, this.dataIn).then(response => { 
        console.log(response.data);
        this.callback();
      })
      .catch(error => {
        console.log(error);
        this.$store.state.systemMsg = error.response.data.message;
        this.cancel();
      })
      .finally(()=> { 
        this.$store.state.loader = false; 
      });
    },

    reset_data(){
      for(let prop in this.tmpData){
        this.dataIn[prop] = this.tmpData[prop];
      }
    },
    cancel(){
      this.reset_data();
      this.callback();
    }
   
  },
  mounted: function(){
    this.tmpData = JSON.parse(JSON.stringify(this.dataIn));
    // console.log(this.tmpData);
  }
}
</script>


<style scoped>

</style>