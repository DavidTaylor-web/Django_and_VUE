<template>
  <div class="page-home">
    <h1>慕旅游网</h1>
    <Button type="primary">主要按钮</Button>
    <Button type="info">主要按钮</Button>
    <v-button type="info">主要按钮</v-button>
  </div>
</template>

<script>
// @ is an alias to /src
// import axios from 'axios'
import { ajax } from '@/utils/ajax'
// 引入组件
import Button from 'vant/lib/button'
// 引入组件相关的样式
import 'vant/lib/button/style'

export default {
  name: 'Home',
  components: {
    'v-button': Button,
    // Button: Button,
    Button
  },
  created () {
    // ajax.get('http://django.t.mukewang.com/api/system/slider/list/?types=11').then(resp => {
    // ajax.get('http://django.t.mukewang.com/api/accounts/user/detail/').then(resp => {
    // ajax.get('http://localhost:8080/api/system/slider/list/?types=11').then(resp => {
    // ajax.get('http://localhost:9527/hello/world/').then(resp => {
    ajax.get('http://localhost:8080/test/hello/world/').then(resp => {
      console.log('返回的结果：', resp)
    }).catch(err => {
      console.log('请求出错：', err)
    })
  }
}
</script>
<style lang="less" scoped>
.page-home {

}
</style>
