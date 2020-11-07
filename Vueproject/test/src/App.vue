<template>
  <div id="app">
    <!-- 上面展示 -->
    <router-view />
    <!-- 底部导航 -->
    <div class="nav-bottom">
      <router-link to="/">
        <a href="">
          <img src="@/assets/icon_6zwherk9se2/shouye.png" alt="">
          <label for="">首页</label>
        </a>
      </router-link>
      <router-link to="/dingdan">
        <a href="">
         <img src="@/assets/icon_6zwherk9se2/wodedingdan.png" alt=""> <i></i>
          <label for="">订单</label>
        </a>
      </router-link>
      <router-link to="/wode">
        <a href="">
          <img src="@/assets/icon_6zwherk9se2/wodejuhuasuan.png" alt="">
          <label for="">我的</label>
        </a>
      </router-link>
      <router-link to="/faxian">
        <a href="">
          <img src="@/assets/icon_6zwherk9se2/yanjing.png" alt="">
          <label for="">发现</label>
        </a>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
@import './assets/style.css';
#app .nav-bottom .active{
  color: yellow;
}
</style>
