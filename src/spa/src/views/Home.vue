<template>
  <div class="Home">
    <!-- <div class="viewHl">Your Apps</div> -->
   
   
    <div class="appsRaster">
      <div class="frame" v-for="(app, idx) in data" :key="idx" @click="create_jwt(idx)">
        <div class="box">
          <img src="@/assets/icon_app-spacer.png" :id="app.app.name" />
        </div>
        <div class="tagTxt">{{app.app.name}}</div>
      </div>
    </div>


  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Home',
  props: {
    msg: String
  },
  data(){
    return {
      componentTitle: "Home",
      data: []
    }
  },
  methods:{
    call_my_apps(){
      this.$store.state.loader = true;
      axios.get("/api/links").then(response => { 
        // console.log(response.data);
        this.data = response.data.data;
        this.build_icons();
      })
      .catch(error => {
        console.log(error);
        this.$store.state.systemMsg = error.response.data.message;
      })
      .finally(()=> { 
        this.$store.state.loader = false; 
      });
    },

    call_icon_blob(appName){
      axios.get('/api/apps/'+appName+'/icon', { responseType: 'blob' }).then(response => { 
        // console.log(response.data)
        var urlCreator = window.URL || window.webkitURL;
        var imageUrl = urlCreator.createObjectURL(response.data);
        let icoIptElm = document.getElementById(appName);
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

    build_icons(){
      for(let idx in this.data){
        this.call_icon_blob(this.data[idx].app.name);
      }
    },

    create_jwt(idx){
      // console.log(this.data[idx]);
      let appName = this.data[idx].app.name;
      axios.get('/api/jwt/'+appName).then(response => { 
        console.log(response.data);
        let auth_url = response.data.auth_url;
        let jwt = response.data.jwt;
        this.follow_bearer_to_app(auth_url, jwt);
        
      })
      .catch(error => {
        console.log(error);
        // this.$store.state.systemMsg = error.response.data.message;
        // this.callback();
      })
      .finally(()=> { 
      });
    },

    follow_bearer_to_app(auth_url, jwt){
      let followUri = auth_url+'?Bearer='+jwt+'&redirect=True'
      window.open(followUri);
      
      // const config = {
      //   withCredentials: true,
      //   headers: { 'Authorization': 'Bearer '+jwt }
      // };

      // axios.post(auth_url, {}, config
      // ).then(response => { 
      //   console.log(response.data);
      // })
      // .catch(error => {
      //   console.log(error.response);
      //   // this.$store.state.systemMsg = error.response.data.message;
      //   // this.callback();
      // })
      // .finally(()=> { 
      //   // this.$store.state.loader = false; 
        
      // });
    }

  },
  mounted: function(){
    
  },
  created: function(){
    this.call_my_apps();
  }
  
}
</script>

<style scoped>

.appsRaster{
  text-align: center;
  margin: 1%;
  min-height: 100px;
  min-width: 600px;
  /* background-color: #fff; */
}
.appsRaster .frame{
  display: inline-block;
  margin: 3.5%;
}
.appsRaster .box{  
  height: 120px;
  width: 120px;
  padding:16px;
  cursor: pointer;
  box-shadow: 0px 2px 4px #666;
  border: 0.5px solid #666;
  border-radius: 12px;
  background-color: #fff;
}
.appsRaster .box:hover{
  box-shadow: 0px 3px 6px #444;
  border: 0.5px solid #444;
}
.appsRaster .box img{
  cursor: pointer;
  width: 100%;
}
.appsRaster .tagTxt{
  margin: auto;
  padding:12px;
  font-size: 16px;
  color: #444;
  text-shadow: 0px 1px #fff;
  font-weight: bold;
}

</style>



