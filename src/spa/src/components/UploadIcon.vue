<template>
  <div class="blocker">
    
    <div class="stdForm">
      <div class="hl">Upload Icon for App: {{dataIn.name}}</div>
      
      <div class="icoBox" @click="call_file_select">
        <img id="icoImg" src="@/assets/icon_app-spacer.png" />
      </div>
      <input type="file" id="icoInput" accept="image/png, image/jpeg, image/svg" @change="upload" />
      
      <div class="btnFrame">
        <button v-on:click="callback">ok</button>
        <button type="button" v-on:click="reset">reset</button>
      </div>

    </div>
  
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'UploadIcon',
  props: {
    dataIn: Object,
    callback: Function,
  },
  data(){
    return{
    }
  },
  methods:{
    call_file_select(){
      let icoIptElm = document.getElementById("icoInput");
      icoIptElm.click();
    },

    call_existing_icon(){
      axios.get('/api/apps/'+this.dataIn.name+'/icon', { responseType: 'blob' }).then(response => { 
        console.log(response.data)
        var urlCreator = window.URL || window.webkitURL;
        var imageUrl = urlCreator.createObjectURL(response.data);
        let icoIptElm = document.getElementById("icoImg");
        icoIptElm.src = imageUrl;
      })
      .catch(error => {
        console.log(error);
        // this.$store.state.systemMsg = error.response.data.message;
        // this.callback();
      })
      .finally(()=> { 
      });
    },

    upload(){
      // this.$store.state.loader = true; 
      let icoIptElm = document.getElementById("icoInput");
      
      const file = icoIptElm.files[0];
      const formData = new FormData();
      formData.append('file',file)

      axios.post('/api/apps/'+this.dataIn.name+'/icon', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then(response => { 
        console.log(response.data);
      })
      .catch(error => {
        console.log(error);
        // this.$store.state.systemMsg = error.response.data.message;
        // this.callback();
      })
      .finally(()=> { 
        // this.$store.state.loader = false; 
        this.call_existing_icon();
      });
    },

    reset(){
      axios.delete('/api/apps/'+this.dataIn.name+'/icon').then(response => { 
        console.log(response.data);
        let icoIptElm = document.getElementById("icoImg");
        // icoIptElm.removeAttribute('src');
        icoIptElm.src = require('../assets/icon_app-spacer.png');
      })
      .catch(error => {
        console.log(error);
        // this.$store.state.systemMsg = error.response.data.message;
        // this.callback();
      })
      .finally(()=> { 
      });
    }
    
  },
  created: function(){
    this.call_existing_icon();
  }
}
</script>


<style scoped>
.icoBox{
  padding:12px;
  min-height: 100px;
  min-width: 100px;
  display:table;
  margin: 24px auto 24px auto;
  background-color: #fff;
  text-align: center;
  border: 1px solid #bbb;
  cursor: pointer;
}
.icoBox img{
  width:200px;
  height:200px;
  cursor: pointer;
}
#icoInput{
  display:none;
}
</style>