<template>
  <div class="Home">
   <h2>Home</h2>
  </div>
</template>

<script>
export default {
  name: 'Home',
  props: {
    msg: String
  },
  data(){
    return {
      componentTitle: "Home" 
    }
  },
  methods:{
    a_method(){
      console.log("Hallo Home")
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



