<template>
  <div class="home">
    <el-row>
      <el-col :span="3" style="color: white;">a</el-col>
      <el-col :span="18">
        <Box v-if="!isLoginVar" @is-login="IsLogin"/>
      </el-col>

      <el-col :span="18">
        <PagePosts v-if="isLoginVar" :token="token" :username="username" />
    </el-col>
  </el-row>
  
  </div>
</template>

<script>
import Box from '@/components/Box.vue'
import PagePosts from '@/components/PagePosts.vue'


export default {
  name: 'Home',
  components: {
    Box,
    PagePosts,
  },
  props: {
  },
  methods:{
    IsLogin(listProps){
      // console.log("is-login1: " + token)
      this.token = listProps[0]
      this.username = listProps[1]
      this.isLoginVar = true
      }
  },
    data(){
      return{
        isLoginVar: false,
        token: '',
        username: '',
      }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
