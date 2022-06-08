<template>
  <div class="page-home">
    <!-- banner图 -->
    <Banner/>
  </div>
</template>

<script>
// import { ajax } from '@/utils/ajax'
import Banner from '@/components/home/Banner'

export default {
  name: 'Home',
  components: {
    // banner图
    Banner
  },
  created () {
  }
}
</script>
<style lang="less">
.page-home {

}
</style>
