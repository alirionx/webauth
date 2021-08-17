<template>
  <div class="menuBar">
    <div 
      v-for="(btn, idx) in menuList" :key="idx"
      v-bind:class="{ underLine: btn.lnk==activeBtn }"
      v-on:click="go_2_hash(btn.lnk)">{{btn.txt}}</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'MenuBar',
  props: {
    msg: String
  },
  data(){
    return{
      activeBtn: null,
      menuList: [
        {
          txt: "Home",
          lnk: "#/"
        },
        {
          txt: "Users",
          lnk: "#/users"
        },
        {
          txt: "Apps",
          lnk: "#/apps"
        },
        {
          txt: "Logout",
          lnk: this.logout
        }
      ]
    }
  },
  methods:{
    go_2_hash(lnk){
      if(typeof lnk == "function"){
        lnk();
      }
      else{
        this.activeBtn = lnk
        location.hash=lnk;
      }    
    },

    logout(){
      axios.delete("/api/user/auth").then(response => { 
        console.log(response.data);
        this.$store.commit('unset_username');
        this.$store.commit('unset_role');
        location.hash = "#/login"
      })
      .catch(error => {
        console.log(error);
        this.$store.commit("set_system_message", "Logout Failed!");
      });
    }

  },
  mounted: function(){
    this.activeBtn = location.hash;
  }
}
</script>


<style scoped>
.menuBar{
  position: absolute;
  right: 14px;
  bottom:6px;
  font-size: 14px;
  font-weight: bold;
  color:#000;
  white-space: nowrap;
}
.menuBar div{
  display: inline-block;
  min-width: 70px;
  padding:1px 8px 1px 8px;
  text-align: center;
  border-left: 2px solid #000;
  cursor: pointer;
}
.menuBar div:last-child{
  border-right: 2px solid #000;
}
.menuBar div:hover{
  text-decoration: underline;
}
.underLine{
  text-decoration: underline;
}
</style>
