<template>
  <div class="Hello">
   <h2>Hello</h2>
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
      componentTitle: "Hello" 
    }
  },
  methods:{
    a_method(){
      console.log("Hallo Welt")
    }
  },
  mounted: function(){
    this.a_method();
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


