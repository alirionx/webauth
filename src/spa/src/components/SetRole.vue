<template>
  <div class="blocker">
    
    <div class="stdForm">
      <div class="hl">Set Role for User: {{dataIn.username}}</div>
      
      <form @submit="submit">
        <select class="extra" v-model="putData.role" id="roleSelect">
          <option v-for="(role, idx) in roles" :key="idx" :value="role.key">{{role.val}}</option>
        </select>
      </form>


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
  name: 'SetRole',
  props: {
    dataIn: Object,
    callback: Function,
  },
  data(){
    return{
      roles:[
        {
          key: "",
          val: "Please select a role"
        },
        {
          key: "user",
          val: "App User"
        },
        {
          key: "admin",
          val: "User Admin"
        }
      ],
      putData:{
        username: this.dataIn.username,
        role: ""
      }
    }
  },
  methods:{
    submit(){
      if(this.putData.role==""){ // SEEEEEHR SCHÖN!!!
        let domEl = document.getElementById("roleSelect");
        let tmpCol = domEl.style.borderColor;
        domEl.style.borderColor = "red";
        setTimeout(()=>{ domEl.style.borderColor = tmpCol; },200)
        return
      }
      
      axios.put("/api/user/role", this.putData).then(response => { 
        console.log(response.data);
        if(!this.dataIn.role){
          this.dataIn.role = {};
        }
        this.dataIn.role.name = this.putData.role;
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
    if(this.dataIn.role){
      this.putData.role = this.dataIn.role.name;
    }
  }
}
</script>


<style scoped>

</style>