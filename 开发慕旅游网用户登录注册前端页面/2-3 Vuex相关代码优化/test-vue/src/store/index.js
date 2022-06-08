import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {
      username: 'zhangsan',
      nickname: '张三'
    },
    profile: {
      name: '我的详细信息'
    }
  },
  mutations: {
    updateUsername (state, payload) {
      console.log(state, payload)
      this.state.user.username = payload.uname
    },
    updateUsername2 (state, uname) {
      console.log(state, uname)
      this.state.user.username = uname
    }
  },
  actions: {
    updateUser (context, payload) {
      setTimeout(() => {
        context.commit('updateUsername2', payload.uname)
      }, 5000)
    }
  },
  modules: {
  }
})
