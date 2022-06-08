<template>
  <div class="hello">
    <h1>我的第一个全局组件</h1>
    <h3 v-if="score >= 90">A级：优秀</h3>
    <h3 v-else-if="score >= 80">B级：良好</h3>
    <h3 v-else-if="score >= 70">C级：合格</h3>
    <h3 v-else-if="score >= 60">D级：勉强</h3>
    <h3 v-else>E级：不及格</h3>
    <h3 class="text-danger" v-if="hasError">存在错误if</h3>
    <h3 class="text-danger" v-show="hasError">存在错误show</h3>
    <ul>
      <!-- <li v-for="item in areaList" :key="item">{{ item }}</li> -->
      <!-- <li v-for="item of areaList" :key="item">{{ item }}</li> -->
      <li v-for="(item, index) in areaList" :key="index">{{ item }} - {{ index }}</li>
    </ul>
    <h3>渲染对象</h3>
    <ul>
      <li v-for="(value, key, index) in userInfo" :key="index">{{index}}: {{key}} -> {{ value}}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      // 学生的分数
      score: 58,
      hasError: false,
      areaList: ['北京', '上海', '广州', '深圳'],
      userInfo: {
        username: '张三',
        nickname: '阿三',
        age: 35
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
  li {
    display: inline-block;
    margin: 0 10px;
  }
}
.text-danger {
  color: #f00;
}

</style>
