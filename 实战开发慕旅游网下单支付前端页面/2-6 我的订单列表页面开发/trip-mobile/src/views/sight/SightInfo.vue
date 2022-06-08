<template>
  <!-- 景点介绍 -->
  <div class="page-sight-info">
    <van-nav-bar title="景点介绍" left-text="返回" left-arrow @click-left="goBack" />
    <van-panel title="入园参考">
      <div v-html="sightInfo.entry_explain">
      </div>
    </van-panel>
    <van-panel title="特色玩法">
      <div v-html="sightInfo.play_way"></div>
    </van-panel>
    <van-panel title="温馨提示">
      <div v-html="sightInfo.tips"></div>
    </van-panel>
    <van-panel title="交通和到达">
      <div v-html="sightInfo.traffic"></div>
    </van-panel>
  </div>
</template>
<script>
import { SightApis } from '@/utils/apis'
import { ajax } from '@/utils/ajax'
export default {
  components: {},
  data() {
    return {
      // 景点ID
      id: 1,
      // 景点信息
      sightInfo: {}
    }
  },
  methods: {
    goBack () {
      this.$router.go(-1)
    },
    /**
     * 景点详情
     */
    getSigthInfo() {
      const url = SightApis.sightInfonUrl.replace('#{id}', this.id)
      ajax.get(url).then(({ data }) => {
        this.sightInfo = data
      })
    },
    loadData() {
      // 从URL获取景点ID
      this.id = this.$route.params.id
      // 加载景点详情
      this.getSigthInfo()
    }
  },
  watch: {
    /**
     * 检测路由变化时重新加载数据
     */
    $route() {
      this.loadData()
    }
  },
  mounted() {
    this.loadData()
  }
}
</script>
<style lang="less">
.page-sight-info {
  .van-panel {
    margin-top: 10px;
    text-align: left;

    h4 {
      padding: 10px 0;
      font-size: 13px;
    }
    p {
      font-size: 13px;
      color: #444;
      line-height: 2;
      text-align: left;
    }
    img {
      max-width: 100%;
      height: auto;
    }
  }
  .van-panel__header {
    padding-left: 10px;
  }
  .van-cell__title {
    text-align: left;
    padding-left: 5px;
    border-left: 5px solid #1989fa;
  }
  .van-panel__content {
    padding: 10px;
  }
}
</style>
