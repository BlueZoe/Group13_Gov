<template>
  <el-container class="container">
    <!-- 头部 -->
    <el-header>
      <el-row>
        <el-col :span="12">
          <el-image style="width:250px; height: 60px" :src="url"></el-image>
        </el-col>
        <el-col class="logout" :span="12">
          <template>
            <div class="navOperater">
              <el-link type="info">退出系统</el-link>
            </div>
            
          </template>
        </el-col>
      </el-row>
    </el-header>
    <el-container>
      <!-- 侧边栏 -->
      <el-aside>
        <Aside />
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
import Aside from "@/components/aside/index.vue";

export default {
  name: "home",
  components: {
    Aside
  },
  data() {
    return {
      url: "/verify.png",
      fits: ["fill", "contain", "cover", "none", "scale-down"]
    };
  }
};
</script>
<style lang="scss" scoped>
body > .el-container {
  margin-bottom: 40px;
}
.container {
  height: 600px;
  background-color: #0c141f;
}
.el-header {
  text-align: left;
  background-color: white;
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
.el-main {
  background-color: #0c141f;
  text-align: center;
}
</style>

