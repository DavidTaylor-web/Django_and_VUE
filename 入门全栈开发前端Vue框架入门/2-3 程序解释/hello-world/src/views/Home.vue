<template>
  <div class="home">
    <h3>表单操作</h3>
    <input type="text" name="username" v-model="username">
    <input type="button" value="提交" @click="submit">
    <p>{{ uname }}</p>

    <h3>动态列表</h3>
    <input type="button" value="加载" @click="load">
    <ul>
      <li v-for="item in dataList" :key="item">{{ item }}</li>
    </ul>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
// import HelloWorld from '../components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    // HelloWorld
  },
  data() {
    return {
      username: 'admin',
      dataList: []
    }
  },
  computed: {
    uname () {
      return this.username[0] + "***"
    } 
  },
  methods: {
    submit() {
      console.log('获取表单的值:', this.username)
      this.load()
    },
    load() {
      this.dataList = ['北京', '上海', '广州', '深圳']
    }
  }
}
</script>
