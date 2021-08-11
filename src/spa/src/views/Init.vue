<template>
  <div class="Init">
   <h2>Init: {{$store.state.appReady}}</h2>
  </div>
</template>

<script>
export default {
  name: 'Init',
  props: {
    msg: String
  },
  data(){
    return {
      componentTitle: "Init" 
    }
  },
  methods:{
    a_method(){
      console.log("Hallo Init")
    }
  },
  mounted: function(){
    
  },
  created: function(){
    this.a_method();
  }
  
}
</script>

<style scoped>
h2{
  padding:10px;
  color: rgb(36, 57, 85);
}
</style>



