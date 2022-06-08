<template>
  <div class="hello">
    <h1>表单练习</h1>
    <p>当前的数字是： {{ count }}</p>
    <input type="button" value="点击+1" v-on:click="count+=1">
    <input type="button" value="点击+2" @click="count+=2">
    <input type="button" value="+2再乘以3" @click="calc">
    <ul>
      <li v-for="item in stuScoreList"
        :key="item.id"
        @click="addScore(item)">
        {{ item.name}} : {{item.score }}
      </li>
    </ul>
    <h3>事件冒泡</h3>
    <div class="panel" @click="clickDiv">
      <p @click.stop="clickP">点击我</p>
    </div>
    <h3>默认行为</h3>
    <a href="http://imooc.com" @click.prevent="clickDiv">点击我跳转</a>
    <h3>只触发一次</h3>
    <p @click.once="clickP">点我只触发一次</p>
    <h3>键盘事件</h3>
    <!-- <input type="text" @keyup="submit"> -->
    <input type="text" @keyup.enter="submit">
    <h3>用户登录</h3>
    <input type="text" v-model.trim="username"><br/>
    <input type="password" v-model="password"><br/>
    <!-- <input type="text" v-model.number="age"><br/> -->
    <input type="text" v-model="age"><br/>
    性别：
    <label for="">
      <input type="radio" value="男" v-model="sex">
      男生
    </label>
    <label for="">
      <input type="radio" value="女" v-model="sex">
      女生
    </label>
    <br>
    爱好：
    <!-- <select v-model="hobby" multiple>
      <option value="A">A</option>
      <option value="B">B</option>
      <option value="C">C</option>
    </select> -->

    <select v-model="hobby">
      <option :value="option"
      v-for="(option, index) in options"
      :key="index">{{ option.text }}</option>
    </select>
    <span>您选择了： {{ hobby.text}}</span>


    <input type="button" value="登录" @click="login"><br/>

  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      count: 0,
      stuScoreList: [
        {id: 1, score: 0, name: '张三'},
        {id: 2, score: 0, name: '李四'},
        {id: 3, score: 0, name: '王五'}
        ],
      // 用户名
      username: '',
      // 密码
      password: '',
      age: '',
      sex: '男',
      // 爱好
      hobby: [],
      options: [
        {text: '篮球', value: 'A'},
        {text: '足球', value: 'B'},
        {text: '棒球', value: 'C'}
      ]
    }
  },
  methods: {
    /**
     * 没有参数的点击事件
     */
    calc() {
      this.count = (this.count + 2 ) * 3
      console.log('执行完成')
    },
    /**
     * 分数+1
     */
    addScore(stu) {
      // stu.score = stu.score + 1
      stu.score += 1
      console.log(stu)
    },
    clickDiv() {
      window.alert('clickDiv')
    },
    clickP() {
      window.alert('clickP')
    },
    submit() {
      window.alert('内容变化了')
    },
    login() {
      console.log('用户名:', this.username)
      console.log('密码:', this.password)
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
