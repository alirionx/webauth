<template>
  <div class="blocker">
    
    <div class="messageBox">
      <div class="hl">System Message</div>
      <div class="msgBox">{{$store.state.systemMsg}}</div>
      <div class="btnFrame">
        <button v-on:click="callback">close</button>
      </div>
    </div>
  
  </div>
</template>

<script>
export default {
  name: 'MessageBox',
  props: {
    
  },
  methods:{
    callback(){
      this.$store.commit("unset_system_message");
    }
  }
}
</script>


<style scoped>

</style>