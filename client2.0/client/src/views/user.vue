<template>
     <div class="all-container">
        <div class="all-container-padding bg" >
         <el-tabs class="label_color" v-model="activeName" @tab-click="handleClick">
          <el-tab-pane  label="基本信息" name="first">
            <el-form class="user" :model="userlist" :rules="rules" ref="EditorUserForms">
                <el-form-item label="用户名"  prop="username" :label-width="formLabelWidth">
                  <el-col :span="8">  <el-input v-model="userlist.username" disabled ></el-input></el-col>
                </el-form-item>
                <el-form-item label="真实姓名" prop="real_name" :label-width="formLabelWidth">
                  <el-col :span="8">  <el-input v-model="userlist.real_name" disabled ></el-input></el-col>
                </el-form-item>
                <el-form-item label="性别" prop="gender" :label-width="formLabelWidth">
                  <el-col :span="8">  <el-input v-model="userlist.gender" disabled ></el-input></el-col>
                </el-form-item>
                <el-form-item label="电话" prop="telephone" :label-width="formLabelWidth">
                  <el-col :span="8">   <el-input v-model="userlist.telephone" placeholder="请输入电话"></el-input></el-col>
                </el-form-item>
                <el-form-item label="邮箱" prop="email" :label-width="formLabelWidth">
                  <el-col :span="8">   <el-input v-model="userlist.email" placeholder="请输入邮箱"></el-input></el-col>
                </el-form-item>
                <el-form-item label="工作部门" prop="department" :label-width="formLabelWidth">
                  <el-col :span="8">   <el-input v-model="userlist.department" placeholder="工作部门" ></el-input></el-col>
                </el-form-item>
              <el-form-item label="工作时间" prop="worktime" :label-width="formLabelWidth">
                  <el-col :span="8">   <el-input v-model="userlist.worktime" disabled ></el-input></el-col>
                </el-form-item>
            </el-form>
            <div class="grid-content bg-purple">
             <el-button type="primary"  @click="EditorUserClick('userlist')" >保存</el-button>
            </div>
          </el-tab-pane>
          <el-tab-pane label="修改密码" name="second">
            <el-form class="user" :model="ruleForm" :rules="rules" ref="ruleForm">
             <el-form-item label="原密码" prop="pass" :label-width="formLabelWidth">
                  <el-col :span="8">   <el-input v-model="ruleForm.pass" placeholder="请输入原密码" type="password"></el-input></el-col>
                </el-form-item>
                <el-form-item label="新密码" prop="newpass" :label-width="formLabelWidth">
                  <el-col :span="8"><el-input v-model="ruleForm.newpass" placeholder="请输入新密码" id="newkey" type="password"></el-input></el-col>
                </el-form-item>
                <el-form-item label="重复新密码" prop="checknewpass" :label-width="formLabelWidth">
                  <el-col :span="8">   <el-input v-model="ruleForm.checknewpass" placeholder="请再次输入新密码" id='newkey1' type="password"></el-input></el-col>
                </el-form-item>
                </el-form>
                <div class="grid-content bg-purple">
             <el-button type="primary"  @click="submitForm('ruleForm')">保存</el-button>
            </div>
          </el-tab-pane>
        </el-tabs>
        </div>
     </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
/*****检验两次密码是否一致***/
    var validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else if(value.length<8){
          callback(new Error("请输入长度大于8的密码！！"));
      }
      else {
        if (this.ruleForm.checknewpass !== "") {
          this.$refs.ruleForm.validateField("checknewpass");
        }
        callback();
      }
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次输入密码"));
      } else if (value !== this.ruleForm.newpass) {
        callback(new Error("两次输入密码不一致!"));
      } else {
        callback();
      }
    };

    return {
      ruleForm: {},//修改密码的表单
      activeName: "first",
      loading: true,
      userlist: {},//用户信息表单
      formLabelWidth: "150px",
    /***校验***/
      rules: {
        telephone: [
          {
            required: true,
            message: "请输入电话号码"
          },
          {
            pattern: /^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$/,
            message: "手机格式不对"
          }
        ],
        email: [
          {
            required: true,
            message: "请输入电子邮箱"
          },
          {
            pattern: /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/,
            message: "请输入有效的邮箱"
          }
        ],
        department:[
            {
            required: true,
            message: "请输入工作部门"
            },
            {
            pattern: /^(环保局|工商局|街道办|人事处|城管大队)$/,
            message: "没有该部门"
            }
        ],
        pass: [
          {
            //required: true,
            trigger: "blur",
            message: "请输入密码"
          },
        ],

        newpass: [
          {
            validator: validatePass,
            trigger: "blur"
          },
        ],
        checknewpass: [
          {
            validator: validatePass2,
            trigger: "blur"
          }
        ]
      },
    };
  },
  created() {
    this.getUser();
  },
  computed: {

  },
  methods: {
    //获取个人用户的信息
    getUser() {
         axios.get('http://127.0.0.1:5000/api/user_info').then(response => (this.userlist = response))
    },
    //tab切换
    handleClick(tab, event) {
      console.log(tab, event);
    },

    //修改密码
    submitForm(ruleForm) {
      var obj = {
        username: this.username,
        oldpwd: this.ruleForm.pass,
        newpwd: this.ruleForm.newpass,
        checknewpass:this.ruleForm.checknewpass,
      };
      console.log(obj);

      if(obj.newpwd === obj.checknewpass&&obj.newpwd.length>7)
      {
          let that = this;
          axios.post('http://127.0.0.1:5000/api/change_password',{oldpass:obj.oldpwd,newpass:obj.newpwd })
              .then(function (res) {
            if(res===1){
                that.$message({
                    message:"修改成功",
                    type:"success"
                })
            }else{
                that.$message({
                    message:"原密码错误",
                    type:"error"
                })
            }
        });
        this.ruleForm.pass = "";
        this.ruleForm.newpass = "";
        this.ruleForm.checknewpass = "";
      }
      /*postData("接口", obj).then(response => {
        if (response.status == 200) {
          this.$message({
            message: "保存成功",
            type: "success"
          });
        } else {
          this.$message({
            message: "修改失败" + response.message,
            type: "error"
          });
        }
      });*/
    },
    // 编辑提交的方法
    EditorUserClick() {
      this.$refs.EditorUserForms.validate(valid => {
        if (valid) {
          console.log(this.userlist);
          axios.post('http://127.0.0.1:5000/api/user_info_change',{userinfo:this.userlist})
              // .then(function (res) {
              //   console.log(res);
              // });
          this.$message(
              {
                  message:"修改成功",
                  type:"success"
              }
          )
        }
      });
    }
  }
};
</script>
<style>
    .user .el-form-item__label{
        color: #e4edf8!important;
    }
    .user{
        padding-top: 20px;
    }
    .label_color .el-tabs__item{
        color: #e4edf8!important;
    }
  .el-input.is-disabled .el-input__inner{
  color: #030913!important;
  }
  .el-tabs--top .el-tabs__item.is-top:nth-child(2) {
    padding-left: 100%!important;
  }
  .el-tabs--top .el-tabs__item.is-top:last-child {
    padding-left: 100%!important;
}
  .el-tabs__nav-wrap::after {
    position: absolute!important;
    left: 0!important;
    bottom: 0!important;
    width: 65%!important;
    height: 2px!important;
  }
  .el-tabs{
    padding-left: 30%!important;
    text-align: center!important;
  }
</style>
