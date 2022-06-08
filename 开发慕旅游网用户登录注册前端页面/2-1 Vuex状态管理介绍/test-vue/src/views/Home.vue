<template>
  <div>
    <!-- view -->
    <h1>首页</h1>
    <p>当前计数: {{ count }} </p>
    <input type="button" value="+1" @click="increment">
    <p>
      当前登录的用户是：{{ user.username }}
    </p>
  </div>
</template>
<script>
export default {
  // state
  data () {
    return {
      count: 0
    }
  },
  // actions
  methods: {
    increment () {
      this.count++
    }
  },
  computed: {
    user () {
      return this.$store.state.user
    }
  }
}
</script>