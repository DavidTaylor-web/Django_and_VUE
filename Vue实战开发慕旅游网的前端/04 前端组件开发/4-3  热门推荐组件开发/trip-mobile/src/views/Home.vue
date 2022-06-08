<template>
  <div class="page-home">
    <!-- banner图 -->
    <Banner/>
    <!-- 热门推荐景点 -->
    <Hot/>
  </div>
</template>

<script>
// import { ajax } from '@/utils/ajax'
import Banner from '@/components/home/Banner'
import Hot from '@/components/home/Hot'

export default {
  name: 'Home',
  components: {
    // banner图
    Banner,
    // 热门推荐景点
    Hot
  },
  created () {
  }
}
</script>
<style lang="less">
.page-home {

}
</style>
