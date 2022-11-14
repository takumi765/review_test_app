Vue.use(window["vue-js-modal"].default);

new Vue({
  el: '#app',
  delimiters: ['[[', ']]'],
  data: {
    isActive: true,
    question: '',
    answer: '',
    tests: [],
  },
  methods: {
    /* テスト画面で解答を表示させる処理 */
    changeShow: function() {
      this.isActive = !this.isActive;
    },
    detectChange: function(e) {
      this.tests = [];
      //プルダウンの値を確認する
      //console.log(e.target.value);
      
      //DjangoからのデータをJSON形式で受け取る
      var testList = JSON.parse(document.getElementById('tests_list').textContent);
      //var testList_filtered = new Array();
      //フィルタを掛けてデータを抽出する
      for(let i=0;i<testList.length;i++){
        if(e.target.value=== ''){
          this.tests.push(testList[i]);
        }else if(testList[i].subject === e.target.value){
          this.tests.push(testList[i]);
        }
      }
      //console.log(testList_filtered);
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

