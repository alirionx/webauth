<template>
  <div id="App">
    <div class="headBlock">
      <img class="logo" src="@/assets/icon_access.svg" alt="" />
      <div class="hl">BCL - Useful Microservices - Authentication</div>
      <MenuBar v-if="$store.state.role" />
    </div>
    
    <div class="usrRoleBox">{{$store.state.username}} : {{$store.state.role}}</div>

    <MessageBox v-if="$store.state.systemMsg" />
    <ConfirmBox v-if="$store.state.confirmMsg" />

    <Loader v-if="$store.state.loader" />

    <router-view/>
  </div>
</template>


<script>
import MessageBox from '@/components/MessageBox.vue'
import ConfirmBox from '@/components/ConfirmBox.vue'
import Loader from '@/components/Loader.vue'
import MenuBar from '@/components/MenuBar.vue'

export default {
  name: 'App',
  components:{
    MessageBox,
    ConfirmBox,
    Loader,
    MenuBar
  },
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
   
  },
  created: function(){
    
  }
  
}
</script>

<style>
body{
  background-image: linear-gradient(#eee 10%, #ddd 100%);
  background-repeat: no-repeat;
  background-color: #ddd;
  font-family: sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  padding: 130px 0 10px 0;
  min-height:80vh;
}

.headBlock{
  position: fixed;
  left: 0px;
  top: 0px;
  width: 100%;
  min-width:800px;
  height: 110px;
  background-color: #ffffff;
  border-bottom: 1px solid #666;
  box-shadow: 0px 2px 3px #888;
  text-align: center;
  color: #000;
  z-index: 10;
}
.headBlock .logo{
  height: 90px;
  position: absolute;
  left: 30px;
  top: 18px;

}
.headBlock .hl{
  font-size: 20px;
  padding: 38px 0px 0px 52px;
  font-weight: 600;
  display:inline-block;
}

.blocker{
  position: fixed;
  top:0;
  left:0;
  width: 100%;
  height:100vh;
  padding-top: 8vh;
  background-color: rgba(0, 0, 0, 0.6);
  text-align:center;
  z-index:10;
}

.viewHl{
  display: table;
  margin: auto;
  padding: 8px;
  font-size: 18px;
  color: #444;
  text-shadow: 0px 1px #fff;
  font-weight: bold;
}



.messageBox{
  /* display: table; */
  width: 30%;
  min-width: 600px;
  margin: 12vh auto auto auto; 
  padding:18px;
  background-color: #eee;
  border: 1px solid #666 solid;
  box-shadow: 4px 8px 12px #333;
  text-align: center;
}
.messageBox .hl{
  padding:8px;
  margin-bottom: 2vh;
  background-color: #203958;
  color: #fff;
  font-size: 14px;
  font-weight: bold;
  text-align: center;
}
.messageBox .msgBox{
  padding:18px;
  margin: auto;
  background-color: #fff;
  color: #000;
  font-size: 18px;
  font-weight: normal;
  text-align: center;
  border: 1px solid #bbb;
  line-height: 26px;
}
.messageBox .btnFrame{
  text-align: center;
  padding:20px 10px 10px 10px;
}
.messageBox .btnFrame button{
  min-width:110px;
  background-color: #285894;
  color:#fff;
  text-align:center;
  font-size:16px;
  padding:5px;
  margin: auto 12px auto 12px;
  border-radius: 4px;
  border: 1px solid #000;
  cursor:pointer;
}
.messageBox .btnFrame button:hover{
  background-color: #203958;
}


.stdForm{
  display: table;
  margin: auto;
  min-width:550px;
  min-height:100px;
  text-align:left;
  padding:22px;
  border: 1px solid #444;
  /* border-radius: 12px; */
  box-shadow: 0px 8px 14px #333;
  background-color:#f5f5f5;
}
.stdForm .hl{
  padding:8px;
  margin-bottom: 2vh;
  background-color: #203958;
  color:#fff;
  text-align:center;
  font-size:14px;
  font-weight:bold;
  padding:8px;
  /* border-radius: 6px; */
  border: 1px solid rgb(2, 22, 2);
  margin:auto auto 6px auto;
}
.stdForm .spacer{
  height: 2px;
  background-color: #666;
  margin: 18px 4px 10px 4px;
}
.stdForm .iptHl{
  text-align: left;
  font-size:14px;
  font-weight:bold;
  color: #000;
  padding:10px 8px 4px 2px;
}
.stdForm input[type=text],input[type=password],input[type=email],input[type=url]{
  text-align: left;
  font-size:16px;
  color: #000;
  padding:8px;
  margin: 0px 0px 8px 2px;
  border: 0.5px solid #777;
  background-color:#fff;
  box-shadow: 0px 1px 1px #444;
  width:95%;
}
.stdForm input[type=number]{
  text-align: left;
  font-size:16px;
  color: #000;
  padding:8px;
  margin: 0px 0px 8px 2px;
  border: 0.5px solid #777;
  background-color:#fff;
  box-shadow: 0px 1px 1px #444;
  min-width:180px
}
.stdForm input[type=text]:focus,input[type=password]:focus,input[type=number]:focus,input[type=email]:focus,input[type=url]:focus{
  background-color:rgb(247, 249, 255);
}
.stdForm input[type=text][disabled]{
  background-color:#f6f6f6;
}
.stdForm select{
  text-align: left;
  font-size:16px;
  color: #000;
  padding:10px;
  margin: 0px 0px 8px 2px;
  border: 0.5px solid #777;
  background-color:#fff;
  box-shadow: 0px 1px 1px #444;
  width:98.5%;
}

.stdForm .btnFrame{
  text-align: center;
  padding:20px 0px 0px 0px;
}
.stdForm .btnFrame button{
  min-width:110px;
  background-color: #285894;
  color:#fff;
  text-align:center;
  font-size:16px;
  padding:5px;
  margin: auto 12px auto 12px;
  border-radius: 4px;
  border: 1px solid #000;
  cursor:pointer;
}
.stdForm .btnFrame button:hover{
  background-color: #203958;
}


.usrRoleBox{
  position: fixed;
  bottom: 10px;
  left: 10px;
  font-size: 12px;
  text-shadow: 0px 1px #fff;
}


.stdTable{
  margin: 20px auto 20px auto;
  padding-right: 20px;
  min-width: 1000px;
}
.stdTable th{
  background-color: #203958;
  color: #fff;
  font-size: 14px;
  font-weight: bold;
  padding:4px 6px 4px 6px;
  border: 1px solid #000;
  cursor:pointer;
}
.stdTable .sortTh{
  position:relative;
  padding-right: 30px;
}
.stdTable td{
  background-color: #fff;
  color: #000;
  font-size: 15px;
  padding:6px;
  border: 1px solid #aaa;
  white-space: nowrap;
}
.stdTable .lastline td{
  border:none;
  background: none;
  padding:14px 4px 4px 4px;
  text-align: right;
}
.stdTable button{
  background-color: #285894;
  color:#fff;
  text-align:center;
  font-size:14px;
  padding:3px 6px 3px 6px;
  margin: auto;
  border-radius: 4px;
  border: 1px solid #000;
  cursor:pointer;
}
.stdTable button:hover{
  background-color: #203958;
}

.accessCheckBox{
  padding-left:30px;
  text-align: left;
}
.accessCheckBox input[type=checkbox]{
  transform: scale(1.4);
  margin: 10px 16px auto auto;
  cursor: pointer;
}
.accessCheckBox label{
  line-height: 30px;
  font-size: 16px;
  cursor: pointer;
}

</style>


