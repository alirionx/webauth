<template>
  <div class="Home">
   <div class="viewHl">Home</div>
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


</style>



