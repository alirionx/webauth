<template>
  <div class="blocker">
    
    <div class="stdForm">
      <div class="hl">Configure JWT for App: {{dataIn.name}}</div>
      
      <form @submit="submit">

        <div class="iptHl">Select an encryption Algorthm</div>
        <select class="extra" v-model="postData.jwt_algorithm" >
          <option v-for="(algo, idx) in algos" :key="idx" :value="algo.key">{{algo.val}}</option>
        </select>

        <div class="iptHl">Enter Encryption Secret</div>
        <input type="password" required minlength="6" v-model="postData.jwt_secret" />

        <div class="iptHl">Repeate Encryption Secret</div>
        <input type="password" required minlength="6" v-model="repSecret" />

        <div class="btnFrame">
          <button type="submit">ok</button>
          <button type="button" v-on:click="callback">cancel</button>
        </div>

      </form>

    </div>
  
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SetJwt',
  props: {
    dataIn: Object,
    callback: Function,
  },
  data(){
    return{
      tmpAlgo: "",
      algos:[
        {
          key: "HS256",
          val: "HMAC (HS256)"
        },
        {
          key: "RS256",
          val: "RSA (RS256)"
        }
      ],
      postData:{
        app: this.dataIn.name,
        jwt_algorithm: "HS256",
        jwt_secret: ""
      },
      repSecret: "",
    }
  },
  methods:{
    submit(){
      if(this.postData.jwt_secret!=this.repSecret){
        this.$store.state.systemMsg = "Secret repeate does not fit.";
        this.postData.jwt_secret = "";
        this.repSecret = "";
        return
      }

      axios.post("/api/app/jwt", this.postData).then(response => { 
        console.log(response.data);
        this.dataIn.jwt_algorithm = this.postData.jwt_algorithm;
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
  mounted: function(){
    if(this.dataIn.jwt_algorithm && this.dataIn.jwt_algorithm != "" ){
      this.postData.jwt_algorithm = this.dataIn.jwt_algorithm;
    }
  }
}
</script>


<style scoped>

</style>