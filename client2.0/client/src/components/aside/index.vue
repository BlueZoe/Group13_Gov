<template>
  <div>
    <!-- 菜单组件 -->
    <el-menu
      default-active="/"
      router
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
        :collapse="isCollapse"
    >

      <!-- 子菜单：异常报警 -->
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>报警</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="11" color=black @click="alarm">异常事件</el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <!-- 子菜单：可视化分析 -->
      <el-submenu index="2">
        <template slot="title">
          <i class="el-icon-menu"></i>
          <span>可视化分析</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="21">民生信息</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group>
          <el-menu-item index="22">街道事件</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group>
          <el-menu-item index="23">热点社区</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group>
          <el-menu-item index="22">结办分析</el-menu-item>
        </el-menu-item-group>
      </el-submenu>     
    </el-menu>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },

  methods: {
    alarm(){
        this.$router.push("/admin/Index");
    },

    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
  }
};
</script>

<style scoped>
</style>
