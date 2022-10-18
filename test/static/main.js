new Vue({
  el: '#app',
  data: {
    isActive: true
  },
  methods: {
    changeShow() {
      this.isActive = !this.isActive
    }
  }
})