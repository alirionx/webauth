<template>
  <div class="blocker">
    
    <div class="stdForm">
      <div class="hl">{{title}}</div>

      <form @submit="submit">
      <div v-for="(col, idx) in defi" :key="idx">
        <div class="iptHl">{{col.hl}}</div>
        <input v-if="col.typ=='static'" type="text" disabled :required="col.manda" v-model="dataIn[col.col]" />
        <input v-if="col.typ=='text'" type="text" :required="col.manda" v-model="dataIn[col.col]" />
        <input v-if="col.typ=='email'" type="email" :required="col.manda" v-model="dataIn[col.col]" />
        <input v-if="col.typ=='number'" type="number" :required="col.manda" v-model="dataIn[col.col]" />
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
  name: 'UserEdit',
  props: {
    dataIn: {},
    callback: Function
  },
  data(){
    return{
      title: "Edit User: "+this.dataIn.username,
      tmpData: {},
      defi:[
        {
          col: "username",
          hl: "Username",
          typ: "static",
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
      // console.log(this.dataIn);
      this.$store.state.loader = true;
      axios.put("/api/users/"+this.dataIn.username, this.dataIn).then(response => { 
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