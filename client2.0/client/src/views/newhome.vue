<template>
  <el-container class="container">
    <!-- 头部 -->
    <el-header>
      <el-row>
        <el-col :span="8">
          <el-image style="width:200px; height: 60px;" :src=url></el-image>
        </el-col>
        <el-col :span="15"><strong><font size="6" color="#f0f8ff" face="楷体">{{message}}</font></strong></el-col>
        <el-col class="logout" :span="1">
          <template>
            <div class="navOperater">
              <el-link type="info" @click="logout"><strong>退出系统</strong></el-link>
            </div>
          </template>
        </el-col>
      </el-row>
    </el-header>
    <el-container>
      <!-- 侧边栏 -->
      <el-aside width="200px">
        <template>

    <!-- 菜单组件 -->
    <el-menu

      :default-active="$route.path"
      :unique-opened="false"
      :default-openeds="['1','2','3']"
      router
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
    >
<!--:collapse="isCollapse"-->

      <!-- 子菜单：异常报警 -->
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-warning"></i>
            <span><strong><font  color="#f0f8ff" >报警</font>></strong></span>
        </template>
        <el-menu-item-group>
          <el-menu-item @click="alarm" color=black >异常事件</el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <!-- 子菜单：可视化分析 -->
      <el-submenu index="2">
        <template slot="title">
          <i class="el-icon-menu"></i>
            <span><strong><font  color="#f0f8ff" >可视化分析</font></strong></span>
        </template>
        <el-menu-item-group>
<!--          <el-menu-item  @click="on1" >民生信息</el-menu-item>-->
          <el-menu-item @click="on1">民生信息</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group>
          <el-menu-item  @click="on2">街道事件</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group>
          <el-menu-item @click="on3" >热点社区</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group>
          <el-menu-item @click="on4">结办分析</el-menu-item>
        </el-menu-item-group>
      </el-submenu>
       <el-submenu index="3">
        <template slot="title">
          <i class="el-icon-setting"></i>
            <span><strong><font  color="#f0f8ff" >设置</font></strong></span>
        </template>
          <el-menu-item-group>
          <el-menu-item @click="onuser" color=black >用户设置</el-menu-item>
        </el-menu-item-group>
      </el-submenu>
    </el-menu>


</template>
      </el-aside>
      <!-- 内容区 -->
      <el-main>
        <template>
         <router-view></router-view>
        </template>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
// 导入组件
import axios from 'axios';
import Aside from "@/components/aside/index.vue";
export default {
  name: "home",
  components: {
  },
    data: function () {
        return {
            url: require('@/assets/hitlogo.jpg'),
            fits: ["fill", "contain", "cover", "none", "scale-down"],
            message:""
        };
    },
    created(){
      this.welcome() ;
    },
    methods: {
    alarm(){
        this.$router.push("Index");
    },
    welcome(){
        axios.get('http://127.0.0.1:5000/api/title').then(response => (this.message = response))
    },

    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
         logout(){//退出功能
            //弹出确认对话框
            //用户点击确认，跳回用户登录页面，清除token
                this.$confirm('确定要退出登录吗?', '提示', {
                   confirmButtonText: '确定',
                   cancelButtonText: '取消',
                   type: 'warning'
                  }).then(() => {

                    axios.get('http://127.0.0.1:5000/api/login')
                         .then(function(res){})
            //console.log(datalist)
                    //websocket
                    // this.$message({
                    //    type: 'success',
                    //    message: '退出成功!'
                    //  });
                     //确认退出，清除token
                     localStorage.removeItem('token')
                     //跳转登录页面(编程式导航)
                     this.$router.push('/')

                }).catch(() => {
              this.$message({
               type: 'info',
               message: '已取消退出'});
                });
         },


      on1(){
        this.$router.push("chart1")
      },
      on2(){
        this.$router.push("chart2")
      },
      on3(){
        this.$router.push("chart3bmap")
      },
        on4(){
        this.$router.push("chart4")
      },
        onuser(){
        this.$router.push("user")
      }
  }
};
</script>
<style lang="scss" scoped>
body > .el-container {
  margin-bottom: 40px;
}
.container {
  height: 800px;
  background-color: #13182c;
 /*? background-image: url(../assets/bg1.jpg);*/
   background-size: cover;
    background-repeat: no-repeat;
}
.el-header {
  padding: 0;
  text-align: left;
  /*background-color: #ffffff;*/
  .logout {
    text-align: right;
    .navOperater {
      width: 80px;
      height: 80px;
      float: right;
      line-height: 50px;
    }
  }
}
.el-menu,.el-menu-item-group{
    background-color: #13182c;
}
.el-main {
  /*background-color: #0c141f;*/
    padding: 0;
  text-align: center;
}
.el-menu-item{
    color:#e4edf8;
}
</style>

