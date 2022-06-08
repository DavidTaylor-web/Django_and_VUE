<template>
  <div class="hello">
    <h1>我的第一个全局组件</h1>
    <ul>
      <li>
        内容 {{ name }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  // data: {
  //   'name': '组件名称'
  // }
  data() {
    return {
      'name': '组件名称'
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

</style>
