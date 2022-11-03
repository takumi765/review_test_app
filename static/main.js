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
      this.val = e.target.value;
      // csrfトークンを定義
     /*  const csrftoken = Cookies.get('csrftoken');
      fetch("", {
          method: 'post',
          headers: {
              'Content-Type':  'application/json',
              'X-CSRFToken': csrftoken,
            },
          // htmlから入力されたtaskの情報をviews.pyに送信
          body: JSON.stringify({
            subject_type: e.target.value,
            name: "bind_subject",
          }),
      })
      .then((response) => {
          return response.json();
      })
      .catch(error => {
          console.error('There has been a problem with your fetch operation:', error);
      });
      console.log('Aba'); */
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