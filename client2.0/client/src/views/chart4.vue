<template>
  <div class="total">
      <div class="charts">
        <br><br>
        <div id="chart4" :style="{width:'1170px',height:'450px'}"></div>
      </div>
    <div class="select-box" :style="{width:'1170px',height:'100px'}">

    <span><br>时间范围选择: &#12288</span>
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
    <input type='button' @click="getdata_chart4" style="width:40px;height:20px;border-radius:15%;border: solid 1px;background: #9e9e9e" value="确定">

  </div>

</div>
</template>

<script>
  import axios from 'axios';
    export default {
        name: "chart1",
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
        record:[],
        days:["2018-10-30","2018-10-30",true],
        intervalid:[],
        rad:[['0%','0%'],['0%','0%'],['0%','0%']],
        radbefore:[['0%','0%'],['0%','0%'],['0%','0%']],
            }},
        created(){
            this.init();
            this.getdata_chart4();
            /*this.intervalid = setInterval(() => {
          this.getdata_chart4()
                console.log(this.rad)
        }, 2000);*/
        },
    beforeDestroy () {
            //console.log(this.intervalid)
      clearInterval(this.intervalid)
    },

methods: {
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
    submit(){
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
          getdata_chart4(){
                let that = this;
                this.submit();
                    if(this.days[2])
                    {
                        axios.get('http://127.0.0.1:5000/api/getdata_chart4',{
                            params: {
                                day1:this.days[0],
                                day2:this.days[1]}
                        })
                          .then(function(res){
                           that.datalist = res;
                           that.drawECharts();
                           })
                    //websocket

                     }
          },


    drawECharts(){
		    var myChart = this.$echarts.init(document.getElementById("chart4"))
        var option = {}
        option ={
		        title:{text:"可视化分析——结办分析",
                      x:'center',
                      textStyle:{ //设置主标题风格
                      color:'#fff3ae',
                      fontSize: 30,
                      Height:50},//设置主标题字体颜色
                        textAlign: null,
                      padding:5},
    tooltip: {
        trigger: 'item',
        formatter: "{a} <br/>{b}: {c} ({d}%)"
    },
    legend: [
        {
        orient: 'vertical',
        x: '8%',
        top:'middle',
        data:
            [
                {name:'待结办',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                {name:'超期结办',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                {name:'按期结办',icon: 'circle',textStyle: {color: '#d2ffe4'}},
            ],
        },
        {
        orient: 'vertical',
        x: '15%',
        top:'middle',
        data:
            [
                {name:'市容环卫',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                {name:'环保水务',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                {name:'市政设施',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                {name:'规土城建',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                {name:'教育卫生',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                {name:'安全隐患',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                {name:'组织人事',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                {name:'党纪政纪',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                {name:'劳动社保',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                {name:'社区管理',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                {name:'交通运输',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                {name:'治安维稳',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                {name:'专业事件采集',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                {name:'统一战线',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                {name:'民政服务',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                {name:'文体旅游',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                {name:'食药市监',icon: 'circle',textStyle: {color: '#d2ffe4'}},
                {name:'党建群团',icon: 'circle',textStyle: {color: '#d2ffe4'}},
            ],
        },
    ],
    series: [
        {
            name:'总',
            type:'pie',
            avoidLabelOverlap:true,
            selectedMode: 'single',
            radius: [0, '40%'],
            center:['50%','60%'],
            label: {
                normal: {
                    position: 'inner'
                }
            },
            labelLine: {
                normal: {
                    show: false
                }
            },
            data:this.datalist[0]
        },
        {
            name:'待结办',
            type:'pie',
            minAngle:3,
            avoidLabelOverlap:true,
            center:['50%','60%'],
            radius: ['0%','0%'],
            label: {
                normal: {
                    show:false,
                    position:'outside',
                    formatter: ' {d}%  ',
                    backgroundColor: '#fff',
                    borderColor: '#fff',
                    borderWidth: 1,
                    borderRadius: 4,

                    rich: {
                        a: {
                            color: '#999',
                            lineHeight: 22,
                            align: 'center'
                        },
                        hr: {
                            borderColor: '#aaa',
                            width: '100%',
                            borderWidth: 0.5,
                            height: 0
                        },
                        b: {
                            fontSize: 16,
                            lineHeight: 33
                        },
                        per: {
                            color: '#eee',
                            backgroundColor: '#334455',
                            padding: [2, 4],
                            borderRadius: 2
                        }
                    }
                }
            },
            data:this.datalist[1]
        },
        {
            name:'按期结办',
            type:'pie',
            minAngle:3,
            avoidLabelOverlap:true,
            center:['50%','60%'],
            radius: ['0%','0%'],
            label: {
                normal: {
                    show:false,
                    position:'outside',
                    formatter: ' {d}%  ',
                    backgroundColor: '#fff',
                    borderColor: '#fff',
                    borderWidth: 1,
                    borderRadius: 4,

                    rich: {
                        a: {
                            color: '#999',
                            lineHeight: 22,
                            align: 'center'
                        },
                        hr: {
                            borderColor: '#aaa',
                            width: '100%',
                            borderWidth: 0.5,
                            height: 0
                        },
                        b: {
                            fontSize: 16,
                            lineHeight: 33
                        },
                        per: {
                            color: '#eee',
                            backgroundColor: '#334455',
                            padding: [2, 4],
                            borderRadius: 2
                        }
                    }
                }
            },
            data:this.datalist[2]
        }, {
            name:'超期结办',
            type:'pie',
            minAngle:3,
            avoidLabelOverlap:true,
            center:['50%','60%'],
            radius: ['0%','0%'],
            label: {
                normal: {
                    show:false,
                    position:'outside',
                    formatter: ' {d}%  ',
                    backgroundColor: '#fff',
                    borderColor: '#fff',
                    borderWidth: 1,
                    borderRadius: 4,
                    // shadowBlur:3,
                    // shadowOffsetX: 2,
                    // shadowOffsetY: 2,
                    // shadowColor: '#999',
                    // padding: [0, 7],
                    rich: {
                        a: {
                            color: '#999',
                            lineHeight: 22,
                            align: 'center'
                        },
                        // abg: {
                        //     backgroundColor: '#333',
                        //     width: '100%',
                        //     align: 'right',
                        //     height: 22,
                        //     borderRadius: [4, 4, 0, 0]
                        // },
                        hr: {
                            borderColor: '#aaa',
                            width: '100%',
                            borderWidth: 0.5,
                            height: 0
                        },
                        b: {
                            fontSize: 16,
                            lineHeight: 33
                        },
                        per: {
                            color: '#eee',
                            backgroundColor: '#334455',
                            padding: [2, 4],
                            borderRadius: 2
                        }
                    }
                }
            },
            data:this.datalist[3]
        },

    ]
},
        myChart.setOption(option)
        myChart.on('click', function (params){
		       // alert("饼图点击事件");
		        //window.open('https://www.baidu.com/s?wd=' + encodeURIComponent(params.name));
            if(params.name=='待结办')
            {
                option.series[1].radius=['60%','75%'];
                option.series[2].radius=['0%','0%'];
                option.series[3].radius=['0%','0%'];
                option.series[1].label.normal.show=true;
                option.series[2].label.normal.show=false;
                option.series[3].label.normal.show=false;
            }
            else if(params.name=='按期结办'){
                option.series[1].radius=['0%','0%'];
                option.series[2].radius=['60%','75%'];
                option.series[3].radius=['0%','0%'];
                option.series[1].label.normal.show=false;
                option.series[2].label.normal.show=true;
                option.series[3].label.normal.show=false;
            }
            else if(params.name=='超期结办'){
                option.series[1].radius=['0%','0%'];
                option.series[2].radius=['0%','0%'];
                option.series[3].radius=['60%','75%'];
                option.series[1].label.normal.show=false;
                option.series[2].label.normal.show=false;
                option.series[3].label.normal.show=true;
            }

            myChart.setOption(option)
        })


   },
},

    }
</script>

<style>
  .total{
    padding: 0;
    /*background-image: url(../assets/bg1.jpg);*/
    /*background-size: cover;*/
    /*background-repeat: no-repeat;*/
    position: center;
  }
</style>
