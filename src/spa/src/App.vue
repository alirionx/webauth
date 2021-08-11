<template>
  <div id="App">

    <router-view/>  
  </div>
</template>


<script>
export default {
  name: 'Hello',
  props: {
    msg: String
  },
  data(){
    return {
      componentTitle: "App" 
    }
  },
  methods:{
    
  },
  mounted: function(){
    this.$store.dispatch('check_app_ready')
  },
  created: function(){
    
  }
  
}
</script>

<style scoped>

</style>


