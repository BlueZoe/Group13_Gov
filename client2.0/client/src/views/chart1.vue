<template>
  <div class="total">
      <div class="charts">
        <br><br>
        <div id="chart1" :style="{width:'1170px',height:'450px'}"></div>
      </div>
    <div class="select-box" :style="{width:'1170px',height:'100px'}">

    <span><br><br>时间范围选择: &#12288</span>
    <span >
      <span class="item" >
        <select v-model="formData1.year1">
          <option v-for="item in year1" :value="item">{{item}}年</option>
        </select>
      </span>
      <span class="item" @change="getDay1">
        <select  v-model="formData1.month1">
          <option v-for="item in month1" :value="item">{{item}}月</option>
        </select>
      </span>
      <span class="item">
        <select  v-model="formData1.day1" >
          <option v-for="item in day1" :value="item">{{item}}日</option>
        </select>
      </span>
    </span>
     <span> —— </span>
<!--    <div><a class="btn-submit btn-submit-s" @click="submit"></a></div>-->
  <span>
      <span class="item">
        <select v-model="formData2.year2">
          <option v-for="item in year2" :value="item">{{item}}年</option>
        </select>
      </span>
      <span class="item" @change="getDay2">
        <select  v-model="formData2.month2">
          <option v-for="item in month2" :value="item">{{item}}月</option>
        </select>
      </span>
      <span class="item">
        <select  v-model="formData2.day2" >
          <option v-for="item in day2" :value="item">{{item}}日</option>
        </select>
      </span>
    </span>
  <span>&#12288 &#12288</span>
<!--    <el-botton @click="submit" type="success" size="mini">提交</el-botton>-->
    <input type='button' @click="submit" style="width:40px;height:20px;border-radius:15%;border: solid 1px;background: #9e9e9e" value="确定">

  </div>

</div>
</template>


<script>
import axios from 'axios';
export default {
        data(){
            return{

                year1:[],
                month1:[],
                day1:[],
                formData1:{
                year1:2018,
                month1:10,
                day1:30},
                year2:[],
                month2:[],
                day2:[],
                formData2:{
                year2:2018,
                month2:10,
                day2:30},
                datalist:[],
                days:["2018-10-30","2018-10-30",true],
                intervalid:[],
                }
        },
        created(){
            this.init();
            this.getdata_chart1();
            this.intervalid = setInterval(() => {
            this.getdata_chart1()
        }, 800);
        },
    beforeDestroy () {
            //console.log(this.intervalid)
      clearInterval(this.intervalid)
    },
    methods:{
        init(){
          this.getYear1();
          this.getMonth1();
          this.getDay1();
          this.getYear2();
          this.getMonth2();
          this.getDay2();

        },
        getYear1(){//获取年
          let date = new Date;
          let current_year = date.getFullYear();
          for (let i = 0; i < 10; i++) {
            let y = current_year - i;
          this.year1.push(y);
          }
        },
        getMonth1(){//获取月
          for (let i = 1; i < 13; i++) {
          this.month1.push(i);
          }
        },
        getDay1(){//获取日
          this.day1 = [];
          let day = this.getDaysInMonth1(this.formData1.year1, this.formData1.month1)
          for (let i = 1; i <= day ; i++) {
              this.day1.push(i);
          }
        },
        getYear2(){//获取年
          let date = new Date;
          let current_year = date.getFullYear();
          for (let i = 0; i < 10; i++) {
            let y = current_year - i;
          this.year2.push(y);
          }
        },
        getMonth2(){//获取月
          for (let i = 1; i < 13; i++) {
          this.month2.push(i);
          }
        },
        getDay2(){//获取日
          this.day2 = [];
          let day = this.getDaysInMonth2(this.formData2.year2, this.formData2.month2)
          for (let i = 1; i <= day ; i++) {
              this.day2.push(i);
          }
        },
        getDaysInMonth1(year, month) {//获取某个月的天数
                month = parseInt(month, 10);
          let d = new Date(year, month, 0);
          return d.getDate();
        },
        getDaysInMonth2(year, month) {//获取某个月的天数
              month = parseInt(month, 10);
        let d = new Date(year, month, 0);
        return d.getDate();

      },
        padding0(num, length) {//数字前填充0方法
         for(let len = (num + "").length; len < length; len = num.length) {
          num = "0" + num;
         }
         return num;
      },
        submit(){//提交
            let day1 = this.formData1.year1 +"-" + this.padding0(this.formData1.month1,2) +"-" + this.padding0(this.formData1.day1,2);
            let day2 = this.formData2.year2 +"-" + this.padding0(this.formData2.month2,2) +"-" + this.padding0(this.formData2.day2,2);
            let cur_date = new Date();
            if(new Date(day1)>new Date(day2))
            {
                this.days = [day1,day2,false];
                this.$message({
                    message:"请选择正确的年月日",
                    type:"error"
                })
                return;
            }
            else
            {
                this.days = [day1,day2,true];
            }
      },
         getdata_chart1(){
                let that = this;
                //let days = this.days;
               // console.log(this.days);
                if(this.days[2])
                {
                    axios.get('http://127.0.0.1:5000/api/getdata_chart1',{
                        params: {
                            day1:this.days[0],
                            day2:this.days[1]}
                    })
                        .then(function(res){

                         that.datalist = res;
                         that.drawECharts();
                }
                )

            //console.log(datalist)
                    //websocket
        }},





            drawECharts(){
                // temp 是我们的自定义样式，上面安装Echarts时有介绍
                var myChart = this.$echarts.init(document.getElementById("chart1"))
                var option = {}
                option = {
                  title:{
                      text:"可视化分析——民生分析",
                      x:'center',
                      y:'10',
                      textStyle:{ //设置主标题风格
                      color:'#fff3ae',
                      fontSize: 30,
                      Height:70},//设置主标题字体颜色
                        textAlign: null,
                      padding:0
                  },
                    tooltip: {
                        trigger: 'item',
                        formatter: "{b}: {c} ({d}%)"
                    },
                    legend: {
                        orient: 'vertical',
                        x: '70%',
                        data:
                        [
                            {name:'投诉',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                            {name:'感谢',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                            {name:'建议',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                            {name:'求决',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                            {name:'咨询',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                            {name:'其他',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                        ],
                        itemHeight:70,
                        top:'middle',

                    },
                    series: [
                        {
                            name:'访问来源',
                            type:'pie',
                            minAngle:3,
                            avoidLabelOverlap: true,
                            radius: ['0%', '65%'],
                            center:['50%','60%'],
                            label: {
                                align: 'left',
                                normal: {


                                    show: true,
                                    position: 'outside',
                                    color:'white',
                                    formatter: "{b}:{d}%"

                                },
                                emphasis: {
                                    show: false,
                                    textStyle: {
                                        fontSize: '30',
                                        fontWeight: 'bold'
                                    }
                                }
                            },
                            labelLine: {
                                normal: {
                                    show: true
                                }
                            },
                            data:
                                //this.getdata_chart1(),
                                this.datalist,
                                //this.submit(),
                                //this.getdata_chart1(this.submit()),
                                /*[
                                {value:335, name:'投诉'},
                                {value:310, name:'感谢'},
                                {value:234, name:'建议'},
                                {value:135, name:'求决'},
                                {value:15, name:'咨询'},
                                {value:5, name:'其他'},
                            ],*/
                            itemStyle: {
                                emphasis: {
                                    shadowBlur: 10,
                                    shadowOffsetX: 0,
                                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                                }
                            }
                             //
                        }
                    ],

                  // color:[
                  //     'rgb(39,204,217)',
                  //   'rgb(54,132,254)',
                  //
                  //   'rgb(153,119,238)',
                  //   'rgb(245,97,110)',
                  //   'rgb(246,177,63)',
                  //   'rgb(43,141,33)',]

                }
                 // 执行渲染图形和数据的操作
                    myChart.setOption(option)
            }
        }
    }


</script>
<style>
  .total{
    /*background: #d2ffe4;*/
    padding: 0;
    /*background-image: url(../assets/bg1.jpg);*//*
    background-size: cover;
    background-repeat: no-repeat;*/
    color:#ffffff;
    position: center;
  }
</style>
