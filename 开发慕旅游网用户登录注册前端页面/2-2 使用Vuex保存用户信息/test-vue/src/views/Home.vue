<template>
  <div>
    <!-- view -->
    <h1>首页</h1>
    <p>当前计数: {{ count }} </p>
    <input type="button" value="+1" @click="increment">
    <p>
      当前登录的用户是：{{ user.username }}
    </p>
    <p>
      <input type="text" v-model="uname">
      <input type="button" value="提交" @click="submit">
    </p>
  </div>
</template>
<script>
export default {
  // state
  data () {
    return {
      count: 0,
      uname: ''
    }
  },
  // actions
  methods: {
    increment () {
      this.count++
    },
    submit () {
      // this.$store.state.user.username = 'wangwu'
      // this.$store.commit('updateUsername', {
      //   uname: this.uname
      // })
      // this.$store.commit('updateUsername2', this.uname)
      this.$store.dispatch('updateUser', {
        uname: this.uname
      })
    }
  },
  computed: {
    user () {
      return this.$store.state.user
    }
  }
}
</script>