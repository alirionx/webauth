<template>
  <div class="Apps">
   <h2>Apps</h2>
  </div>
</template>

<script>
export default {
  name: 'Apps',
  props: {
    msg: String
  },
  data(){
    return {
      componentTitle: "Apps" 
    }
  },
  methods:{
    a_method(){
      console.log("Hallo Apps")
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



