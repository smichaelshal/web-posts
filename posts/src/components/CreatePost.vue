<template>
  <div class="CreatePost">
    <el-input
      type="textarea"
      :rows="2"
      placeholder="Enter your post"
      v-model="textarea">
    </el-input>

    <el-button class="btn" @click="sendPost">Send</el-button>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CreatePost',
  props: {
    token: String,
  },
  data(){
    return {
      textarea: '',
      responseData: '',
    }
  },
  methods:{
    sendPost(){
      this.isFirst = true
      axios.post('http://localhost:8000/api/create-post/', {
      data: this.textarea,
    })

    .then(response => (this.responseData = response.data))
    .catch(error => console.log(this.errors = error))

    },
  },

    watch: {
      responseData: function (val) {
        console.log(val)
        this.textarea = ''
      },
    },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.btn{
  margin: 15px;
}
</style>
