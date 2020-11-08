<template>
  <div class="dingdan">
    <ul class="cusion">
      <li v-for="v in cusion" :key="v.id" @click="curActive(v.id)">
        <router-link :to="{ path: '/order', query: { id: v.id } }" class="a">{{
          v.name
        }}</router-link>
      </li>
    </ul>
    <div class="main">
      <p>菜品</p>
      <ul>
        <li v-for="v in lists" :key="v.id">
          <img src="" alt="" width="100px" height="100px" />
          <div class="info">
            <label>口水鸭</label>
            <label>月售123|98%好评</label>
            <div class="choose">
              <a @click="reduce(v)">-</a>
              <span>{{v.count}}</span>
              <a @click="add(v)">+</a>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import qs from "qs";
import axios from "axios";
export default {
  name: "dingdan",
  data() {
    return {
      cusion: [
        { id: 0, name: "粤菜" },
        { id: 1, name: "湘菜" },
        { id: 2, name: "浙菜" },
        { id: 3, name: "川菜" },
        { id: 4, name: "鲁菜" },
        { id: 5, name: "苏菜" },
        { id: 6, name: "闽菜" },
        { id: 7, name: "徽菜" },
      ],
      lists: [
        {id:0, name:"口水鸡",count:0},
        {id:1, name:"口水鸡",count:0},
        {id:2, name:"口水鸡",count:0},
        {id:3, name:"口水鸡",count:0},
      ],
    };
  },
  methods: {
    getCusion() {
      this.$http.get("/data/cusion").then((res) => {
        console.log(res);
        this.cusion = res.data;
      });
    },
    curActive(id) {
      this.$http.get("/data/cusion" + id).then((res) => {
        this.lists = res.data;
      });
    },
    add:function(v) {
      v.count++
    },
    reduce:function (v) {
      if(v.count>0){
        v.count--
      }
    }
  },

  mounted() {
    this.getCusion();
  },
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}
.cusion {
  float: left;
}
.cusion {
  background-color: skyblue;
  height: 649px;
  width: 100px;
}
.cusion li {
  display: block;
  height: 50px;
  width: 100px;
  text-align: center;
  line-height: 50px;
  border-bottom: 1px solid gray;
}
.a {
  text-decoration: none;
  color: #000;
}
.main {
  float: left;
  margin-left: 10px;
}
.main li{
  height: 110px;
  width: 240px;
}
.main img {
  float: left;
}
.main .info {
  float: left;
  position: relative;
}
.main .info label {
  display: block;
  margin: 5px;
}
.main .info .choose {
  position: absolute;
  right: 10px;
  bottom: -40px;
}
.main .info .choose a {
  border: 1px solid black;
  height: 20px;
  width: 20px;
  display: inline-block;
  text-align: center;
  line-height: 20px;
  background-color: skyblue;
}
.main p {
  font-size: 20px;
  color: rgb(31, 94, 211);
  display: block;
  margin-bottom: 10px;
}
</style>