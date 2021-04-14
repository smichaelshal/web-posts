<template>
  <div class="ListPosts">
    <!-- <div v-for="(item, index) in responseData" :key="index">{{item.data}}</div> -->

    <el-card class="box-card cards" v-for="(item, index) in responseData" :key="index">
    <!-- <div slot="header" class="clearfix">
      <span>Card name</span>
    </div> -->

    <div>{{item.data}}</div>
  </el-card>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ListPosts',
  props: {
    token: String,
  },
    data(){
    return {
      responseData: '',
      intervalid1:'',
    }
  },
    methods:{
    getListPosts(){
      this.isFirst = true
      axios.get('http://localhost:8000/api/get-list-posts/', {
      data: this.textarea,
    })

    .then(response => (this.responseData = response.data.reverse()))
    .catch(error => console.log(this.errors = error))
    },

    todo: function(){           
      this.intervalid1 = setInterval(function(){
          this.getListPosts()
      }.bind(this), 100);
    }
  },
      mounted : function(){
        this.todo()     
    },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.cards{
  margin: 50px;
}
</style>
