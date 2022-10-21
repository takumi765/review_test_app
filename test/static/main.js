Vue.use(window["vue-js-modal"].default);

new Vue({
  el: '#app',
  data: {
    isActive: true
  },
  methods: {
    /* テスト画面で解答を表示させる処理 */
    changeShow: function() {
      this.isActive = !this.isActive
    },
    
    /* 登録したテストでポップアップを表示する処理 */
    show : function() {
      this.$modal.show('hello-world');
    },
    hide : function () {
      this.$modal.hide('hello-world');
    },
  }
})
