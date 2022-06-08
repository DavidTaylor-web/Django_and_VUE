<template>
  <h1>详情页：{{ id }}</h1>
</template>
<script>
export default {
  data () {
    return {
      id: ''
    }
  },
  watch: {
    $route (to, from) {
      console.log('to:', to)
      console.log('from:', from)
      this.id = this.$route.params.id
    },
    id (to, from) {
      console.log('to-id:', to)
      console.log('from-id:', from)
    }
  },
  created () {
    let id = this.$route.params.id
    this.id = id
    console.log('id:', id)
    console.log('types:', this.$route.params.types)

    let name = this.$route.query.name
    console.log('name:', name)
    console.log('sort:', this.$route.query.sort)
  }
}
</script>
