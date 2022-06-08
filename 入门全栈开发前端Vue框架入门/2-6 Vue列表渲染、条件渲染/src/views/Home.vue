<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld />
    <my-component-name/>
    {{ username }}
  </div>
</template>

<script>
import Vue from 'vue'

// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

Vue.component('my-component-name', {
  template: '<h3>我的第一个局部组件</h3>'
})

export default {
  name: 'Home',
  components: {
    HelloWorld
  },
  data() {
    return {
      username: '张三'
    }
  },
}
</script>
