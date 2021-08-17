<template>
  <div class="Apps">
   <div class="viewHl">Apps</div>

    <table class="stdTable">
      <tr>
        <th v-for="(col, idx) in defi" :key="idx" :style="{textAlign: col.align}" >
            {{col.hl}}
        </th>
      </tr>
      <tr v-for="(row, idx) in data" :key="idx">
        <td v-for="(col, idx2) in defi" :key="idx2" :style="{textAlign: col.align}">
          <ActionMenu 
            v-if="col.col=='menu'" 
            v-bind:activeMenu="activeIdx"
            v-bind:colId= "idx"
            v-bind:setActive="set_active_menu"
            v-bind:menuActs="menuActs"
            />
          <span v-else>{{row[col.col]}}</span>

        </td>
      </tr>
      <tr class="lastline">
        <td :colspan="defi.length">
          <button @click="call_app_add">add</button>
        </td>
      </tr>
    </table>
    
    <AppAdd 
      v-if="activeAdd"
      v-bind:callback="reset_app_add"
      v-bind:dataIn="data" />

    <AppEdit 
      v-if="activeEdit!=null"
      v-bind:callback="reset_app_edit"
      v-bind:dataIn="data[activeEdit]" />

    <SetAccessesApp 
      v-if="activeAccess!=null"
      v-bind:callback="reset_app_set_access"
      v-bind:dataIn="data[activeAccess]" />

    <SetJwt 
      v-if="activeJwt!=null"
      v-bind:callback="reset_app_set_jwt"
      v-bind:dataIn="data[activeJwt]" />
      

  </div>
</template>

<script>
import axios from 'axios';
import ActionMenu from '../components/ActionMenu.vue'
import AppAdd from '../components/AppAdd.vue'
import AppEdit from '../components/AppEdit.vue'
import SetAccessesApp from '../components/SetAccessesApp.vue'
import SetJwt from '../components/SetJwt.vue'

export default {
  name: 'Apps',
  props: {
    msg: String
  },
  components:{
    ActionMenu,
    AppAdd,
    AppEdit,
    SetAccessesApp,
    SetJwt,
  },
  data(){
    return {
      componentTitle: "Apps",
      activeIdx: null,
      activeEdit: null,
      activeAdd: false,
      activeAccess: null,
      activeJwt: null,
      data: [],
      defi:[
        {
          col: "id",
          hl: "Id",
          align: "center",
        },
        {
          col: "name",
          hl: "App name",
          align: "left",
        },
        {
          col: "description",
          hl: "Description",
          align: "left",
        },
        {
          col: "app_url",
          hl: "App Url",
          align: "left",
        },
        {
          col: "auth_url",
          hl: "Auth Url",
          align: "left",
        },
        {
          col: "session_key",
          hl: "Session Key",
          align: "left",
        },
        {
          col: "jwt_algorithm",
          hl: "JWT Algo",
          align: "center",
        },
        {
          col: "menu",
          hl: "Act",
          align: "center",
        },
      ],
      menuActs:[
        {
          txt: "Edit Metadata",
          act: this.call_app_edit
        },
        {
          txt: "Configure Jwt",
          act: this.call_app_set_jwt
        },
        {
          txt: "Set Access",
          act: this.call_app_set_access
        },
        {
          txt: "Delete",
          act: this.call_app_delete
        }
      ],

    }
  },
  methods:{
    api_call_apps(){
      this.$store.state.loader = true;
      axios.get("/api/apps").then(response => { 
        console.log(response.data);
        this.data = response.data.data;
      })
      .catch(error => {
        console.log(error);
        this.$store.state.systemMsg = error.response.data.message;
      })
      .finally(()=> { 
        this.$store.state.loader = false; 
      });
    },


    set_active_menu(idx){
      this.activeIdx = idx;
    },
    reset_active_menu(idx){
      this.activeIdx = null;
    },

    call_app_add(){
      this.activeAdd = true;
    },
    reset_app_add(){
      this.activeAdd = false;
    },

    call_app_edit(idx){
      this.activeEdit = idx;
    },
    reset_app_edit(idx){
      this.activeEdit = null;
    },

    call_app_set_access(idx){
      this.activeAccess = idx;
    },
    reset_app_set_access(idx){
      this.activeAccess = null;
    },

    call_app_set_jwt(idx){
      console.log("Set JWT Secret 4 "+this.data[idx].name)
      this.activeJwt = idx;

    },
    reset_app_set_jwt(){
      this.activeJwt = null;
    },


    call_app_delete(idx){
      let curAppName = this.data[idx].name;
      this.$store.state.confirmMsg = "Do you really want to delete App: "+curAppName+"?";
      this.$store.state.confirmFw = ()=>{this.do_app_delete(idx)};
    },
    do_app_delete(idx){
      this.$store.state.loader = true; 
      let curAppName = this.data[idx].name;

      axios.delete("/api/apps/"+curAppName).then(response => { 
        //console.log(response.data);
        this.data.splice(idx, 1); 
      })
      .catch(error => {
        console.log(error);
        this.$store.state.systemMsg = error.response.data.message;
      })
      .finally(()=> { 
        this.$store.state.loader = false; 
      });
    }

  },
  mounted: function(){
    var fwFunc = this.reset_active_menu;
    document.body.addEventListener("click", function(ev){
      if(ev.target.getAttribute("tag") != 'menu'){
        fwFunc();
      }
    });
  },
  created: function(){
    this.api_call_apps();
  }
  
}
</script>

<style scoped>


</style>



