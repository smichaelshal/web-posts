<template>
  <div class="PagePosts">
    <div class="wel">Welcome {{ username }}</div>
    <CreatePost :token="token"/>
    <ListPosts :token="token"/>
  </div>
</template>

<script>
import CreatePost from '@/components/CreatePost.vue'
import ListPosts from '@/components/ListPosts.vue'


export default {
  name: 'PagePosts',
  components: {
    CreatePost,
    ListPosts,
  },
  props: {
    token: String,
    username: String,
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.wel{
  margin-top: 0px;
  margin-bottom: 50px;
}
</style>
