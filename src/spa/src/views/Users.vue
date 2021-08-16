<template>
  <div class="Users">
   <div class="viewHl">Users</div>

    <table class="stdTable">
      <tr>
        <th v-for="(col, idx) in defi" :key="idx" :style="{textAlign: col.align}" >
            {{col.hl}}
        </th>
      </tr>
      <tr v-for="(row, idx) in data" :key="idx">
        <td v-for="(col, idx2) in defi" :key="idx2" :style="{textAlign: col.align}">
          <span v-if="col.grp">{{get_sub_val(idx,col)}}</span>
          <ActionMenu 
            v-else-if="col.col=='menu'" 
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
          <button @click="call_user_add">add</button>
        </td>
      </tr>
    </table>
    
    <UserAdd 
      v-if="activeAdd"
      v-bind:callback="reset_user_add"
      v-bind:dataIn="data" />

    <UserEdit 
      v-if="activeEdit!=null"
      v-bind:callback="reset_user_edit"
      v-bind:dataIn="data[activeEdit]" />

    <SetRole 
      v-if="activeRole!=null"
      v-bind:callback="reset_user_set_role"
      v-bind:dataIn="data[activeRole]" />
      

  </div>
</template>

<script>
import axios from 'axios';
import ActionMenu from '../components/ActionMenu.vue'
import UserAdd from '../components/UserAdd.vue'
import UserEdit from '../components/UserEdit.vue'
import SetRole from '../components/SetRole.vue'

export default {
  name: 'Users',
  props: {
    msg: String
  },
  components:{
    ActionMenu,
    UserAdd,
    UserEdit,
    SetRole,
  },
  data(){
    return {
      componentTitle: "Users",
      activeIdx: null,
      activeEdit: null,
      activeAdd: false,
      activeRole: null,
      data: [],
      defi:[
        {
          col: "id",
          hl: "Id",
          align: "center",
        },
        {
          col: "username",
          hl: "Username",
          align: "left",
        },
        {
          grp: "role",
          col: "name",
          hl: "Role",
          align: "left",
        },
        {
          col: "email",
          hl: "Email",
          align: "left",
        },
        {
          col: "company",
          hl: "Company",
          align: "left",
        },
        {
          col: "unit",
          hl: "Unit",
          align: "left",
        },
        {
          col: "phone",
          hl: "Phone",
          align: "left",
        },
        {
          col: "address",
          hl: "Address",
          align: "left",
        },
        {
          col: "zip",
          hl: "Zip Code",
          align: "center",
        },
        {
          col: "city",
          hl: "City",
          align: "left",
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
          act: this.call_user_edit
        },
        {
          txt: "Set Role",
          act: this.call_user_set_role
        },
        {
          txt: "Set Access",
          act: this.call_user_set_access
        },
        {
          txt: "Delete",
          act: this.call_user_delete
        }
      ],

    }
  },
  methods:{
    api_call_users(){
      this.$store.state.loader = true;
      axios.get("/api/users").then(response => { 
        //console.log(response.data);
        this.data = response.data.data;
        
      })
      .catch(error => {
        console.log(error);
      })
      .finally(()=> { 
        this.$store.state.loader = false; 
      });
      
    },

    get_sub_val(idx,col){
      try{
        return this.data[idx][col.grp][col.col];
      }
      catch{
        return null;
      }
      
    },

    set_active_menu(idx){
      this.activeIdx = idx;
    },
    reset_active_menu(idx){
      this.activeIdx = null;
    },

    call_user_add(){
      this.activeAdd = true;
    },
    reset_user_add(){
      this.activeAdd = false;
    },

    call_user_edit(idx){
      this.activeEdit = idx;
    },
    reset_user_edit(idx){
      this.activeEdit = null;
    },

    call_user_set_role(idx){
      this.activeRole = idx;
    },
    reset_user_set_role(idx){
      this.activeRole = null;
    },

    call_user_set_access(idx){
      console.log("Set Access: " +this.data[idx].username)
    },
    call_user_delete(idx){
      let curUserName = this.data[idx].username;
      this.$store.state.confirmMsg = "Do you really want to delete User: "+curUserName+"?";
      this.$store.state.confirmFw = ()=>{this.do_user_delete(idx)};
    },
    do_user_delete(idx){
      this.$store.state.loader = true; 
      let curUserName = this.data[idx].username;

      axios.delete("/api/users/"+curUserName).then(response => { 
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
    this.api_call_users();
  }
  
}
</script>

<style scoped>


</style>



