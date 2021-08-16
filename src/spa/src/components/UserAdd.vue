<template>
  <div class="blocker">
    
    <div class="stdForm">
      <div class="hl">{{title}}</div>

      <form @submit="submit">
      <div v-for="(col, idx) in defi" :key="idx">
        <div class="iptHl">{{col.hl}}</div>
        <input v-if="col.typ=='static'" type="text" disabled :required="col.manda" v-model="usrData[col.col]" />
        <input v-if="col.typ=='text'" type="text" :required="col.manda" v-model="usrData[col.col]" />
        <input v-if="col.typ=='email'" type="email" :required="col.manda" v-model="usrData[col.col]" />
        <input v-if="col.typ=='number'" type="number" :required="col.manda" v-model="usrData[col.col]" />
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
  name: 'UserAdd',
  props: {
    dataIn: Array,
    callback: Function
  },
  data(){
    return{
      title: "Add new User",
      usrData: {},
      defi:[
        {
          col: "username",
          hl: "Username",
          typ: "text",
          manda: true,
        },
        {
          col: "email",
          hl: "Email Address",
          typ: "email",
          manda: true,
        },
        {
          col: "company",
          hl: "Company",
          typ: "text",
          manda: false,
        },
        {
          col: "unit",
          hl: "Unit",
          typ: "text",
          manda: false,
        },
        {
          col: "phone",
          hl: "Phone",
          typ: "text",
          manda: false,
        },
        {
          col: "address",
          hl: "Address",
          typ: "text",
          manda: false,
        },
        {
          col: "zip",
          hl: "Zip Code",
          typ: "number",
          manda: false
        },
        {
          col: "city",
          hl: "City",
          typ: "text",
          manda: false
        },

      ]
    }
  },
  methods:{
    submit(){
      console.log(this.usrData);
      this.$store.state.loader = true;
      axios.post("/api/users", this.usrData).then(response => { 
        console.log(response.data);
        this.dataIn.push(this.usrData);
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
      this.usrData[this.defi[idx].col] = "";
    }
  }
}
</script>


<style scoped>

</style>