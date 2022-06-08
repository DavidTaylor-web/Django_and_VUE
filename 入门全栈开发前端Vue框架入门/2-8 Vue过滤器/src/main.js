import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

// 全局注册了一个过滤器
Vue.filter('priceFormat2', function(price) {
  if (price === undefined || price === null || isNaN(price)) {
    return price
  }
  return '￥' + (price).toFixed(2)
})

window.app = new Vue({
  // el: '#app',
  router,
  store,
  render: h => h(App),
}).$mount('#app')