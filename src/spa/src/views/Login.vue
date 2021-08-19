<template>
  <div class="Login">
   <form @submit.prevent="login">
    <div class="stdForm" style="margin-top:10vh;">
      <div class="hl">{{title}}</div>

      <div class="iptHl">Username</div>
      <input type="text" required v-model="formData.username" />

      <div class="iptHl">Password</div>
      <input type="password" required v-model="formData.password" />

      <div class="btnFrame">
        <button>Login</button>
      </div>
    </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Login',
  props: {
    msg: String
  },
  data(){
    return {
      componentTitle: "Login",
      title: "User Login",
      formData: {
        username: "",
        password: ""
      }
    }
  },
  methods:{
    login(){
      axios.post("/api/user/auth", this.formData).then(response => { 
        console.log(response.data);
        location.hash = "/";
      })
      .catch(error => {
        console.log(error.response.data);
        this.$store.commit("set_system_message", "Login Failed!");
        this.formData = { username: "", password: "" };
      })
      .finally(()=> { 

      });
    }
    
  },
  mounted: function(){
    
  },
  created: function(){
    
  }
  
}
</script>

<style scoped>
h2{
  padding:10px;
  color: rgb(36, 57, 85);
}
</style>



