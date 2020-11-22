<template>
  <div id="home">
    <button @click="clearCookie">logout</button>
    <!-- 顶部的一个视频 -->
    <div class="video_intro">
      <!-- 背景视频 -->
      <video id="background_video" autoplay loop muted>
        <source src="../assets/animals.mp4" type="video/mp4" />
      </video>
      <div class="video_mask">
        <div class="content">
          <h2 class="title">WELCOME MONSTERS</h2>
        </div>
        <div class="state">
          <h3 class="explanation">
            It's our paradise , everyone here is monster
          </h3>
          <h3 class="explanation">Are you ready?</h3>
        </div>
      </div>
    </div>

    <!-- 剩下的静态文字介绍 -->
    <div class="container">
      <img class="arrow" src="../assets/arrows.jpg" />
      <div class="who">
        <div class="mask">
          <h3 class="head">WHO WE ARE?</h3>
          <h3 class="words">你一定很好奇我们是谁？</h3>
          <h3 class="words">
            既然你已经成功进入我们的虚拟乐园，那告诉你也无妨
          </h3>
          <h3 class="words">我们</h3>
          <h3 class="words">是来自火星的</h3>
          <h3 class="words" style="font-size: 24px; font-weight: 600">
            Monsters
          </h3>
        </div>
      </div>
      <div class="what">
        <div class="mask">
          <h3 class="head">WHAT DO WE DO?</h3>
          <h3 class="words">终极目的</h3>
          <h3 class="words">打败小巫，占领网络部</h3>
          <h3 class="words">日常工作是拍网络部工具人的精致表情包</h3>
          <h3 class="words">并通过我们Monsters相连的脑电波</h3>
          <h3 class="words">将表情包实时传入虚拟乐园</h3>
          <h3 class="words">为早日占领网络部</h3>
          <h3 class="words">期待各位Monster的加入！</h3>
        </div>
      </div>
      <div class="future">
        <div class="mask">
          <h3 class="head">FUTURE PLAN</h3>
          <h3 class="words">扩大虚拟乐园</h3>
          <h3 class="words">为小巫、一折、纬恒、志扉等老猴子</h3>
          <h3 class="words">献上表情包特辑</h3>
        </div>
      </div>
      <img class="arrow" src="../assets/arrows.jpg" />
      <div class="bar">
        <div class="author">
          <p>Designed By:</p>
          <p>Elvira And Eric</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      flag: 1,
    };
  },
  methods: {
    setCookie(username, password, day) {
      var exdate = new Date(); //获取时间
      exdate.setTime(exdate.getTime() + 24 * 60 * 60 * 1000 * day);
      //字符串拼接cookie
      window.document.cookie =
        "username" +
        "=" +
        username.value +
        ";path=/;expires=" +
        exdate.toGMTString();
      window.document.cookie =
        "password" +
        "=" +
        password.value +
        ";path=/;expires=" +
        exdate.toGMTString();
    },
    //清除cookie
    clearCookie: function () {
      this.setCookie("", "", -1); //修改2值都为空，天数为负1天就好了
      this.$router.push("/login");
    },
  },
  mounted() {
    var arr = document.cookie.split("; "); //这里显示的格式需要切割一下自己可输出看下
    for (var i = 0; i < arr.length; i++) {
      var arr2 = arr[i].split("="); //再次切割
      //判断查找相对应的值
      if (arr2[0] == "username") {
        this.flag = 0;
      }
    }
    if(this.flag == 1){
      this.$router.push('/login')
    }
  },
};
</script>

<style  scoped>
* {
  margin: 0px;
  padding: 0px;
}

html,
body {
  width: 100%;
  height: 100%;
  margin: 0;
  overflow: hidden;
}

#home {
  position: relative;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}
button {
  position: absolute;
  width: 200px;
  height: 50px;
  line-height: 50px;
  text-align: center;
  text-decoration: none;
  text-transform: uppercase;
  font-size: 24px;
  border-radius: 50px;
  color: #ffffff;
  background-image: linear-gradient(
    to right,
    #30a9f4,
    #f441a5,
    #ffeb3b,
    #09a8f4
  );
  background-size: 400%;
  z-index: 1000;
  outline: none;
}
button::before {
  content: "";
  position: absolute;
  top: -5px;
  bottom: -5px;
  right: -5px;
  left: -5px;
  border-radius: 50px;
  background-image: linear-gradient(
    to right,
    #30a9f4,
    #f441a5,
    #ffeb3b,
    #09a8f4
  );
  background-size: 400%;
  z-index: -1;
  filter: blur(20px);
}
button:hover {
  animation: sun 8s infinite;
}
button:hover::before {
  animation: sun 8s infinite;
}
@keyframes sun {
  100% {
    background-position: -400% 0;
  }
}

#background_video {
  position: absolute;
  width: 100%;
  overflow: hidden;
}

.video_mask {
  position: relative;
  z-index: 1;
  width: 100%;
  height: 720px;
  background-color: #0019212a;
}

.content {
  height: 100px;
  width: 1000px;
  text-align: center;
  margin-top: 250px;
  left: 50%;
  transform: translate(-50%, -50%);
  position: absolute;
  background-color: #00192134;
}

.content .title {
  color: white;
  font-size: 80px;
  font-weight: 600;
}

.state {
  height: 50px;
  width: 900px;
  margin-top: 330px;
  text-align: center;
  left: 50%;
  transform: translate(-50%, -50%);
  position: absolute;
}

.state .explanation {
  color: white;
  font-size: 38px;
  font-weight: 350;
  margin-top: 5px;
}

.container {
  position: relative;
  margin-top: 100px;
  display: flex;
  flex-direction: column;
}

.arrow {
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  height: 100px;
  width: 100px;
}

.mask .head {
  font-size: 40px;
  font-weight: 550;
  color: rgb(4, 180, 180);
  margin-bottom: 20px;
  font-family: Verdana, Geneva, Tahoma, sans-serif;
}
.mask .words {
  margin: 10px 0;
  font-size: 18px;
  font-weight: 500;
}

.who {
  position: relative;
  height: 240px;
  width: 600px;
  margin: 130px 0 70px 0;
  text-align: center;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.what {
  position: relative;
  height: 300px;
  width: 600px;
  margin: 60px 0 50px 0;
  text-align: center;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.future {
  position: relative;
  height: 165px;
  width: 600px;
  text-align: center;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.bar {
  height: 110px;
  width: 100%;
  background-color: black;
}

.bar .author {
  height: 50px;
  width: 200px;
  margin-top: 30px;
  margin-left: 1050px;
}

.bar .author p {
  color: white;
  font-size: 20px;
  font-weight: 400;
  margin-top: 8px;
  font-family: "Trebuchet MS", "Lucida Sans Unicode", "Lucida Grande",
    "Lucida Sans", Arial, sans-serif;
}
</style>