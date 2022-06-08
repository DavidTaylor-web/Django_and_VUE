import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from './views/Home.vue'
import AboutPage from './views/About.vue'
import DetailPage from './views/Detail.vue'

// VueRouter是Vue.js的一个插件
Vue.use(VueRouter)

// 定义路由规则
const routes = [
  {path: '/home', component: HomePage, name: 'home'},
  {path: '/about', component: AboutPage},
  {path: '/d/:id/:types', component: DetailPage, name: 'detail-page'}
]

const route = new VueRouter({
  // routes: routes
  routes
})

export default route
