<template>
  <div class="page-home">
    <!-- banner图 -->
    <Banner/>
    <!-- 热门推荐景点 -->
    <Hot/>
    <!-- 精选景点 -->
    <Fine/>
  </div>
</template>

<script>
// import { ajax } from '@/utils/ajax'
import Banner from '@/components/home/Banner'
import Hot from '@/components/home/Hot'
import Fine from '@/components/home/Fine'

export default {
  name: 'Home',
  components: {
    // banner图
    Banner,
    // 热门推荐景点
    Hot,
    // 精选景点
    Fine
  },
  created () {
  }
}
</script>
<style lang="less">
.page-home {

}
</style>
