const App = {
  data() {
      return {
          task: {title: ''},
          tasks: [],
      }
  },
  /* 通常、Vue は{{}}を使って、データを表示するのですが
  今回 django で{{}}を使ってしまっているので、Vue のデータは[[]]を使って表示します。 */
  compilerOptions: {
      delimiters: ['[[', ']]'],
  },
  //methods は、Vue で使用するメソッドを書く部分です。
  methods: {
      getTasks(){
          fetch(URL, {//取得したい情報を提供している url を書き、
              method: 'get',
              headers: {
                  'Content-Type':  'application/json',
              },
          })
          .then((response) => {//返ってきたレスポンスを 何形式で受け取るか指定し、
              return response.json();
          })
          .then((tasks_list) => {//レスポンスのデータの処理方法を定義します。
              this.tasks = tasks_list;
          })
          .catch(error => {
              console.error('There has been a problem with your fetch operation:', error);
          });
      },
      createTask(){
          // csrfトークンを定義
          const csrftoken = Cookies.get('csrftoken');
          // taskリストを取得する
          this.getTasks();
          fetch(URL, {
              method: 'post',
              headers: {
                  'Content-Type':  'application/json',
                  'X-CSRFToken': csrftoken,
              },
              // htmlから入力されたtaskの情報をviews.pyに送信
              body:JSON.stringify(this.task),
          })
          .then((response) => {
              return response.json();
          })
          .then((task) => {
              console.log(task)
              // タイトルを空にする
              this.task.title = ''
              this.getTasks();
          })
          .catch(error => {
              console.error('There has been a problem with your fetch operation:', error);
          });
      },
  },
  
  //created()には Vue のオブジェクトが起動したときに実行される処理を書きます。
  created() {
      this.getTasks();
  },
}


/* Vue.createApp(App).mount('#app')で、html の id=app の要素に、
この Vue のオブジェクトが作られるようになります。 */
Vue.createApp(App).mount('#app');