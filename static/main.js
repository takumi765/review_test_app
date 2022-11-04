Vue.use(window["vue-js-modal"].default);

new Vue({
  el: '#app',
  delimiters: ['[[', ']]'],
  data: {
    isActive: true,
    question: '',
    answer: '',
    val: '',
  },
  methods: {
    /* テスト画面で解答を表示させる処理 */
    changeShow: function() {
      this.isActive = !this.isActive;
    },
    detectChange: function(e) {
      this.val=e.target.value;
      console.log(e.target.value);
      var opt={
        method: 'get',
        headers: {
          'Content-Type': 'application/json',
          'subject-Type': 'ss',/* e.target.value */
        },
      };
      fetch("", opt)
      .then((response) => {
          return response.json();
      })
      .then((tasks_list) => {
          this.tasks = tasks_list;
      })
      .catch(error => {
          console.error('There has been a problem with your fetch operation:', error);
      });
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

/* モーダル画面 */
/* var myModal = document.getElementById('myModal')
var myInput = document.getElementById('myInput')

myModal.addEventListener('shown.bs.modal', function () {
  myInput.focus()
}) */