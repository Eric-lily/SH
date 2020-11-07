<template>
  <div class="hello">
    <!-- 轮播 -->
    <div class="banner">
      <img
        v-for="(item, index) in list"
        :key="index"
        :src="item"
        alt=""
        v-show="n == index"
      />
      <div class="banner-circle">
        <ul>
          <li
            v-for="(item, index) in list"
            :key="index"
            :class="n == index ? 'selected' : ''"
          ></li>
        </ul>
      </div>
    </div>
    <!-- 导航 -->
    <div class="daodang">
      <div class="index-nav" v-for="(item, index) in items" :key="index" >
        <div :style="{background:item.color}">
          <img :src="item.img" alt="" />
        </div>
        <label for="">{{item.title}}</label>
      </div>
    </div>
    <!-- 列表 -->
    <div class="list">
      <div v-for="(item,index) in box " :key="index">
        <img :src="item.img" alt="">
        <span>{{item.title}}</span>
        <span>{{item.price}}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "shouye",
  data() {
    return {
      n: 0,
      list: [
        require("@/assets/images/1.jpg"),
        require("@/assets/images/2.jpg"),
        require("@/assets/images/3.jpg"),
      ],
      items:[
        {title:'购物',img:require("@/assets/icon_6zwherk9se2/gouwuche.png"),color:'rgba(209, 69, 14, 0.726)'},
        {title:'明星',img:require("@/assets/icon_6zwherk9se2/mingxing.png"),color:'rgb(12, 46, 201)'},
        {title:'宝贝',img:require("@/assets/icon_6zwherk9se2/baobei.png"),color:'rgb(11, 204, 218)'},
        {title:'搞笑',img:require("@/assets/icon_6zwherk9se2/gaoxiaoquwei.png"),color: 'rgb(247, 17, 208)'},
        {title:'摄影',img:require("@/assets/icon_6zwherk9se2/sheyinglvxing.png"),color: 'rgb(243, 228, 14)'},
        {title:'美发',img:require("@/assets/icon_6zwherk9se2/meifa.png"),color:'rgb(202, 13, 240)'},
        {title:'专辑',img:require("@/assets/icon_6zwherk9se2/zhuanji.png"),color:'rgb(228, 17, 17)'},
        {title:'店铺',img:require("@/assets/icon_6zwherk9se2/dianpu.png"),color:'rgb(202, 13, 240）'},

      ],
      box:[
        {title:'卡西欧Gshoke手表',img:require("../assets/images/wp2.jpg"),price:'￥1500'},
        {title:'卡西欧Gshoke手表',img:require("../assets/images/wp1.jpg"),price:'￥1500'},
        {title:'卡西欧Gshoke手表',img:require("../assets/images/wp3.jpg"),price:'￥1500'},
        {title:'卡西欧Gshoke手表',img:require("../assets/images/wp4.jpg"),price:'￥1500'},
        {title:'卡西欧Gshoke手表',img:require("../assets/images/wp5.jpg"),price:'￥1500'},
        {title:'卡西欧Gshoke手表',img:require("../assets/images/wp6.jpg"),price:'￥1500'},
      ]
    };
  },
  methods: {
    autoplay: function () {
      setInterval(() => {
        this.n++;
        if (this.n >= this.list.length) {
          this.n = 0;
        }
      }, 2000);
    },
  },
  mounted: function () {
    this.autoplay();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
* {
  margin: 0;
  padding: 0;
}
.banner {
  position: relative;
  left: 0;
  width: 100%;
}
.banner img {
  width: 100%;
  position: absolute;
  top: 0;
  left: 0;
}
.banner .banner-circle {
  height: 20px;
  width: 100%;
  position: absolute;
  top: 130px;
}
.banner .banner-circle ul {
  text-align: center;
}
.banner .banner-circle ul li {
  display: inline-block;
  list-style: none;
  height: 10px;
  width: 10px;
  margin: 5px;
  border-radius: 5px;
  background-color: #fff;
}
.banner .banner-circle .selected {
  background-color:skyblue;
}
.index-nav {
  float: left;
  height: 60px;
  margin-left: 10px;
}
.index-nav div {
  height: 40px;
  width: 75px;
  background-color: green;
  position: relative;
  border-radius: 20px;
}
.index-nav .gouwuche {
  background-color: rgba(209, 69, 14, 0.726);
}
.index-nav .mingxing {
  background-color: rgb(12, 46, 201);
}
.index-nav .gaoxiaoquwei {
  background-color: rgb(11, 204, 218);
}
.index-nav .meifa {
  background-color: rgb(247, 17, 208);
}
.index-nav .dianpu {
  background-color: rgb(243, 228, 14);
}
.index-nav .sheyinglvxing {
  background-color: rgb(228, 17, 17);
}
.index-nav .zhuanji {
  background-color: rgb(202, 13, 240);
}
.index-nav img {
  height: 30px;
  width: 30px;
  position: absolute;
  left: 21px;
  top: 5px;
}
.index-nav label {
  display: inline-block;
  width: 75px;
  text-align: center;
}
.daodang {
  position: relative;
  top: 180px;
}
.list div {
  height: 200px;
  width: 150px;
  background-color: skyblue;
  float: left;
  margin: 10px;
}
.list div img{
  width: 100%;
}
.list{
  position: absolute;
  top: 300px;
  height: 730px;
}
</style>
