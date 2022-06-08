<template>
  <div class="hello">
    <h1>我的第一个全局组件</h1>
    <p v-html="rawHtml"></p>
    <p v-text="name"></p>
    <a v-bind:href="url">点我跳转</a><br/>
    <a :href="url">点我跳转2</a>
    <h3 :class="{'text-danger': result > 0}">设置css的class</h3>
    <h3 :class="[{'text-danger': result < 0}, 'myclass']">设置css的class</h3>
    <h3 :style="{color: color}">设置css的style</h3>
    <h3 :style="[{color: color}, {border: '1px solid #f00'}]">设置css的style2</h3>
    <ul>
      <li>
        内容 {{ name }}
      </li>
      <li>{{ name.split('').reverse().join('') }}</li>
      <li>{{ result > 0 ? 'YES' : 'NO' }}</li>
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
      'name': '组件名称',
      result: -100,
      rawHtml: '<h3 style="color:#f00">你好</h3>',
      url: 'http://www.imooc.com',
      color: '#00f'
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
