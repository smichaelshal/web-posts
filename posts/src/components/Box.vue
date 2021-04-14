<template>
  <div class="box">
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <el-button v-bind:type="infoRegister" style="float: left;" @click="changeMode(true)">Register</el-button>
        <el-button v-bind:type="infoLogin" style="float: right;" @click="changeMode(false)">Login</el-button>
      </div>

        <Register v-if="isRegister"/>
        <Login v-if="!isRegister" @is-login="IsLogin"/>

    </el-card>

   
  </div>
</template>

<script>
import Register from '@/components/Register.vue'
import Login from '@/components/Login.vue'


export default {
  name: 'Box',
  components: {
    Register,
    Login,
  },
  props: {
  },
  data(){
    return {
      isRegister: true,
      infoRegister: "primary",
      infoLogin: "",
    }
  },
  methods:{
    changeMode(newMode){
      this.isRegister = newMode
      let temp = this.infoRegister
      this.infoRegister = this.infoLogin
      this.infoLogin = temp
    },
    IsLogin(listProps){
      // console.log("is-login " + item)
      // this.isLoginVar = true
      this.$emit('is-login', listProps)
    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
 .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .mark{
    background: red;
  }
</style>
