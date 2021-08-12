<template>
  <div class="Init">

    <form @submit.prevent="submit">
    <div class="stdForm">
      <div class="hl">{{title}}</div>
      
      <div class="iptHl">Username of initial admin account </div>
      <input type="text" required v-model="formData.username" placeholder="required" />

      <div class="iptHl">Email</div>
      <input type="email" required v-model="formData.email" placeholder="required" />

      <div class="iptHl">Company</div>
      <input type="text" v-model="formData.company" />

      <div class="spacer"></div>

      <div class="iptHl">Password</div>
      <input type="password" required minlength="6" v-model="formData.password" />

      <div class="iptHl">Repeat Password</div>
      <input type="password" required v-model="repPassword" />

      <!--div class="spacer"></div-->

      <div class="btnFrame">
        <button>Submit</button>
        <button type="button" @click="reset_form" >Reset Form</button>
      </div>
    </div>
    </form>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Init',
  props: {
    msg: String
  },
  data(){
    return {
      componentTitle: "Init",
      title: "Backend Initialization",
      formData:{
        username: "",
        email: "",
        company: "",
        password: "",
      },
      repPassword: ""
    }
  },
  methods:{
    submit(){
      if(this.formData.password!=this.repPassword){
        this.$store.commit("set_system_message", "Password does not fit. Try Again...");
        this.formData.password = "";
        this.repPassword = "";
        return;
      }

      this.$store.state.loader = true;
      
      axios.post("/api/init", this.formData).then(response => { 
        console.log(response.data);
        location.hash = "/";
      })
      .catch(error => {
        console.log(error.response.data);
        this.$store.commit("set_system_message", "Failed to initialize the backend. Open console for details...");
        this.reset_form();
      })
      .finally(()=> { 
        this.$store.state.loader = false;
      });

    },

    reset_form(){
      this.formData = {
        username: "",
        email: "",
        company: "",
        password: "",
      };
      this.repPassword = "";
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



