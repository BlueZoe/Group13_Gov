<template>
  <div class="total">
    <div class="charts">
        <br><br>
        <div id="chart2" :style="{width:'1170px',height:'450px'}"></div>
    </div>

    <div class="select-box" :style="{width:'1170px',height:'100px'} ">
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
            }},
        created(){
            this.init();
            this.getdata_chart2();
            this.intervalid = setInterval(() => {
          this.getdata_chart2()
        }, 700);
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
            }
            else
            {
                this.days = [day1,day2,true];
            }
      },
      getdata_chart2(){
                let that = this;
                if(this.days[2])
                {
                    axios.get('http://127.0.0.1:5000/api/getdata_chart2',{
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
                // temp 是我们的自定义样式，上面安装Echarts时有介绍
                var myChart = this.$echarts.init(document.getElementById("chart2"))
                var option = {}
                option = {
                    title:{
                      text:"可视化分析——各街道情况",
                      x:'center',
                      textStyle:{ //设置主标题风格
                      color:'#fff3ae',
                      fontSize: 30,
                      Height:50},//设置主标题字体颜色
                        textAlign: null,
                      padding:0
                  },
    tooltip : {
        trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    legend: {
        data:[
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
        /*data:[
            {name:'市容城管',textStyle: {color: '#d2ffe4'}},
            {name:'禽畜养殖污染',textStyle: {color: '#d2ffe4'}},
            {name:'市政、公共设施设置及维护',textStyle: {color: '#d2ffe4'}},
            {name:'商业经营噪声',textStyle: {color: '#d2ffe4'}},
            {name:'城乡规划',textStyle: {color: '#d2ffe4'}},
            {name:'房屋征收',textStyle: {color: '#d2ffe4'}},
            {name:'宣传广告违法行为',textStyle: {color: '#d2ffe4'}},
            {name:'工业噪声',textStyle: {color: '#d2ffe4'}},
            {name:'教育行政管理',textStyle: {color: '#d2ffe4'}},
            {name:'占道经营',textStyle: {color: '#d2ffe4'}},
            {name:'垃圾问题',textStyle: {color: '#d2ffe4'}},
            {name:'绿化养护',textStyle: {color: '#d2ffe4'}},
            {name:'公用部件',textStyle: {color: '#d2ffe4'}},
            {name:'交通设施',textStyle: {color: '#d2ffe4'}},
            {name:'废弃物堆放',textStyle: {color: '#d2ffe4'}},
            {name:'道路交通安全',textStyle: {color: '#d2ffe4'}},
            {name:'车辆乱停放',textStyle: {color: '#d2ffe4'}},
            {name:'社会生活噪声',textStyle: {color: '#d2ffe4'}},
            {name:'道路保洁',textStyle: {color: '#d2ffe4'}},
            {name:'医患纠纷',textStyle: {color: '#d2ffe4'}},
            {name:'人力资源',textStyle: {color: '#d2ffe4'}},
            {name:'行政效能',textStyle: {color: '#d2ffe4'}},
            {name:'医政监管',textStyle: {color: '#d2ffe4'}},
            {name:'道路设施',textStyle: {color: '#d2ffe4'}},
            {name:'水污染',textStyle: {color: '#d2ffe4'}},
            {name:'招生中的违法行为',textStyle: {color: '#d2ffe4'}},
            {name:'教育体制',textStyle: {color: '#d2ffe4'}},
            {name:'城市建设和市政管理',textStyle: {color: '#d2ffe4'}},
            {name:'其他市容违法行为或影响市容事件',textStyle: {color: '#d2ffe4'}},
            {name:'劳动就业',textStyle: {color: '#d2ffe4'}},
            {name:'劳动社保',textStyle: {color: '#d2ffe4'}},
            {name:'住宅区（园区）或建筑物内安全、环卫问题',textStyle: {color: '#d2ffe4'}},
            {name:'渣土问题',textStyle: {color: '#d2ffe4'}},
            {name:'公共交通管理',textStyle: {color: '#d2ffe4'}},
            {name:'建筑施工噪声',textStyle: {color: '#d2ffe4'}},
            {name:'违法建筑与用地行为',textStyle: {color: '#d2ffe4'}},
            {name:'供、排水及水质问题',textStyle: {color: '#d2ffe4'}},
            {name:'道路规划建设',textStyle: {color: '#d2ffe4'}},
            {name:'扬尘污染',textStyle: {color: '#d2ffe4'}},
            {name:'环卫设施设置及维护',textStyle: {color: '#d2ffe4'}},
            {name:'住房保障和房地产',textStyle: {color: '#d2ffe4'}},
            {name:'集体土地上房屋拆迁与补偿',textStyle: {color: '#d2ffe4'}},
            {name:'营业性文化娱乐噪声',textStyle: {color: '#d2ffe4'}},
            {name:'工业、住宅废气扰民',textStyle: {color: '#d2ffe4'}},
            {name:'经济纠纷',textStyle: {color: '#d2ffe4'}},
            {name:'建设工程质量',textStyle: {color: '#d2ffe4'}},
            {name:'城市公共资源管理',textStyle: {color: '#d2ffe4'}},
            {name:'服务行业废气扰民',textStyle: {color: '#d2ffe4'}},
            {name:'人口房屋',textStyle: {color: '#d2ffe4'}},
            {name:'综合事件采集',textStyle: {color: '#d2ffe4'}},
            {name:'社会治安',textStyle: {color: '#d2ffe4'}},
            {name:'土地资源管理',textStyle: {color: '#d2ffe4'}},
            {name:'交通管理',textStyle: {color: '#d2ffe4'}},
            {name:'教育收费',textStyle: {color: '#d2ffe4'}},
            {name:'违反计生政策',textStyle: {color: '#d2ffe4'}},
            {name:'工商经济联络',textStyle: {color: '#d2ffe4'}},
            {name:'交通运输噪声',textStyle: {color: '#d2ffe4'}},
            {name:'其他公共安全隐患',textStyle: {color: '#d2ffe4'}},
            {name:'消防设施安全',textStyle: {color: '#d2ffe4'}},
            {name:'建筑市场',textStyle: {color: '#d2ffe4'}},
            {name:'建筑消防安全',textStyle: {color: '#d2ffe4'}},
            {name:'危险化学品安全',textStyle: {color: '#d2ffe4'}},
            {name:'医疗机构违规经营',textStyle: {color: '#d2ffe4'}},
            {name:'教学违规',textStyle: {color: '#d2ffe4'}},
            {name:'环保标志管理',textStyle: {color: '#d2ffe4'}},
            {name:'双拥优抚',textStyle: {color: '#d2ffe4'}},
            {name:'环保管理',textStyle: {color: '#d2ffe4'}},
            {name:'物业服务管理监督',textStyle: {color: '#d2ffe4'}},
            {name:'宣传舆论',textStyle: {color: '#d2ffe4'}},
            {name:'互联网与通讯',textStyle: {color: '#d2ffe4'}},
            {name:'户籍证件',textStyle: {color: '#d2ffe4'}},
            {name:'警务督察',textStyle: {color: '#d2ffe4'}},
            {name:'经济管理',textStyle: {color: '#d2ffe4'}},
            {name:'线路消防安全',textStyle: {color: '#d2ffe4'}},
            {name:'社区公共管理',textStyle: {color: '#d2ffe4'}},
            {name:'医疗机构违规收费',textStyle: {color: '#d2ffe4'}},
            {name:'药品（医疗器械）监管',textStyle: {color: '#d2ffe4'}},
            {name:'面源污染隐患',textStyle: {color: '#d2ffe4'}},
            {name:'党的建设',textStyle: {color: '#d2ffe4'}},
            {name:'表达情感',textStyle: {color: '#d2ffe4'}},
            {name:'福利慈善',textStyle: {color: '#d2ffe4'}},
            {name:'刑案侦破',textStyle: {color: '#d2ffe4'}},
            {name:'公共设施保洁',textStyle: {color: '#d2ffe4'}},
            {name:'消费维权',textStyle: {color: '#d2ffe4'}},
            {name:'地质安全',textStyle: {color: '#d2ffe4'}},
            {name:'野生资源管理',textStyle: {color: '#d2ffe4'}},
            {name:'社会组织',textStyle: {color: '#d2ffe4'}},
            {name:'军转安置',textStyle: {color: '#d2ffe4'}},
            {name:'生态破坏',textStyle: {color: '#d2ffe4'}},
            {name:'劳动保护',textStyle: {color: '#d2ffe4'}},
            {name:'安全生产',textStyle: {color: '#d2ffe4'}},
            {name:'社区建设',textStyle: {color: '#d2ffe4'}},
            {name:'无证无照经营',textStyle: {color: '#d2ffe4'}},
            {name:'文化',textStyle: {color: '#d2ffe4'}},
            {name:'危险废物、化学品污染',textStyle: {color: '#d2ffe4'}},
            {name:'质监检验检疫',textStyle: {color: '#d2ffe4'}},
            {name:'燃气安全',textStyle: {color: '#d2ffe4'}},
            {name:'社会救助',textStyle: {color: '#d2ffe4'}},
            {name:'公共卫生',textStyle: {color: '#d2ffe4'}},
            {name:'商标管理',textStyle: {color: '#d2ffe4'}},
            {name:'国有土地上房屋征收与补偿',textStyle: {color: '#d2ffe4'}},
            {name:'固体废物',textStyle: {color: '#d2ffe4'}},
            {name:'经济违法行为举报',textStyle: {color: '#d2ffe4'}},
            {name:'教师队伍和待遇',textStyle: {color: '#d2ffe4'}},
            {name:'出入境检验检疫',textStyle: {color: '#d2ffe4'}},
            {name:'价格监管',textStyle: {color: '#d2ffe4'}},
            {name:'普法教育',textStyle: {color: '#d2ffe4'}},
            {name:'食品安全',textStyle: {color: '#d2ffe4'}},
            {name:'小散乱污',textStyle: {color: '#d2ffe4'}},
            {name:'建筑设计',textStyle: {color: '#d2ffe4'}},
            {name:'义工联',textStyle: {color: '#d2ffe4'}},
            {name:'复退安置',textStyle: {color: '#d2ffe4'}},
            {name:'核安全',textStyle: {color: '#d2ffe4'}},
            {name:'人口计生',textStyle: {color: '#d2ffe4'}},
            {name:'体育',textStyle: {color: '#d2ffe4'}},
            {name:'校园安全',textStyle: {color: '#d2ffe4'}},
            {name:'民间纠纷',textStyle: {color: '#d2ffe4'}},
            {name:'招录辞退',textStyle: {color: '#d2ffe4'}},
            {name:'食药监问题',textStyle: {color: '#d2ffe4'}},
            {name:'征转地审批',textStyle: {color: '#d2ffe4'}},
            {name:'旅游市场管理',textStyle: {color: '#d2ffe4'}},
            {name:'工作纪律',textStyle: {color: '#d2ffe4'}},
            {name:'跨河桥、河堤、河道破损',textStyle: {color: '#d2ffe4'}},
            {name:'卫生问题',textStyle: {color: '#d2ffe4'}},
            {name:'科学技术',textStyle: {color: '#d2ffe4'}},
            {name:'编制职务',textStyle: {color: '#d2ffe4'}},
            {name:'宣传教育',textStyle: {color: '#d2ffe4'}},
            {name:'建筑安装',textStyle: {color: '#d2ffe4'}},
            {name:'信息化建设',textStyle: {color: '#d2ffe4'}},
            {name:'网约车管理',textStyle: {color: '#d2ffe4'}},
            {name:'知识产权',textStyle: {color: '#d2ffe4'}},
            {name:'更改房屋结构',textStyle: {color: '#d2ffe4'}},
            {name:'市场垄断',textStyle: {color: '#d2ffe4'}},
            {name:'文化市场违法行为',textStyle: {color: '#d2ffe4'}},

            ],*/
        top:'20%',
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '0%',
        top:'30%',
        containLabel: true
    },
    xAxis : [
        {
            type : 'category',
            axisLine:{
        　　　　show:true,
        　　　　onZero:true,
        　　　　lineStyle:{
        　　　　color: '#fff',
        　　　　width: 2,
        　　　　type: 'solid'
        　　　　}
            },
            data : ['坪山街道','碧岭街道','龙田街道','坑梓街道','马峦街道','石井街道',]
        }
    ],
    yAxis : [
        {
            type : 'value',
            axisLine:{
        　　　　show:true,
        　　　　onZero:true,
        　　　　lineStyle:{
        　　　　color: '#fff',
        　　　　width: 2,
        　　　　type: 'solid'
        　　　　}
            },
        }
    ],
    /*series : [
        {
            name:'市容城管',
            type:'bar',
            stack: 'xx',
            barWidth:55,
            data:[120, 132, 101, 134, 90, 0]
        },
        {
            name:'禽畜养殖污染',
            type:'bar',
            stack: 'xx',
            data:[220, 182, 191, 234, 290,0]
        },
        {
            name:'市政/公共设施',
            type:'bar',
            stack: '广告',
            data:[150, 232, 201, 154, 1900]
        },
        {
            name:'教育卫生',
            type:'bar',
            stack: '广告',
            data:[862, 1018, 964, 1026, 1679, 0],

        },
        {
            name:'党纪政纪',
            type:'bar',
            stack: '广告',
            data:[620, 732, 701, 734, 1090, 0]
        },
        {
            name:'环保水务',
            type:'bar',
            stack: '广告',
            data:[120, 132, 101, 134, 290, 0]
        },
        {
            name:'交通运输',
            type:'bar',
            stack: '广告',
            data:[60, 72, 71, 74, 190, 0]
        },
        {
            name:'其他',
            type:'bar',
            stack: '广告',
            data:[62, 82, 91, 84, 109, 0]
        }

    ],*/
    series:this.datalist
}
                 // 执行渲染图形和数据的操作
                    myChart.setOption(option)
            }
        }
    }


</script>

<style scoped>
  .total{
    /*background: #d2ffe4;*/
    padding: 0;
    /*background-image: url(../assets/bg1.jpg);*/
   /* background-size: cover;
    background-repeat: no-repeat;*/
    color:#ffffff;
    position: center;
  }
</style>
