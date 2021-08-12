<template>
  <div class="Apps">
   <div class="viewHl">Apps</div>
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



