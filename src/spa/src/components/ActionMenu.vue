<template >
  <div tag="menu" class="menuFrame">
    <div tag="menu" class="actMenuBtn" v-on:click="setActive(colId)" >
      <div tag="menu" class="dot"></div>
      <div tag="menu" class="dot"></div>
      <div tag="menu" class="dot"></div>
    </div>

    <div class="actMenuFrame" v-if="activeMenu == colId" >
      <div class="arrow"></div>
      <div class="btn" v-for="(act, idx) in menuActs" :key=idx v-on:click="act.act(colId)" >{{act.txt}}</div>
    </div>
  </div>
</template>


<script>
export default {
  name: 'ActionMenu',
  props: {
    menuActs: Array,
    activeMenu: Number,
    colId: Number,
    setActive: Function
  },
  data(){
    return{
    }
  },
  mounted(){
    
  },
  methods: {
    
  }
}
</script>

<style scoped>
.menuFrame{
  display: inline-block;
  position: relative;
}
.actMenuBtn{
  display: inline-block;
  margin: -7px auto -7px auto;
  padding:1px;
  border: 1px solid #333;
  border-radius: 3px;
  cursor: pointer;
}
.actMenuBtn .dot{
  width:12px;
  height: 4px;
  border-radius: 4px;
  margin: 2px;
  background: #333;
}
.actMenuBtn:hover{
  background-color: #333;
}
.actMenuBtn:hover .dot{
  background: rgb(255, 243, 243);
}
.actMenuFrame{
  position: absolute;
  left: 40px;
  top:-4px;
  min-width: 100px;
  *border:1px solid rgb(39, 10, 8);
  *z-index: 3;
}
.actMenuFrame .arrow{
  position: absolute;
  left:-19px;
  top:4px;
  width: 0; 
  height: 0; 
  border-top: 8px solid transparent;
  border-bottom: 8px solid transparent; 
  border-right:18px solid #333;
}
.actMenuFrame .btn{
  background-color: #444;
  border:1px solid #111;
  margin-bottom: -1px;
  color: #fff;
  text-align: left;
  font-size: 13px;
  padding: 4px 4px 4px 8px;
  border-radius: 0px;
  cursor: pointer;
}
.actMenuFrame .btn:hover{
  background-color: #024d90;
}
</style>