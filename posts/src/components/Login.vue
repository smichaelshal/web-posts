<template>
  <div class="login">
    <el-input style="width: 250px; margin: 10px;" placeholder="Enter a username" v-model="inputUsername"></el-input>
    <el-input style="width: 250px; margin: 10px;" placeholder="Enter a password" v-model="inputPassword" type="password"></el-input>
    <el-button @click="sendLogin">Send</el-button>

    <div class="msg">{{msg}}</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Login',
  props: {
  },
  data(){
    return {
      inputUsername: '',
      inputPassword: '',
      responseData: '',
      errors: '',
      token: '',
      msg: ''
    }
  },
  methods:{
    sendLogin(){
      this.isFirst = true
      axios.post('http://localhost:8000/api/login/', {
      username: this.inputUsername,
      password: this.inputPassword
    })

    .then(response => (this.responseData = response.data))
    .catch(error => console.log(this.errors = error))

    },
  },
  watch: {
      responseData: function (val) {
      this.token = val.token
      this.$emit('is-login', [val.token, this.inputUsername])
      },
      errors: function (val) {
       console.log(val)
       this.msg = "The username or password is incorrect"
      },
      },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
