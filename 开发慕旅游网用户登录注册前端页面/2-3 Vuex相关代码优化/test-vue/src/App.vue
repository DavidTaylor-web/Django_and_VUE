<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <router-link to="/home">首页</router-link> | 
    <router-link to="/about">关于</router-link>|
    <router-link to="/d/123/type1">详情1</router-link>|
    <router-link :to='"/d/" + id + "/" + types'>详情2</router-link>|
    <router-link :to='{path: "/d/" + id + "/" + types, query: {name: "abc", sort: "desc"}}'>详情3</router-link>|
    <router-link :to='{name: "detail-page", params: {id: "abc123", types: "type3"}, query: {name: "abc", sort: "desc"}}'>详情4</router-link>|
    <a href="javascript:;" @click="goHome">点我跳转</a>
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <!-- 路由变化之后，在这里显示组件的内容 -->
    <router-view></router-view>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  data () {
    return {
      id: 456,
      types: 'type2'
    }
  },
  methods: {
    goHome () {
      // this.$router.push({name: 'home'})
      // this.$router.push({name: "detail-page", params: {id: "abc123", types: "type3"}, query: {name: "abc", sort: "desc"}})
      // this.$router.go(-1)
      this.$router.replace({name: 'home'})
    }
  },
  components: {
    // HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
