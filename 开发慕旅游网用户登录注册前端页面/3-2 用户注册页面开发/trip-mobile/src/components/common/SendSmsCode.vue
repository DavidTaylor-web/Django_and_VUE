<template>
  <!-- 短信验证码发送相关的逻辑 -->
  <van-button
    size="small"
    type="primary"
    @click.prevent="sendSmsCode()"
    :disabled="isSmsSend"
    >{{ sendBtnText }}</van-button>
</template>
<script>
export default {
  props: ['phoneNum'],
  data () {
    return {
      // 是否已经发送了验证码
      isSmsSend: false,
      sendBtnText: '点击发送验证码',
      timer: null,
      counter: 60
    }
  },
  methods: {
    reset () {
      this.isSmsSend = false
      this.sendBtnText = '点击发送验证码'
      if (this.timer) {
        clearInterval(this.timer)
        this.counter = 60
        this.timer = null
      }
    },
    /**
     * 倒计时
     */
    countDown () {
      this.timer = setInterval(() => {
        this.sendBtnText = `(${this.counter}秒)后重新发送`
        this.counter--
        if (this.counter < 0) {
          this.reset()
        }
      }, 1000)
    },
    /**
     * 发送验证码
     */
    sendSmsCode () {
      // 判断手机号是否已经输入
      if (!this.phoneNum) {
        this.$notify('请输入手机号')
        return false
      }
      // TODO 调用接口，发送短信验证码
      this.isSmsSend = true
      // 开启倒计时, 60s之后才能再次点击
      this.countDown()
    }
  }
}
</script>
