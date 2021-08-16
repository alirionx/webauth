<template>
  <div class="blocker">
    
    <div class="messageBox">
      <div class="hl">Confirm Message</div>
      <div class="msgBox">{{$store.state.confirmMsg}}</div>
      <div class="btnFrame">
        <button v-on:click="confirm">ok</button>
        <button v-on:click="callback">cancel</button>
      </div>
    </div>
  
  </div>
</template>

<script>
export default {
  name: 'ConfirmBox',
  props: {
    
  },
  methods:{
    callback(){
      this.$store.commit("unset_confirm");
    },
    confirm(){
      this.$store.state.confirmFw();
      this.$store.commit("unset_confirm");
    }
  }
}
</script>


<style scoped>

</style>