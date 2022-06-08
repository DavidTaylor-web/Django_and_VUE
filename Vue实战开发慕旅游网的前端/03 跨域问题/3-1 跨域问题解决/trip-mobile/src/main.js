import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import * as filters from './utils/filters'

Vue.config.productionTip = false

// 注册过滤器
Object.keys(filters).forEach(k => Vue.filter(k, filters[k]))

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
