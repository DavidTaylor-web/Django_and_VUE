<template>
  <div>
    <!-- view -->
    <h1>首页</h1>
    <p>当前计数: {{ count }} </p>
    <input type="button" value="+1" @click="increment">
    <p>
      <!-- 当前登录的用户是：{{ username }} - {{ nname }} -->
      当前登录的用户是：{{ user.username }} - {{ profile.name }}
    </p>
    <p>
      <input type="text" v-model="uname">
      <input type="button" value="提交" @click="submit">
    </p>
  </div>
</template>
<script>
import { mapState, mapMutations, mapActions } from 'vuex'
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
    // ...mapMutations(['updateUsername']),
    ...mapMutations({
      update: 'updateUsername'
    }),
    // ...mapActions(['updateUser']),
    ...mapActions({
      updateUserInfo: 'updateUser'
    }),
    increment () {
      this.count++
    },
    submit () {
      // this.$store.state.user.username = 'wangwu'
      // this.$store.commit('updateUsername', {
      //   uname: this.uname
      // })
      // 使用mapMutations之后
      // this.updateUsername({uname: this.uname})
      // this.update({uname: this.uname})

      // this.$store.commit('updateUsername2', this.uname)
      // this.$store.dispatch('updateUser', {
      //   uname: this.uname
      // })
      // 使用mapActions之后
      // this.updateUser({uname: this.uname})
      this.updateUserInfo({uname: this.uname})
    }
  },
  // computed: {
  //   user () {
  //     return this.$store.state.user
  //   }
  // }
  // 传递对象
  // computed: mapState({
  //   username: state => state.user.username,
  //   nname: state => state.user.nickname
  // })
  // 传递数组 
  // computed: mapState(['user', 'profile'])
  computed: {
    conent () {
      return ''
    },
    ...mapState(['user', 'profile'])
  }
}
</script>