<template>
  <div class="login_wrap">
    <div class="welcome">欢迎登录坪山区大数据分析平台</div>
    <div class="from">
      <h2 class="title"></h2>
      <el-form class="xxxx" ref="form" :rules="rules" size="small" :model="form" label-width="100px">
        <el-form-item label="账号" prop="username">
          <el-input class="shishi" v-model="form.username"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input show-password v-model="form.password"></el-input>
        </el-form-item>
        <!-- <el-form-item label="验证码" prop="verifycode">
          <el-input v-model="form.verifycode"></el-input>
          <el-image style="width: 140px; height: 34px" :src="url"></el-image>
        </el-form-item> -->
        <el-form-item label="验证码" prop="verifycode">
          <el-input v-model="form.verifycode"></el-input>
        </el-form-item>
        <el-form-item>
          <div id="identifybox">
            <vue-img-verify @getImgCode="getImgCode" ref="vueImgVerify" />
          </div>
        </el-form-item>

        <el-form-item>
          <el-button
            type="primary"
            size="small"
            @click="submitForm('form')"
            :loading="islogin"
          >{{islogin ? "登录中" : ' 登录 '}}</el-button>
          <el-button type="primary" size="small" @click="resetForm('form')"> 重置 </el-button>
        </el-form-item>
      </el-form>
      <div class="bg">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>
  </div>
</template>

<script>
import vueImgVerify from '@/components/vue-img-verify'
export default {
  data() {
    const validateVerifycode = (rule, value, callback) => {
      if (this.imgCode.toLowerCase() !== value.toLowerCase()) {
        console.log('validateVerifycode:',value)
        callback(new Error('请输入正确的验证码'))
      } else {
        callback()
      }
    }
    return {
      form: {
        username: "",
        password: "",
        verifycode: ''
      },
      islogin: false,
      rules: {
        username: [
          { required: true, message: "请输入用户名", trigger: "blur" }
        ],
        password: [{ required: true, message: "请输入密码", trigger: "blur" }],
          verifycode: [
          { required: true, message: '请输入验证码', trigger: 'blur' },
          // { validator: validateVerifycode, trigger: 'blur' }
        ]
      },
      imgCode:''
    };
  },

  methods: {
    randomNum(min, max) {
      return parseInt(Math.random() * (max - min) + min)
    },
    // refreshCode() {
    //   this.identifyCode = ''
    //   this.makeCode(this.identifyCodes, 4)
    // },
/*    makeCode(o, l) {
      for (let i = 0; i < l; i++) {
        this.getImgCode += this.identifyCodes[
          this.randomNum(0, this.identifyCodes.length)
        ]
      }
    },*/
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
            // 校验验证码
            if (this.imgCode.toLowerCase() !== this.form.verifycode.toLowerCase()) {
                this.$message.error("验证码输入有误！");
                this.$refs.vueImgVerify.handleDraw()
                return
            }
          this.login();
        } else {
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    async login() {
      this.islogin = true;
      const result = await this.$api.login(this.form);
      this.islogin = false;
      if (result && result.code == 0) {
        //   登录成功
        localStorage.setItem("login", true);
        localStorage.setItem("token", result.data.token);
        this.$router.push({ name: "newhome" });
      } else {
        this.$message.error(result.msg || "请求错误");
      }
    },
    // 点击图片获取验证码
    getImgCode(code) {
      this.imgCode = code
      console.log('验证码: ' + this.imgCode)
    }

  },
  components:{
    vueImgVerify
  }
}
</script>

<style lang="scss" >

.identifybox{
  display: flex;
  justify-content:space-between;
  margin-top: 7px;
}
.login_wrap {
  width: 100vw;
  height: 100vh;
  background-color: #6e7070fa;
  background-image: url(../assets/bg1.png);// 此处为登录页面背景图
  background-size: cover;
  background-repeat: no-repeat;
  color: #fff;
  .welcome{
    padding-top: 4%;
    padding-right: 5%;
    font-size: 30px;
    font-family: "华文行楷";
  }
}
.el-form-item__label{
  color:#e4edf8!important;
}
.xxxx .el-form-item__label {
    color: #e4edf8;
}
.from {
  //background-color: #d9dadb;
  background-color:transparent;
  padding: 20px 30px 0px 0px;
  width: 340px;
  border: 0px solid rgb(159, 190, 211);
  border-radius: 6px;
  position: fixed;
  top: 15%;
  left: 45%;
  transform: translate(-50%);
  .title {
    color: rgb(213, 254, 242);
    font-size: 18px;
    text-align: center;
    padding: 0px 0px 20px 40px;
  }

  .el-button--primary{
    background-color: #235158;
    border-color: #020536;
    width: 80px;
  }
  /*.shishi .el-in*/
  .el-button--text{
    background-color: #89d6c8;
    border-color: #89d6c8;
    width: 80px;
  }
  .bg {
    z-index: -1;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    // span {
    // }
  }
}
</style>
