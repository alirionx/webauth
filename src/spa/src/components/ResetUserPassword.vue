<template>
  <div class="blocker">
    
    <div class="stdForm">
      <div class="hl">Re-/Set Password for User: {{dataIn.username}}</div>

      <form @submit="submit">
        
        <div class="iptHl">Enter Encryption Secret</div>
        <input type="password" required minlength="6" v-model="putData.password" />

        <div class="iptHl">Repeate Encryption Secret</div>
        <input type="password" required minlength="6" v-model="repPassword" />
        
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
  name: 'ResetUserPassword',
  props: {
    dataIn: Object,
    callback: Function,
  },
  data(){
    return{
      putData:{
        username: this.dataIn.username,
        password: ""
      },
      repPassword: ""
    }
  },
  methods:{
    submit(){
      if(this.putData.password!=this.repPassword){
        this.$store.state.systemMsg = "Password repeate does not fit.";
        this.putData.jwt_secret = "";
        this.repPassword = "";
        return
      }
      this.$store.state.loader = true; 
      axios.put("/api/user/auth", this.putData).then(response => { 
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
  mounted: function(){

  }
}
</script>


<style scoped>

</style>