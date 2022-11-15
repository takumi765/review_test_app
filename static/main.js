Vue.use(window["vue-js-modal"].default);

//DjangoからのデータをJSON形式で受け取る
const testList = JSON.parse(document.getElementById('tests_list').textContent);

new Vue({
  el: '#app',
  delimiters: ['[[', ']]'],
  data: {
    isActive: true,
    question: '',
    answer: '',
    tests: testList,
  },
  methods: {
    /* テスト画面で解答を表示させる処理 */
    changeShow: function() {
      this.isActive = !this.isActive;
    },
    /* プルダウンメニューと同期させる処理 */
    detectChange: function(e) {
      /* 初期化 */
      this.tests = [];

      //プルダウンの値を確認する
      //console.log(e.target.value);
      
      //フィルタを掛けてデータを抽出する
      for(let i=0;i<testList.length;i++){
        if(e.target.value=== '全て'){
          this.tests.push(testList[i]);
        }else if(e.target.value === testList[i].subject){
          this.tests.push(testList[i]);
        }
      }
    },
  },
  computed: {
    /* フォームバリデーション */
    check_que: function () {
      return this.question.length < 1;
    },
    check_ans: function(){
      return this.answer.length < 1;
    },
    /* 更新ボタン有効化 */
    sendable() {
      return this.question.length > 0 && this.answer.length >0
    },
  },
})

