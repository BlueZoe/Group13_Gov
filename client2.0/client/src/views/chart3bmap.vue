<template>
  <div class='total'>
    <div class="charts">

        <div id="chart3" :style="{width:'1170px',height:'550px'}"></div>
      </div>
    <div class="select-box" :style="{width:'1170px',height:'100px'}">
    <span>时间范围选择: &#12288</span>
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
        </select>f
      </span>
    </span>
  <span>&#12288 &#12288</span>
<!--    <el-botton @click="submit" type="success" size="mini">提交</el-botton>-->
    <input type='button' @click="submit" style="width:40px;height:20px;border-radius:15%;border: solid 1px;background: #9e9e9e" value="确定">
    </div>
  </div>

</template>

<script>
import bmap from 'echarts/extension/bmap/bmap.js'
import axios from 'axios';
export default {
    data(){
        return {
            year1: [],
            month1: [],
            day1: [],
            formData1: {
                year1: 2018,
                month1: 10,
                day1: 30
            },
            year2: [],
            month2: [],
            day2: [],
            formData2: {
                year2: 2018,
                month2: 10,
                day2: 30
            },
            datalist: [],
          days:["2018-10-30","2018-10-30",true],
                intervalid:[],
            }},
        created(){
            this.init();
            this.getdata_chart3();
            this.intervalid = setInterval(() => {
          this.getdata_chart3()
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
                return;
            }
            else
            {
                this.days = [day1,day2,true];
            }



      },
        getdata_chart3(){
                let that = this;
                let days = this.days;
                if(days[2])
                {
                    axios.get('http://127.0.0.1:5000/api/getdata_chart3',{
                        params: {
                            day1:this.days[0],
                            day2:this.days[1]}
                    })
                          .then(function(res){
                           that.datalist = res;
                           that.drawECharts();
                           })

                    //websocket
        }},

        drawECharts(){
            var myChart = this.$echarts.init(document.getElementById('chart3'));
            var option = {}
           /* var data = [
                    {name: '坪山社区', value: 41},
                    {name: '和平社区', value: 31},
                    {name: '金沙社区', value: 41},
                    {name: '南布社区', value: 64},
                    {name: '田心社区', value: 41},
                    {name: '碧岭社区', value: 41},
                    {name: '江岭社区', value: 41},
                    {name: '金龟社区', value: 41},
                    {name: '汤坑社区', value: 61},
                    {name: '石井社区', value: 21},
                    {name: '六和社区', value: 41},
                    {name: '沙湖社区', value: 41},
                    {name: '老坑社区', value: 36},
                    {name: '竹坑社区', value: 41},
                    {name: '秀新社区', value: 21},
                    {name: '沙田社区', value: 41},
                    {name: '六联社区', value: 78},
                    {name: '坪环社区', value: 41},
                    {name: '龙田社区', value: 41},
                    {name: '坑梓社区', value: 41},
                    {name: '田头社区', value: 41},
                    {name: '马峦社区', value: 91},
                    {name: '沙坣社区', value: 41},

                ];*/
            //let data=this.datalist;
            var geoCoordMap = {
                    '坪山社区':[114.352641,22.697439],
                    '和平社区':[114.355104,22.697106],
                    '金沙社区':[114.404081,22.758677],
                    '南布社区':[114.375607,22.70534],
                    '田心社区':[114.421943,22.700351],
                    '碧岭社区':[114.295663,22.67342],
                    '江岭社区':[114.362596,22.69202],
                    '金龟社区':[114.406461,22.663744],
                    '汤坑社区':[114.331079,22.678805],
                    '石井社区':[113.803103,23.029933],
                    '六和社区':[114.346675,22.711219],
                    '沙湖社区':[114.326552,22.67909],
                    '老坑社区':[114.369312,22.734866],
                    '竹坑社区':[114.395074,22.715773],
                    '秀新社区':[114.381223,22.746873],
                    '沙田社区':[114.404444,22.761764],
                    '六联社区':[114.332971,22.795219],
                    '坪环社区':[114.35474,22.688096],
                    '龙田社区':[114.372841,22.753346],
                    '坑梓社区':[114.390013,22.753031],
                    '田头社区':[114.410837,22.697197],
                    '马峦社区':[114.338203,22.644538],
                    '沙坣社区':[114.377888,22.690889],

                };
            var convertData = function (data) {
                    var res = [];
                    for (var i = 0; i < data.length; i++) {
                        var geoCoord = geoCoordMap[data[i].name];
                        if (geoCoord) {
                            res.push({
                                name: data[i].name,
                                value: geoCoord.concat(data[i].value)
                            });
                        }
                    }
    return res;
};
            option={
                title: {
                    text: '深圳坪山热点社区地图',
                    // subtext: 'data from PM25.in',
                    // sublink: 'http://www.pm25.in',
                    left: '10%',
                    top:'10%',
                    textStyle:{ //设置主标题风格
                                  color:'#11203e',
                                  fontSize: 20,
                                  Height:50},//设置主标题字体颜色
                },
                tooltip : {
                    trigger: 'item',
                    formatter: function(params) {
                var res = params.name+'<br/>';
                var myseries = option.series;
                for (var i = 0; i < 1; i++) {
                    for(var j=0;j<myseries[i].data.length;j++){
                        if(myseries[i].data[j].name==params.name){
                            res+=myseries[i].name +' : '+myseries[i].data[j].value[2]+'</br>';
                        }
                    }
                }
                return res;
            }
                },
                bmap: {
                    center: [114.395074,22.715773], // 中心位置坐标
                    zoom: 12.6, // 地图缩放比例
                    roam: true, // 开启用户缩放
                    mapStyle: {
                        style:'light'
                    /*styleJson: [
                        {  //地图样试
                                'featureType': 'water',
                                'elementType': 'all',
                                'stylers': {
                                    'color': '#d1d1d1'
                                }
                            }, {
                                'featureType': 'land',
                                'elementType': 'all',
                                'stylers': {
                                    'color': '#f3f3f3'
                                }
                            }, {
                                'featureType': 'railway',
                                'elementType': 'all',
                                'stylers': {
                                    'visibility': 'off'
                                }
                            }, {
                                'featureType': 'highway',
                                'elementType': 'all',
                                'stylers': {
                                    'color': '#fdfdfd'
                                }
                            }, {
                                'featureType': 'highway',
                                'elementType': 'labels',
                                'stylers': {
                                    'visibility': 'off'
                                }
                            }, {
                                'featureType': 'arterial',
                                'elementType': 'geometry',
                                'stylers': {
                                    'color': '#fefefe'
                                }
                            }, {
                                'featureType': 'arterial',
                                'elementType': 'geometry.fill',
                                'stylers': {
                                    'color': '#fefefe'
                                }
                            }, {
                                'featureType': 'poi',
                                'elementType': 'all',
                                'stylers': {
                                    'visibility': 'off'
                                }
                            }, {
                                'featureType': 'green',
                                'elementType': 'all',
                                'stylers': {
                                    'visibility': 'off'
                                }
                            }, {
                                'featureType': 'subway',
                                'elementType': 'all',
                                'stylers': {
                                    'visibility': 'off'
                                }
                            }, {
                                'featureType': 'manmade',
                                'elementType': 'all',
                                'stylers': {
                                    'color': '#d1d1d1'
                                }
                            }, {
                                'featureType': 'local',
                                'elementType': 'all',
                                'stylers': {
                                    'color': '#d1d1d1'
                                }
                            }, {
                                'featureType': 'arterial',
                                'elementType': 'labels',
                                'stylers': {
                                    'visibility': 'off'
                                }
                            }, {
                                'featureType': 'boundary',
                                'elementType': 'all',
                                'stylers': {
                                    'color': '#fefefe'
                                }
                            }, {
                                'featureType': 'building',
                                'elementType': 'all',
                                'stylers': {
                                    'color': '#d1d1d1'
                                }
                            }, {
                                'featureType': 'label',
                                'elementType': 'labels.text.fill',
                                'stylers': {
                                    'color': '#999999'
                                }
                        }]*/
                    }
                },
                 series : [
        {
            name: '热点值',
            type: 'scatter',
            coordinateSystem: 'bmap',
            data: convertData(this.datalist),
            symbolSize: function (val) {
                return 12;
            },
            label: {
                normal: {
                    formatter: '{b}',
                    position: 'right',
                    show: false
                },
                emphasis: {
                    show: true
                }
            },
            itemStyle: {
                normal: {
                    color: 'purple'
                }
            }
        },
        {
            name: 'Top 5',
            type: 'effectScatter',
            coordinateSystem: 'bmap',
            data: convertData(this.datalist.sort(function (a, b) {
                return b.value - a.value;
            }).slice(0, 6)),
            symbolSize: function (val) {
                return 20;
            },
            showEffectOn: 'render',
            rippleEffect: {
                brushType: 'stroke'
            },
            hoverAnimation: true,
            label: {
                normal: {
                    formatter: '{b}',
                    position: 'right',
                    show: true
                }
            },
            itemStyle: {
                normal: {
                    color: '#992629',
                    shadowBlur: 10,
                    shadowColor: '#333'
                }
            },
            zlevel: 1
        }
    ]


            };
            myChart.setOption(option)
        }
    }
}
</script>

<style scoped>
.select-box{
  position:absolute;
  /*left:80px;*/
  top:550px;
}

</style>
