<template>
<div class="wode" id="wode">
    <h1 class="title">欢迎登录</h1>
    <div class="zhanghao">
        <input type="text" placeholder="手机号码" v-model="mobile">
        <span v-show="!mobile">手机号不能为空</span>
    </div>
    <div class="mima">
        <input type="password" placeholder="密码" v-model="password">
        <span v-show="!password">密码不能为空</span>
    </div>
    <button class="denglu" :disabled="!mobile||!password" @click="login">登录</button>
</div>
</template>


<script>
import qs from 'qs'
import axios from 'axios'
export default {
  name: "wode",
  data() {
    return {
      password:null,
      mobile:null
    };
  },
  methods: {
    login:function(){
      var data = {
        mobile:this.mobile,
        password:this.password
      }
      axios({
        method:'post',
        url:'http://127.0.0.1:3333/form_login',
        data:data
      }).then(function(res){
        console.log(res);
        if(res.data.code=='200'){
          //路由跳转
        }
        else{
          alert('用户名或密码错误')
        }
      }).catch(function(error){
        console.log(error);
      })
    }
  }
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}
* {
  margin: 0;
  padding: 0;
}
.wode {
  background-image: url(../assets/images/timg.jpg);
  background-size: cover;
  background-repeat: no-repeat;
}
.title {
  margin: 0 auto;
  padding-top: 100px;
  text-align: center;
}
.zhanghao {
  margin: 0 auto;
  margin-top: 100px;
  height: 40px;
  width: 280px;
}
.zhanghao input {
  height: 100%;
  width: 100%;
  border: 2px solid skyblue;
  font-size: 15px;
  border-radius: 10px;
  outline: none;
}
.zhanghao span {
  color: rgb(99, 106, 109);
}
.mima {
  margin: 0 auto;
  margin-top: 40px;
  height: 40px;
  width: 280px;
}
.mima input {
  height: 100%;
  width: 100%;
  border: 2px solid skyblue;
  font-size: 15px;
  border-radius: 10px;
  outline: none;
}
.mima span {
  color: rgb(99, 106, 109);
}
.denglu {
  display: block;
  margin: 0 auto;
  margin-top: 40px;
  height: 40px;
  width: 280px;
  border: 2px solid black;
  border-radius: 10px;
  outline: none;
}
.guanggao {
  width: 100%;
  height: 100%;
  position: absolute;
}
.guanggao img {
  width: 100%;
  height: 100%;
}
.guanggao span {
  display: block;
  position: absolute;
  top: 10px;
  right: 10px;
  border: 2px solid black;
  border-radius: 10px;
}
</style>