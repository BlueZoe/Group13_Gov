<template>
  <div class="message">
    <div class="text">
      <span v-show="type != 's2'">{{data['统计时间']}} ：</span>
      <el-link type="success" front-size:19px>{{data['所属街道']}}</el-link>
      <span>的</span>
      <el-link type="success">{{data['所属社区']}}</el-link>
      <span>从</span>
      <el-link type="primary">{{data['问题来源']}}</el-link>
      <span>接到</span>
      <el-link type="warning">{{data['问题类型']}}</el-link>
      <span>{{data['问题性质名称']}} </span>
      <!-- <el-link type="warning">{{}}</el-link> -->
      <span v-show="type != 's2'"> ,请</span>
      <el-link type="danger" v-show="type != 's2'">{{data['处置部门']}}</el-link>
      <span v-show="type != 's2'">尽管前往处理</span>
    </div>
   </div>
</template>

<script>
export default {
  props:{
    data:Object,
    type:{
      type:String,
      default:"s1"
    }
  }
};
</script>
<style lang="scss" scoped>
.message {
  // border-bottom: 1px solid #efefef;
  padding: 5px 0;
  margin-bottom: 5px;
  .text {
    display: flex;
    align-items: center;
  }
  span {
    color: #fff;
    font-size: 15px;
  }
}
</style>