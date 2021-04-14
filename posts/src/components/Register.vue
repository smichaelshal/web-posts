<template>
  <div class="register">
    <div>
      <div>
        <el-input style="width: 250px; margin: 10px;" placeholder="Enter a username" v-model="inputUsername"></el-input>
        <el-input style="width: 250px; margin: 10px;" placeholder="Enter a email" v-model="inputEmail"></el-input>
        <el-input style="width: 250px; margin: 10px;" placeholder="Enter a password" v-model="inputPassword" type="password"></el-input>
        <el-input style="width: 250px; margin: 10px;" placeholder="Enter a password agin" v-model="inputPassword2" type="password"></el-input>
      </div>

      <div>
        <el-button @click="sendRegister">Send</el-button>
      </div>
    </div>

    <div class="msg">{{msg}}</div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Register',
  props: {
  },
  data(){
    return {
      inputUsername: '',
      inputPassword: '',
      inputPassword2: '',
      inputEmail: '',
      msg: '',
      responseData: ['', 0],
      errorVar: '',
    }
  },
  methods:{
    sendRegister(){
      let _this = this
        axios.post('http://localhost:8000/api/register/', {
        username: this.inputUsername,
        email: this.inputEmail,
        password: this.inputPassword,
        password2: this.inputPassword2
      })

      .then(response => (this.responseData = [response.data, 1]))
      .catch(function (error) {
        console.log("bla " + error.response.status);
        let statusResponse = error.response.status
        if(statusResponse === 400){
          _this.errorVar = error.response.data.username

          console.log(error.response.data)
          if(_this.errorVar === undefined){
             _this.msg = "Passowrd must match."
          }else{
              _this.msg = "Username or email are busy."
          }
        }
    }); 
    },
  },
  watch: {
      responseData: function (val) {
        this.msg = 'You have successfully registered'
        console.log(val)
      },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
