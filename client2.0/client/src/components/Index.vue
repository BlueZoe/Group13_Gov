<template>
  <div class="index">
    <div class="title">
      <span>异常事件</span>
      <span class="date">坪山区人民政府</span>
      <!-- <div class="setting" title="全局设置">
        <i class="el-icon-setting"></i>
        <span>设置</span>
      </div>-->
    </div>
    <!-- 异常事件 -->
    <section class="s1">
      <!-- 置顶 -->
      <el-row>
        <el-col :span="18" :xs="22">
          <div class="msg_list" v-if="topData.length > 0">
            <msg v-for="item in topData" :data="item" :key="item['主键'] + Math.random()*100" />
          </div>
          <el-alert v-else title="暂无置顶信息" type="info" effect="dark"></el-alert>
        </el-col>
      </el-row>
      <!-- 当日 -->
      <el-row>
        <el-col :span="18" :xs="22">
          <div class="msg_list">
            <msg :data="showData" />
          </div>
        </el-col>
      </el-row>
    </section>
    <!-- 其他消息 -->
    <section class="s3">
      <el-row>
        <el-col :span="18" :xs="22">
          <div class="table">
            <el-table
              size="mini"
              :cell-style="tableCellStyle"
              :header-cell-style="tableHeaderColor"
              :row-style="tableRowStyle"
              :data="allTableData"
              style="width: 100%"
            >
              <el-table-column prop="统计时间" label="时间" width="180"></el-table-column>             
              <el-table-column prop="所属社区" label="所属社区" width="120"></el-table-column>
              <el-table-column prop="问题来源" label="问题来源" width="100"></el-table-column>
              <el-table-column prop="小类名称" label="小类名称" width="160"></el-table-column>
              <el-table-column prop="处置部门" label="处置部门"></el-table-column>
              
              <el-table-column fixed="right" label="操作" width="160">
                <template slot-scope="scope">                  
                  <el-button 
                  @click="top(scope.row)" 
                  type="primary" 
                  size="mini"
                  >置顶</el-button>
                  <el-button @click="remove(scope.row)" type="danger" size="mini">删除</el-button>
                </template>
              </el-table-column>                      
            </el-table>

            <div class="pages">
              <el-pagination
                :page-sizes="[5,10,15,20,25]"
                :page-size="limit"
                background
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                layout="prev, sizes,pager, next"
                :total="len"
              ></el-pagination>
            </div>
          </div>
        </el-col>
      </el-row>
    </section>
    <!-- 多人投诉 -->
    <section class="s2">
      <el-row>
        <el-col :span="18" :xs="22">
          <!-- <msg v-for="item in manyData" type="s2" :key="item.data['主键']" :data="item.data" /> -->
          <el-table
            size="mini"
            :cell-style="tableCellStyle"
            :header-cell-style="tableHeaderColor"
            :row-style="tableRowStyle"
            :data="tableData"
            style="width: 100%"
          >
            <el-table-column prop="所属街道" label="街道" width="140"></el-table-column>
            <el-table-column prop="所属社区" label="社区" width="140"></el-table-column>
            <el-table-column prop="小类名称" label="小类名称" width="180"></el-table-column>
            <el-table-column prop="问题性质" label="问题性质" width="130"></el-table-column>
            <el-table-column prop="num" label="事件总数"></el-table-column>
            <el-table-column align="success">
              <template slot-scope="scope">
                <el-button
                  size="mini"
                  type="primary"
                  @click="showInfo(scope.$index, scope.row)"
                >详细信息</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div class="pages">
            <el-pagination
              :page-sizes="[5,10,15,20,25]"
              :page-size="limit2"
              background
              @size-change="handleSizeChange2"
              @current-change="handleCurrentChange2"
              layout="prev, sizes,pager, next"
              :total="len2"
            ></el-pagination>
          </div>
        </el-col>
      </el-row>
    </section>
    <!-- 弹窗 -->

    <!-- <el-row>
      <el-col :span="18" :xs="22"> -->
        <!-- <div class="msg_list" > -->
   <div class="dialg1"> 
      <el-dialog title="⚠以下社区发生紧急情况，请相关部门立刻前往处理 ：" :visible.sync="emergency" @close="emergency = false">
        <el-table :data="emergentData" >
          <el-table-column prop="所属街道" label="所属街道" width="100"></el-table-column>
          <el-table-column prop="所属社区" label="所属社区" width="100"></el-table-column>
          <el-table-column prop="小类名称" label="小类名称" width="120"></el-table-column>
          <el-table-column prop="处置部门" label="处置部门"></el-table-column>
            <!-- <el-table-column fixed="right">
              <template slot-scope="scope">            
                <el-button size="mini" type="primary" @click="removefromEmgc(scope.row)">确认</el-button>
              </template>
            </el-table-column> -->
        </el-table>           
      </el-dialog>
   </div> 

    <div class="dialg"> 
      <el-dialog title="Error" :close-on-click-modal="false" :visible.sync="toppData" > 
        <el-table-column v-model="toppData" >
          <p style="text-align:center;front-size:30px;"> 当前用户无置顶权限 </p>
        </el-table-column>
      </el-dialog>
    </div>   
    <div class="dialg2"> 
      <el-dialog title="Error" :close-on-click-modal="false" :visible.sync="rmvData" > 
        <el-table-column v-model="rmvData" >
          <p style="text-align:center;front-size:30px;"> 当前用户无删除权限 </p>
        </el-table-column>
      </el-dialog>
    </div>   
    <!-- 多人投诉消息展示 -->
    <div class="dialog">
      <el-dialog title="详细信息" :close-on-click-modal="false" :visible.sync="showAllInfo">
        <el-table size="mini" :data="showInfoData" border style="width: 100%">
          <el-table-column prop="统计时间" label="时间" width="160"></el-table-column>
          <el-table-column prop="问题来源" label="问题来源" width="100"></el-table-column>
<!--          <el-table-column prop="问题类型" label="问题类型" width="100"></el-table-column>-->
          <el-table-column prop="小类名称" label="小类名称" width="100"></el-table-column>
          <el-table-column prop="处置部门" label="处置部门"></el-table-column>
        </el-table>
      </el-dialog>
    </div>
  </div>
</template>

<script>
import msg from "@/components/message.vue";
export default {
  components: {
    msg
  },
  data() {
    return {
      nowData: [],
      nowDataLen: 0,
      showLen: 1, // 每页显示多少条
      showData: {},
      emergentData: [],
      topData: [], // 置顶数据
      removeData: [], //删除数据
      manyData: {}, // 多人投诉数据
      allTableData: [], // 10.30前数据
      tableData: [], // 表格数据
      showInfoData: [], //显示详细信息
      showAllInfo: false, // 显示控制
      toppData: false,
      rmvData: false,
      emergency: false,
      offset: 0,
      limit: 5,
      len: 0,
      offset2: 0,
      limit2: 5,
      len2: 0
    };
  },
  created() {
    this.getNowInfo();
    this.getTopData();
    this.getManyData();
    this.beforeData();
    this.getEmergency();
  },
  methods: {
    // 获取当天实时数据
    async getNowInfo() {
      const result = await this.$api.getNowInfo();
      if (result && result.code == 0) {
        this.nowData = result.data;
        this.nowDataLen = result.data.length;
        let len = localStorage.getItem("showLen") || this.showLen;
        this.showData = result.data[result.data.length - 1];
        console.log(this.showData);
        setTimeout(() => {
          this.getNowInfo();
        }, 2000);
      }
    },
    async beforeData() {
      const result = await this.$api.getBeforeData({
        offset: this.offset,
        limit: this.limit
      });
      if (result.code == 0) {
        this.len = result.data.len;
        this.allTableData = result.data.data;
      } else {
        this.$message.error(result.msg);
      }
    },
    async getTopData() {
      const result = await this.$api.getTopData();
      console.log(result)
      if (result && result.code == 0) {
        this.topData = result.data;
        console.log(this.topData)
      }
      else{
        this.$message.error(result.msg);
      }
    },
    async getManyData() {
      const result = await this.$api.getManyData({
        offset: this.offset2,
        limit: this.limit2
      });
      if (result && result.code == 0) {
        this.manyData = result.data.data;
        this.tableData = result.data.data;
        this.len2 = result.data.len;
      }
    },
    // 信息混动时间
    changeNowInfo(index) {
      // let len = localStorage.getItem("showLen") || this.showLen;
      // let start = len * index;
      // let end = start + len;
      // this.showData = this.nowData.slice(start, end);
      // if (index == 0) {
      //   this.getNowInfo();
      //   this.getTopData();
      // }
    },
    tableRowStyle({ row, index }) {
      return "background-color: #0c141f;border:none;";
    },
    // 标题设置
    tableHeaderColor({ row, column, rowIndex, columnIndex }) {
      if (rowIndex === 0) {
        return "background-color: #0c141f;color:#fff;";
      }
    },
    tableCellStyle() {
      return "border:none;color:#eee";
    },
   
    
    /**
     * 获取详细信息
     */
    async showInfo(index, data) {
      let items = data;
      this.showAllInfo = true;
      const result = await this.$api.getMonyDataInfo(items);
      if (result.code == 0) {
        this.showInfoData = result.data;
      } else {
        this.$message.error(result.msg || "系统出错");
      }
    },
    // 获取数量改变
    handleSizeChange(index) {
      console.log(index);
      this.limit = index;
      this.beforeData();
    },
    handleCurrentChange(index) {
      let offset = (index - 1) * this.limit;
      this.offset = offset;
      this.beforeData();
    },
    handleSizeChange2(index) {
      this.limit2 = index;
      this.getManyData();
    },
    handleCurrentChange2(index) {
      let offset = (index - 1) * this.limit2;
      this.offset2 = offset;
      this.getManyData();
    },
    async top(data) {
      console.log('data = ', data)
      let id = data;
      const result = await this.$api.topData(id);
      console.log('result = ', result)
      // this.toppData= true;
      if(result.code == 1)
      {
        this.toppData= true;
      }else{
        this.beforeData();
        this.getTopData();
      }
    },
    async remove(data) {
      let id = data;
      const result = await this.$api.removeData(id);
      if(result.code == 1){       
        this.rmvData = true;
      }else{
        // 这里就是刷新
        this.beforeData();
        this.getTopData();
      }
     
    },
    async getEmergency(data) {
      //let id = data["主键"];
      const result = await this.$api.getEmergency();
      if (result && result.code == 0) {
          this.emergentData = result.data;
          this.emergency = true;
          this.emergentData;
      }
      else
      {
          this.emergency=false;
      }
      setTimeout(() => {
        this.getEmergency();
     }, 2000);
    }
  },

  computed: {
    // 页数计算
    nowDataForLen() {
      let len = localStorage.getItem("showLen") || this.showLen;
      let num = Math.round(this.nowDataLen / len);
      if (this.nowDataLen / len > num) {
        return ++num;
      } else {
        return num;
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.index {
  background-color: #13182c;
  .title {
    position: relative;
    text-align: center;
    color: #fff;
    padding: 20px 20px;
    margin: 10px 10px 0px 0px;
    span {
      font-size: 28px;
      padding: 10px 0;
    }
    .setting {
      cursor: pointer;
      position: absolute;
      top: 0;
      right: 20px;
      font-size: 28px;
      display: flex;
      align-items: center;
      justify-content: center;
      span {
        font-size: 17px;
      }
    }
    .date {
      position: absolute;
      bottom: 0px;
      left: 60%;
      margin-left: 100px;
      font-size: 13px;
    }
  }
}
section {
  width: 100%;
  min-height: 100px;
  .el-row {
    display: flex;
    justify-content: center;
  }
  .el-col {
    padding: 15px;
    box-shadow: 0 2px 12px 0 rgba(255, 255, 255, 0.1);
  }
  div.table {
    div {
      background-color: #0c141f
    }
  }
}
</style>
<style lang="scss">
section .el-table--enable-row-hover .el-table__body tr:hover > td {
  background-color: #ffffff !important;
}
section .el-table--enable-row-hover .el-table__body tr:hover > td > div {
  color: #000000 !important;
}
.el-table .el-table__body tbody tr.el-table__row.hover-row {
  background-color: #0c141f !important;
}
.el-table .el-table__body tbody tr.el-table__row.hover-row > td > div {
  color: #0c141f !important;
}
.el-button--primary{
  background-color: #22444b !important;
  border-color: #235158 !important;
}
.el-button--danger{
    background-color: #9b1b1b !important;
    border-color: #4d021e !important;
}
// 0c141f
</style>