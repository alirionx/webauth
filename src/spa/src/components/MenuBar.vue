<template>
  <div class="menuBar">
    <div v-for="(btn, idx) in menuList" :key="idx" >
      <div class="btn" v-if="btn.role.includes($store.state.role)"
        v-bind:class="{ underLine: btn.lnk==activeBtn, lastBtn: idx==menuList.length-1 }" 
        v-on:click="go_2_hash(btn.lnk)">{{btn.txt}}
      </div>
    </div>
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
          lnk: "#/",
          role: ["user", "admin"]
        },
        {
          txt: "Users",
          lnk: "#/users",
          role: ["admin"]
        },
        {
          txt: "Apps",
          lnk: "#/apps",
          role: ["admin"]
        },
        {
          txt: "Logout",
          lnk: this.logout,
          role: ["user", "admin"]
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
}
.menuBar .btn{
  min-width: 70px;
  padding:1px 8px 1px 8px;
  text-align: center;
  border-left: 2px solid #000;
  cursor: pointer;
}
.menuBar .btn:hover{
  text-decoration: underline;
}
.underLine{
  text-decoration: underline;
}
.lastBtn{
  border-right: 2px solid #000;
}
</style>
