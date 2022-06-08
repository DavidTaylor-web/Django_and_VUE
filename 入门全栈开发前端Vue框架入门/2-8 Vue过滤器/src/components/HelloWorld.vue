<template>
  <div class="hello">
    <h1>过滤器</h1>
    <p>{{ price }}</p>
    <p v-bind:data-id="price|priceFormat">{{ price|priceFormat }}</p>
    <p>{{ price|priceFormat2 }}</p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      price: 35.456
    }
  },
  methods: {
  },
  filters: {
    /**
     * 格式化价格显示-过滤器
     */
    priceFormat: function(price) {
      if (price === undefined || price === null || isNaN(price)) {
        return price
      }
      return '￥' + (price).toFixed(2)
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
.panel {
  background-color: aquamarine;
  padding: 50px;
  p {
    background-color: #fff;
    padding: 20px;
  }
}

</style>
