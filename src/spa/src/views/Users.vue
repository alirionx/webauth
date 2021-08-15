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
    </table>

  </div>
</template>

<script>
import axios from 'axios';
import ActionMenu from '../components/ActionMenu.vue'

export default {
  name: 'Users',
  props: {
    msg: String
  },
  components:{
    ActionMenu
  },
  data(){
    return {
      componentTitle: "Users",
      activeIdx: null,
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
          hl: "Email",
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
          txt: "Edit",
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
        console.log(response.data);
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
      return this.data[idx][col.grp][col.col];
    },

    set_active_menu(idx){
      this.activeIdx = idx;
    },
    reset_active_menu(idx){
      this.activeIdx = null;
    },

    call_user_edit(idx){
      console.log("Edit: " +this.data[idx].username)
    },
    call_user_set_role(idx){
      console.log("Set Role: " +this.data[idx].username)
    },
    call_user_set_access(idx){
      console.log("Set Access: " +this.data[idx].username)
    },
    call_user_delete(idx){
      console.log("Delete: " +this.data[idx].username)
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
h2{
  padding:10px;
  color: rgb(36, 57, 85);
}
</style>



