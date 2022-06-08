<template>
  <div class="page-sight-list">
    <van-nav-bar title="景点列表" left-text="返回" left-arrow @click-left="goBack" />
    <van-search v-model="sightName" show-action label="景点" placeholder="请输入搜索关键词"
      @search="onSearch">
      <template #action>
        <div @click="onSearch">搜索</div>
      </template>
    </van-search>

    <h2 v-if="pageTitle">{{ pageTitle }}</h2>
    <!-- 景点列表 -->
    <van-empty image="search" description="空空如也" v-if="dataList.length===0" />
    <div class="sight-list" v-else>
      <sight-item v-for="item in dataList" :key="item.pk" :item="item" />
      <van-pagination v-model="currentPage" :total-items="totalItems"
      :items-per-page="perPage" @change="pageChange"/>
    </div>
    <!-- //景点列表 -->
  </div>
</template>
<script>
import SightItem from '@/components/common/ListSight'
import { SightApis } from '@/utils/apis'
import { ajax } from '@/utils/ajax'
export default {
  components: {
    SightItem
  },
  data() {
    return {
      // 页面标题
      pageTitle: '',
      // 按景点名称搜索
      sightName: '',
      // 总记录数
      totalItems: 0,
      dataList: [],
      // 分页处理
      currentPage: 1,
      perPage: 5
    }
  },
  methods: {
     goBack () {
      this.$router.go(-1)
    },
    /**
     * 搜索事件
     */
    onSearch() {
      console.log('开始搜索')
      if (!this.sightName) {
        this.$toast('请输入搜索词')
        return
      }
      // 重置数据
      this.currentPage = 1
      this.dataList = []
      // 触发搜索
      this.getDataList()
    },
    getDataList() {
      ajax.get(SightApis.sightListUrl, {
        params: {
          page: this.currentPage,
          limit: this.perPage,
          name: this.sightName
        }
      }).then(({ data: { meta, objects } }) => {
        console.log('fine list:', objects)
        this.dataList = objects
        // 总记录数
        this.totalItems = meta.total_count
      })
    },
    /**
     * 页码发生变化后调用
     */
    pageChange () {
      this.getDataList()
    }
  },
  mounted() {
    this.pageTitle = this.$route.query.title
    this.getDataList()
  }
}
</script>
<style lang="less">
.page-sight-list {
  h2 {
    font-size: 14px;
    padding: 10px 10px 0;
    text-align: left;
  }
  .sight-list {
    margin-top: 10px;
    padding: 10px 10px 5px;
    background-color: #fff;
  }
  .van-pagination {
    background-color: #fff;
    margin-top: 10px;
  }
}
</style>
