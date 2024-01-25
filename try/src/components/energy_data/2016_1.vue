<template>
  <div class="chart-container">
    <div id="chart1" class="chart"></div>
    <div id="chart2" class="chart"></div>
    <div id="chart5" class="chart"></div>
    <div id="chart6" class="chart"></div>
    <div class="flex-container">
      <div id="chart3" class="chart"></div>
      <div id="chart4" class="chart"></div>
    </div>
  </div>
</template>
  
<script>
import * as echarts from 'echarts';
import Data_2016_1 from './2016_1da.json'; // 引入JSON数据
import ecStat from 'echarts-stat';
import anotherData from './2016_1mv.json';
import ms20161Data from './2016_1_monthly_sum.json';
import ms20162Data from './2016_2_monthly_sum.json';
import ms20163Data from './2016_3_monthly_sum.json';
import ms20171Data from './2017_1_monthly_sum.json';
import ms20172Data from './2017_2_monthly_sum.json';
import ms20173Data from './2017_3_monthly_sum.json';
import ms20181Data from './2018_1_monthly_sum.json';
import ms20182Data from './2018_2_monthly_sum.json';
import ms20183Data from './2018_3_monthly_sum.json';
import ms20191Data from './2019_1_monthly_sum.json';
import ms20192Data from './2019_2_monthly_sum.json';
import ms20193Data from './2019_3_monthly_sum.json';
import ms20201Data from './2020_1_monthly_sum.json';
import ms20202Data from './2020_2_monthly_sum.json';
import ms20203Data from './2020_3_monthly_sum.json';
import ms20211Data from './2021_1_monthly_sum.json';
import ms20212Data from './2021_2_monthly_sum.json';
import ms20213Data from './2021_3_monthly_sum.json';
import 'echarts-gl';
import $ from 'jquery';

export default {
  name: 'Module2016_1',
  created() {
    this.fetchData(this.$route.params.year, this.$route.params.module);
  },
  watch: {
    '$route'(to, from) {
      // 路由变化时的逻辑处理
      this.fetchData(to.params.year, to.params.module);
    }
  },
  data() {
    return {
      // 如果需要，在data中添加你的响应式数据
    };
  },
  methods: {
    fetchData(year, module) {
      // 根据年份和模块编号获取数据
    },
    myEcharts1() {
      var chartDom = document.getElementById('chart1');
      var myChart = echarts.init(chartDom);
      var option;
      // 使用导入的JSON数据
      const timeData = Data_2016_1.map(item => {
        // 解析日期字符串为日期对象
        return new Date(item.DateTime).getTime(); // 转换为时间戳
      });
      const hvacActualData = Data_2016_1.map(item => [new Date(item.DateTime).getTime(), item['HVAC Actual [kW]']]);
      // prettier-ignore
      const chillerPowerData = Data_2016_1.map(item => [new Date(item.DateTime).getTime(), item['Chiller Power [kW]']]);
      option = {
        title: {
          text: 'HVAC Actual and Chiller Power ',
          left: 'center'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            animation: false
          }
        },
        legend: {
          data: ['HVAC Actual', 'Chiller Power'],
          left: 10
        },
        toolbox: {
          feature: {
            dataZoom: {
              yAxisIndex: 'none'
            },
            restore: {},
            saveAsImage: {}
          }
        },
        axisPointer: {
          link: [
            {
              xAxisIndex: 'all'
            }
          ]
        },
        dataZoom: [
          {
            show: true,
            realtime: true,
            start: 30,
            end: 70,
            xAxisIndex: [0, 1]
          },
          {
            type: 'inside',
            realtime: true,
            start: 30,
            end: 70,
            xAxisIndex: [0, 1]
          }
        ],
        grid: [
          {
            left: 60,
            right: 50,
            height: '35%'
          },
          {
            left: 60,
            right: 50,
            top: '55%',
            height: '35%'
          }
        ],
        xAxis: [
          {
            type: 'time',
            boundaryGap: false,
            axisLine: { onZero: true },
            data: timeData
          },
          {
            gridIndex: 1,
            type: 'time',
            boundaryGap: false,
            axisLine: { onZero: true },
            data: timeData,
            position: 'top'
          }
        ],
        yAxis: [
          {
            name: 'Chiller Power [kW]',
            type: 'value',
            max: 5
          },
          {
            gridIndex: 1,
            name: 'HVAC Actual [kW]',
            type: 'value',
            inverse: true
          }
        ],
        series: [
          {
            name: 'Chiller Power [kW]',
            type: 'line',
            symbolSize: 8,
            // prettier-ignore
            data: chillerPowerData
          },
          {
            name: 'HVAC Actual',
            type: 'line',
            xAxisIndex: 1,
            yAxisIndex: 1,
            symbolSize: 8,
            // prettier-ignore
            data: hvacActualData
          }
        ]
      };

      option && myChart.setOption(option);
    },
    myEcharts2() {
      var chartDom = document.getElementById('chart2');
      var myChart = echarts.init(chartDom);

      // 使用导入的JSON数据
      const timeData = Data_2016_1.map(item => {
        // 解析日期字符串为日期对象
        return new Date(item.DateTime).getTime(); // 转换为时间戳
      });
      const hvacActualData = Data_2016_1.map(item => [new Date(item.DateTime).getTime(), item['HVAC Actual [kW]']]);
      const chillerPowerData = Data_2016_1.map(item => [new Date(item.DateTime).getTime(), item['Chiller Power [kW]']]);

      const option = {
        title: {
          text: 'HVAC and Chiller Power vs Time',
          left: 'center'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            animation: false
          }
        },
        legend: {
          data: ['HVAC Actual [kW]', 'Chiller Power [kW]'],
          left: 10
        },
        toolbox: {
          feature: {
            dataZoom: {
              yAxisIndex: 'none'
            },
            restore: {},
            saveAsImage: {}
          }
        },
        axisPointer: {
          link: { xAxisIndex: 'all' }
        },
        dataZoom: [{
          show: true,
          realtime: true,
          start: 0,
          end: 100
        }, {
          type: 'inside',
          realtime: true,
          start: 0,
          end: 100
        }],
        xAxis: {
          type: 'time',
          boundaryGap: false,
          data: timeData
        },
        yAxis: [
          {
            name: 'HVAC Actual [kW]',
            type: 'value',
            position: 'left'
          },
          {
            name: 'Chiller Power [kW]',
            type: 'value',
            position: 'right',
            inverse: true
          }
        ],
        series: [
          {
            name: 'HVAC Actual [kW]',
            type: 'line',
            data: hvacActualData,
            areaStyle: {},
            yAxisIndex: 0,
          },
          {
            name: 'Chiller Power [kW]',
            type: 'line',
            data: chillerPowerData,
            areaStyle: {},
            yAxisIndex: 1,
          }
        ]
      };

      myChart.setOption(option);
    },
    myEcharts3() {
      var chartDom = document.getElementById('chart3');
      var myChart = echarts.init(chartDom);
      var option;

      var newData = Data_2016_1.map(item => [
        item['HVAC Actual [kW]'],
        item['Chiller Power [kW]']
      ]);
      var DIM_CLUSTER_INDEX = 2;
      var DATA_DIM_IDX = [0, 1];
      var CENTER_DIM_IDX = [3, 4];
      // See https://github.com/ecomfe/echarts-stat
      var step = ecStat.clustering.hierarchicalKMeans(newData, {
        clusterCount: 6,
        outputType: 'single',
        outputClusterIndexDimension: DIM_CLUSTER_INDEX,
        outputCentroidDimensions: CENTER_DIM_IDX,
        stepByStep: true
      });
      var colorAll = [
        '#bbb',
        '#37A2DA',
        '#e06343',
        '#37a354',
        '#b55dba',
        '#b5bd48',
        '#8378EA',
        '#96BFFF'
      ];
      var ANIMATION_DURATION_UPDATE = 1500;
      function renderItemPoint(params, api) {
        var coord = api.coord([api.value(0), api.value(1)]);
        var clusterIdx = api.value(2);
        if (clusterIdx == null || isNaN(clusterIdx)) {
          clusterIdx = 0;
        }
        var isNewCluster = clusterIdx === api.value(3);
        var extra = {
          transition: []
        };
        var contentColor = colorAll[clusterIdx];
        return {
          type: 'circle',
          x: coord[0],
          y: coord[1],
          shape: {
            cx: 0,
            cy: 0,
            r: 10
          },
          extra: extra,
          style: {
            fill: contentColor,
            stroke: '#333',
            lineWidth: 1,
            shadowColor: contentColor,
            shadowBlur: isNewCluster ? 12 : 0,
            transition: ['shadowBlur', 'fill']
          }
        };
      }
      function renderBoundary(params, api) {
        var xVal = api.value(0);
        var yVal = api.value(1);
        var maxDist = api.value(2);
        var center = api.coord([xVal, yVal]);
        var size = api.size([maxDist, maxDist]);
        return {
          type: 'ellipse',
          shape: {
            cx: isNaN(center[0]) ? 0 : center[0],
            cy: isNaN(center[1]) ? 0 : center[1],
            rx: isNaN(size[0]) ? 0 : size[0] + 15,
            ry: isNaN(size[1]) ? 0 : size[1] + 15
          },
          extra: {
            renderProgress: ++targetRenderProgress,
            enterFrom: {
              renderProgress: 0
            },
            transition: 'renderProgress'
          },
          style: {
            fill: null,
            stroke: 'rgba(0,0,0,0.2)',
            lineDash: [4, 4],
            lineWidth: 4
          }
        };
      }
      function makeStepOption(option, data, centroids) {
        var newCluIdx = centroids ? centroids.length - 1 : -1;
        var maxDist = 0;
        for (var i = 0; i < data.length; i++) {
          var line = data[i];
          if (line[DIM_CLUSTER_INDEX] === newCluIdx) {
            var dist0 = Math.pow(line[DATA_DIM_IDX[0]] - line[CENTER_DIM_IDX[0]], 2);
            var dist1 = Math.pow(line[DATA_DIM_IDX[1]] - line[CENTER_DIM_IDX[1]], 2);
            maxDist = Math.max(maxDist, dist0 + dist1);
          }
        }
        var boundaryData = centroids
          ? [[centroids[newCluIdx][0], centroids[newCluIdx][1], Math.sqrt(maxDist)]]
          : [];
        option.options.push({
          series: [
            {
              type: 'custom',
              encode: {
                tooltip: [0, 1]
              },
              renderItem: renderItemPoint,
              data: data
            },
            {
              type: 'custom',
              renderItem: renderBoundary,
              animationDuration: 3000,
              silent: true,
              data: boundaryData
            }
          ]
        });
      }
      var targetRenderProgress = 0;
      option = {
        timeline: {
          top: 'center',
          right: 50,
          height: 300,
          width: 10,
          inverse: true,
          autoPlay: false,
          playInterval: 2500,
          symbol: 'none',
          orient: 'vertical',
          axisType: 'category',
          label: {
            formatter: 'step {value}',
            position: 10
          },
          checkpointStyle: {
            animationDuration: ANIMATION_DURATION_UPDATE
          },
          data: []
        },
        baseOption: {
          animationDurationUpdate: ANIMATION_DURATION_UPDATE,
          transition: ['shape'],
          tooltip: {},
          xAxis: {
            type: 'value',
            min: -1,   // X轴的最小值
            max: 5,   // X轴的最大值
            axisLine: {
              show: false, // 不显示 x 轴的轴线
            },
          },
          yAxis: {
            type: 'value',
            min: -1,   // X轴的最小值
            max: 5,   // X轴的最大值
            axisLine: {
              show: false, // 不显示 x 轴的轴线
            },
          },
          series: [
            {
              // ...其他系列配置
              type: 'scatter',
              data: newData,
              markLine: {
                silent: true, // 不响应事件
                symbol: 'none', // 去掉标记点
                label: { show: false }, // 不显示标签
                data: [
                  { xAxis: 2 }, // 在 x=2 的位置添加一条线，模拟 x 轴线
                  { yAxis: 2 }  // 在 y=2 的位置添加一条线，模拟 y 轴线
                ],
                lineStyle: {
                  color: 'black', // 颜色
                  type: 'solid', // 类型
                  width: 2 // 宽度
                },

              }
            }
          ]
        },
        options: []
      };
      makeStepOption(option, newData);
      option.timeline.data.push('0');
      for (var i = 1, stepResult; !(stepResult = step.next()).isEnd; i++) {
        makeStepOption(
          option,
          echarts.util.clone(stepResult.data),
          echarts.util.clone(stepResult.centroids)
        );
        option.timeline.data.push(i + '');
      }

      option && myChart.setOption(option, true);

    },
    myEcharts4() {
      var chartDom = document.getElementById('chart4');
      var myChart = echarts.init(chartDom);
      var option;

      // 假设jsonData是您已经加载的JSON数据
      var days = anotherData.map(item => item.DateTime);
      var values1 = anotherData.map(item => item['HVAC Actual [kW]']);
      var values2 = anotherData.map(item => item['Chiller Power [kW]']);

      option = {
        title: {
          text: 'HVAC and Chiller Power Data (Variance)',
          left: 'left' // 将标题放置在左边
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: ['HVAC Actual [kW]', 'Chiller Power [kW]'],
          right: 'right', // 将图例放置在右边
          top: 'top' // 可以进一步指定顶部位置，或者其他具体的位置值
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: days  // 使用映射得到的日期数组
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            name: 'HVAC Actual [kW]',
            type: 'line',
            data: values1  // 使用映射得到的第一个值数组
          },
          {
            name: 'Chiller Power [kW]',
            type: 'line',
            data: values2  // 使用映射得到的第二个值数组
          }
        ]
      };

      option && myChart.setOption(option);
    },
    myEcharts5() {
      var ROOT_PATH = 'https://echarts.apache.org/examples';

      var chartDom = document.getElementById('chart5');
      var myChart = echarts.init(chartDom);
      var option;
      var paperDataURI =
        'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJgAAAAyCAYAAACgRRKpAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAB6FJREFUeNrsnE9y2zYYxUmRkig7spVdpx3Hdqb7ZNeFO2PdoD1Cj9DeoEdKbmDPeNFNW7lu0y7tRZvsYqfjWhL/qPgggoIggABIQKQkwsOhE5sQCfzw3uNHJu5sNnOaZq29RttolwfAbxgwChO9nad//4C2C7S9Sfe3uzQobqNghdoJBdIw3R8qHnvNANcA1sBUGCaV9pYC7rYBbLvbgAFpaBgmWbujlO1NA9h2wQTbcdHOoih2ZujLa7WcFtoMtUsKuFEDWL3bkAHq2GTnT+OJkyTzsXRd1/G8FoYN9vBnQ+pGZ7f7BrDqYSLbq6IdxXGM96BKIlBgDP97mgj7aLXcDLa8fgqoGwFu1ABmvzwwLAuTTJmw/SFIfG/ZBmEMIwRiHCVOnCTSPkk/BDoD7YHJbvcNYOVgYmtNWo1cs0xJ8pQJDgXIfM9bscE4TrDyAWwETuEEpP0QSzWU365T0CpXtzoDdsJY3bmpjqfT0AlRKMfWhQBhFYkGLAwjpE6JIxsnAAz6YW0QjksQaBGGTq0fw/mt0kJvXQA7cezWmpYaqBJ73XmKREABQMAKARjZsOXZqU4/FvLbWgu9VQA24NzRGYEJJm6C1GmuJJ4w39C5Sj6x/H6IKiWxPHflwQv9wPEV5TeibgS4200DzGitSdX6VCZWR0nonAR98dQNgxInpey0BvnNeKHXJGDGYYLiJQwiqIjuHZ+uKsWpEsUYOHVAeOdm0k4rzm9vKYUbrRswY7UmcVYa48mR5SN2YgkoMlXCoHEmQ6cfAojni1VkAUmsrEplVddCfitU6FUFzDpMvDw1nkzFA5dz91dkYvP61MlJREV8waQWUSWRnVac35QeY/EAe83c0RmDCSzMRV+w2nlZhp1UyFNyJVpMaJ6VmlQ3HUBE9rdSpIUbhhJ2WnF+ExZ63U+f/v2h02mfeb7/JZp0a8rEK1ouVqeXu6LwhEZqA0eCuCyD6ExGngVmKpICJ5tUEbjFsmC+nRZRSsSC0UKv++7Pv676/f7ZQb/v7O/vm3p0wQ3sUEIoM/hsDpFNqKqV6t1R5ltgnJ6Xyt0kOT+RZelCQmcuVs1VrhGOC7qd0kIyV2N87j+7v938cUFXyQ8O+nh7hmBrt9vGVUz1mZ3nicsC7ISqTICqldLqFilaoEjddOxP5UamiJ3CubV9n+sKbH7rdHzu74rnE/UzW9QCASpmvC5XekOWiTdoQRA4z58PEGx7+PvSNRE0aHABbV+eiYjlTJ0oW5m+761M4txePWmox5ODVDTCdbIwF2Dysw4zqTzFxOc/TbjlC/p6ZbYM109/Bk+NuP3l2Cn+nDDhQtNKFwTdF3xm7sJLMmWSLmj4nel0+swdXd9coQ86k8EB3gw2enBwgKx0z8pdo4pqECv1Jbfe2lYqAJinmKoWmAexdilEougiOy1qe/P+UrubyfMlfPbT05MzHo/xHsHldLvde/fi8vKjM3MGQa/n9NDmuvIMBhOMrdRSbiOqAWqjEupVrVQFDFWAdS1fVpzVKal00WKHxaAyhi1XXpJYtrpZar/y8tXj4+MSUMuC1AGe7jBgURgOspPvBvMt6CrBto7cphrAdepjcXpnagpgnUCu+mA9FljRXq9bqmiKlSmZ5zhieUplJkqhYE+ajywYqRWOUSlYWQZzf/n1+qc4jr4KEYFAYRSF2YrrBkEGnGoznduKK5FefUwZ4Ja8rKJbBIV+QZVEi4LuC97776HFb8vqZEARmACkAPPRzVvMl+j3/fH8oCA9oWQOWhg603DqPNx/xAMKPwcb9f18hYITef/+g7XcRkJ9R6JEvFDPUwxsXchuiOXkATxf7TEuAMvKKnSIXla31bwF/eYpEhvIpUFc0+pIg3mnoaKszjk8PMQw+b7ev9VeKVOIPjicTtBkRXiAADQATvUh9Lpym+n6mJaVpiUBmZXy8lbRIJ7d0WlanQgogIlYXRGYqCLrBdkAsB/RN987Gu9kgY3CyUGA1Mlq68ptNupjOnd9vaCj/OhF/fVtJ81Mi2ymX+yOMqCgHwCIQAX7ElX7DKj9vWDpIXj2LPLm93ffoh3Z1vmPTa3nNtU7NNW3NvLKKnAMhPDSCyRVpUVRdVYYKAImXBsTwo0DtTKmvBOvEjbb9TZdK8X5TOEOkpQr3DSwF7E6+u6ubAOHgQVQEiZtoJQA48A2TGE7XidstnObqpUG3bZW3tSxOs7jlapbKaC0AWNgg1d4vqsCtnXkNtFbG2XqTjqPVypqdwxQtyY7L/xGa9Ww2c5txPZgeDptX/mY7E2CWbEgvulAGQOsTrDZzm1Cq8t/k2AngbICWJ1gs5Xbij5e2TWgrAPGwHaSggbAvariAovktjKPV3YdqLUCVjfYeLmt6JsEDVA1A6xusEFue/HiuM5Wt5FA1QKwusD28uXLBqhtB0wAG2znOwLYVgFVa8AY2AYUbN9sEWBbDdTGALYO2NYE2E4BtZGA2YLNEmA7DdTGA2YSttPT04nrut0GqAYwVdiGjsZrRkdHR3ftdlv3aQP9/zA0QO0KYBzgpO+0KQL2wCjUqMGmAUwJNgFgDVANYGZgQ4DdI8AGDVANYFba3/98+PqLzz+7ajCw1/4XYABXWBExzrUA+gAAAABJRU5ErkJggg==';
      option = {
        backgroundColor: '#0f375f',
        tooltip: {},
        legend: {
          textStyle: { color: '#ddd' }
        },
        xAxis: [
          {
            data: ['Energy power bills', '', 'Qomolangma', 'Kilimanjaro'],
            axisTick: { show: false },
            axisLine: { show: false },
            axisLabel: {
              margin: 20,
              color: '#ddd',
              fontSize: 14
            }
          }
        ],
        yAxis: {
          splitLine: { show: false },
          axisTick: { show: false },
          axisLine: { show: false },
          axisLabel: { show: false }
        },
        markLine: {
          z: -1
        },
        animationEasing: 'elasticOut',
        series: [
          {
            type: 'pictorialBar',
            name: 'All',
            emphasis: {
              scale: true
            },
            label: {
              show: true,
              position: 'top',
              formatter: '{c} m',
              fontSize: 16,
              color: '#e54035'
            },
            data: [
              {
                value: 14563,
                symbol: 'image://' + paperDataURI,
                symbolRepeat: true,
                symbolSize: ['130%', '20%'],
                symbolOffset: [0, 10],
                symbolMargin: '-30%',
                animationDelay: function (dataIndex, params) {
                  return params.index * 30;
                }
              },
              {
                value: '-',
                symbol: 'none'
              },
              {
                value: 8844,
                symbol:
                  'image://' + ROOT_PATH + '/data/asset/img/hill-Qomolangma.png',
                symbolSize: ['200%', '105%'],
                symbolPosition: 'end',
                z: 10
              },
              {
                value: 5895,
                symbol:
                  'image://' + ROOT_PATH + '/data/asset/img/hill-Kilimanjaro.png',
                symbolSize: ['200%', '105%'],
                symbolPosition: 'end'
              }
            ],
            markLine: {
              symbol: ['none', 'none'],
              label: {
                show: false
              },
              lineStyle: {
                color: '#e54035',
                width: 2
              },
              data: [
                {
                  yAxis: 8844
                }
              ]
            }
          },
          {
            name: 'All',
            type: 'pictorialBar',
            barGap: '-100%',
            symbol: 'circle',
            itemStyle: {
              color: '#185491'
            },
            silent: true,
            symbolOffset: [0, '50%'],
            z: -10,
            data: [
              {
                value: 1,
                symbolSize: ['150%', 50]
              },
              {
                value: '-'
              },
              {
                value: 1,
                symbolSize: ['200%', 50]
              },
              {
                value: 1,
                symbolSize: ['200%', 50]
              }
            ]
          }
        ]
      };

      option && myChart.setOption(option);
    },
    myEcharts6() {
      var chartDom = document.getElementById('chart6');
      var myChart = echarts.init(chartDom);
      var option;

      var dataMap = {};
      function dataFormatter(obj) {
        // prettier-ignore
        var pList = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'];
        var temp;
        for (var year = 2016; year <= 2021; year++) {
          var max = 0;
          var sum = 0;
          temp = obj[year];
          for (var i = 0, l = temp.length; i < l; i++) {
            max = Math.max(max, temp[i]);
            sum += temp[i];
            obj[year][i] = {
              name: pList[i],
              value: temp[i]
            };
          }
          obj[year + 'max'] = Math.floor(max / 100) * 100;
          obj[year + 'sum'] = sum;
        }
        return obj;
      }
      // prettier-ignore
      const timeData = Data_2016_1.map(item => {
        // 解析日期字符串为日期对象
        return new Date(item.DateTime).getTime(); // 转换为时间戳
      });
      const msum20161Data = ms20161Data.map(item =>item['HVAC Actual [kW]']);
      const msum20162Data = ms20161Data.map(item =>item['Chiller Power [kW]']);
      const msum20163Data = ms20162Data.map(item =>item['Humidifier power [kW]']);
      const msum20164Data = ms20162Data.map(item =>item['HV light Power [kW]']);
      const msum20165Data = ms20163Data.map(item =>item['Power[kW]']);
      const msum20166Data = ms20163Data.map(item =>item['PV panels power [kW]']);
      const msum20171Data = ms20171Data.map(item =>item['HVAC Actual [kW]']);
      const msum20172Data = ms20171Data.map(item =>item['Chiller Power [kW]']);
      const msum20173Data = ms20172Data.map(item =>item['Humidifier power [kW]']);
      const msum20174Data = ms20172Data.map(item =>item['HV light Power [kW]']);
      const msum20175Data = ms20173Data.map(item =>item['Power[kW]']);
      const msum20176Data = ms20173Data.map(item =>item['PV panels power [kW]']);
      const msum20181Data = ms20181Data.map(item =>item['HVAC Actual [kW]']);
      const msum20182Data = ms20181Data.map(item =>item['Chiller Power [kW]']);
      const msum20183Data = ms20182Data.map(item =>item['Humidifier power [kW]']);
      const msum20184Data = ms20182Data.map(item =>item['HV light Power [kW]']);
      const msum20185Data = ms20183Data.map(item =>item['Power[kW]']);
      const msum20186Data = ms20183Data.map(item =>item['PV panels power [kW]']);
      const msum20191Data = ms20191Data.map(item =>item['HVAC Actual [kW]']);
      const msum20192Data = ms20191Data.map(item =>item['Chiller Power [kW]']);
      const msum20193Data = ms20192Data.map(item =>item['Humidifier power [kW]']);
      const msum20194Data = ms20192Data.map(item =>item['HV light Power [kW]']);
      const msum20195Data = ms20193Data.map(item =>item['Power[kW]']);
      const msum20196Data = ms20193Data.map(item =>item['PV panels power [kW]']);
      const msum20201Data = ms20201Data.map(item =>item['HVAC Actual [kW]']);
      const msum20202Data = ms20201Data.map(item =>item['Chiller Power [kW]']);
      const msum20203Data = ms20202Data.map(item =>item['Humidifier power [kW]']);
      const msum20204Data = ms20202Data.map(item =>item['HV light Power [kW]']);
      const msum20205Data = ms20203Data.map(item =>item['Power[kW]']);
      const msum20206Data = ms20203Data.map(item =>item['PV panels power [kW]']);
      const msum20211Data = ms20211Data.map(item =>item['HVAC Actual [kW]']);
      const msum20212Data = ms20211Data.map(item =>item['Chiller Power [kW]']);
      const msum20213Data = ms20212Data.map(item =>item['Humidifier power [kW]']);
      const msum20214Data = ms20212Data.map(item =>item['HV light Power [kW]']);
      const msum20215Data = ms20213Data.map(item =>item['Power[kW]']);
      const msum20216Data = ms20213Data.map(item =>item['PV panels power [kW]']);
      option = {
        baseOption: {
          timeline: {
            axisType: 'category',
            // realtime: false,
            // loop: false,
            autoPlay: true,
            // currentIndex: 2,
            playInterval: 1000,
            // controlStyle: {
            //     position: 'left'
            // },
            data: [
              '2016-01-01',
              '2017-01-01',
              '2018-01-01',
              '2019-01-01',
              '2020-01-01',
              '2021-01-01',

            ],
            label: {
              formatter: function (s) {
                return new Date(s).getFullYear();
              }
            }
          },
          title: {
            subtext: '数据来自kaggle'
          },
          tooltip: {},
          legend: {
            left: 'right',
            data: ['HVAC Actual [kW]', 'Chiller Power [kW]', 'Humidifier power [kW]', 'HV light Power [kW]', 'Power[kW]', 'PV panels power [kW]'],
            selected: {
              HVAC_Actual: false,
              Chiller_Power: false,
              Humidifier_power: false
            }
          },
          calculable: true,
          grid: {
            top: 80,
            bottom: 100,
            tooltip: {
              trigger: 'axis',
              axisPointer: {
                type: 'shadow',
                label: {
                  show: true,
                  formatter: function (params) {
                    return params.value.replace('\n', '');
                  }
                }
              }
            }
          },
          xAxis: [
            {
              type: 'category',
              axisLabel: { interval: 0 },
              data: [
                '一月',
                '\n二月',
                '三月',
                '\n四月',
                '五月',
                '\n六月',
                '七月',
                '\n八月',
                '九月',
                '\n十月',
                '十一月',
                '\n十二月',
              ],
              splitLine: { show: false }
            }
          ],
          yAxis: [
            {
              type: 'value',
              name: 'Energy（kW）'
            }
          ],
          series: [
            { name: 'HVAC Actual [kW]', type: 'bar' },
            { name: 'Chiller Power [kW]', type: 'bar' },
            { name: 'Humidifier power', type: 'bar' },
            { name: 'HV light Power', type: 'bar' },
            { name: 'Power[kW]', type: 'bar' },
            { name: 'PV panels power [kW]', type: 'bar' },
            {
              name: '各类能源占比',
              type: 'pie',
              center: ['75%', '35%'],
              radius: '28%',
              z: 100
            }
          ]
        },
        options: [
          {
            title: { text: '2016能源消耗情况' },
            series: [
              { data: msum20161Data },
              { data: msum20162Data },
              { data: msum20163Data },
              { data: msum20164Data },
              { data: msum20165Data },
              { data: msum20166Data },
              {
                data: [
                  { name: 'HVAC Actual [kW]', value: msum20161Data },
                  { name: 'Chiller Power [kW]', value: msum20162Data },
                  { name: 'Humidifier power [kW]', value: msum20163Data },
                  { name: 'HV light Power [kW]', value: msum20164Data },
                  { name: 'Power[kW]', value: msum20165Data },
                  { name: 'PV panels power [kW]', value: msum20166Data }
                ]
              }
            ]
          },
          {
            title: { text: '2017能源消耗情况' },
            series: [
              { data: msum20171Data },
              { data: msum20172Data },
              { data: msum20173Data },
              { data: msum20174Data },
              { data: msum20175Data },
              { data: msum20176Data },
              {
                data: [
                  { name: 'HVAC Actual [kW]', value: msum20171Data },
                  { name: 'Chiller Power [kW]', value: msum20172Data },
                  { name: 'Humidifier power [kW]', value: msum20173Data },
                  { name: 'HV light Power [kW]', value: msum20174Data },
                  { name: 'Power[kW]', value: msum20175Data },
                  { name: 'PV panels power [kW]', value: msum20176Data }
                ]
              }
            ]
          },
          {
            title: { text: '2018能源消耗情况' },
            series: [
              { data: msum20181Data },
              { data: msum20182Data },
              { data: msum20183Data },
              { data: msum20184Data },
              { data: msum20185Data },
              { data: msum20186Data },
              {
                data: [
                  { name: 'HVAC Actual [kW]', value: msum20181Data },
                  { name: 'Chiller Power [kW]', value: msum20182Data },
                  { name: 'Humidifier power [kW]', value: msum20183Data },
                  { name: 'HV light Power [kW]', value: msum20184Data },
                  { name: 'Power[kW]', value: msum20185Data },
                  { name: 'PV panels power [kW]', value: msum20186Data }
                ]
              }
            ]
          },
          {
            title: { text: '2019能源消耗情况' },
            series: [
              { data: msum20191Data },
              { data: msum20192Data },
              { data: msum20193Data },
              { data: msum20194Data },
              { data: msum20195Data },
              { data: msum20196Data },
              {
                data: [
                  { name: 'HVAC Actual [kW]', value: msum20191Data },
                  { name: 'Chiller Power [kW]', value: msum20192Data },
                  { name: 'Humidifier power [kW]', value: msum20193Data },
                  { name: 'HV light Power [kW]', value: msum20194Data },
                  { name: 'Power[kW]', value: msum20195Data },
                  { name: 'PV panels power [kW]', value: msum20196Data }
                ]
              }
            ]
          },
          {
            title: { text: '2020能源消耗情况' },
            series: [
              { data: msum20201Data },
              { data: msum20202Data },
              { data: msum20203Data },
              { data: msum20204Data },
              { data: msum20205Data },
              { data: msum20206Data },
              {
                data: [
                  { name: 'HVAC Actual [kW]', value: msum20201Data },
                  { name: 'Chiller Power [kW]', value: msum20202Data },
                  { name: 'Humidifier power [kW]', value: msum20203Data },
                  { name: 'HV light Power [kW]', value: msum20204Data },
                  { name: 'Power[kW]', value: msum20205Data },
                  { name: 'PV panels power [kW]', value: msum20206Data }
                ]
              }
            ]
          },
          {
            title: { text: '2021能源消耗情况' },
            series: [
              { data: msum20211Data },
              { data: msum20212Data },
              { data: msum20213Data },
              { data: msum20214Data },
              { data: msum20215Data },
              { data: msum20216Data },
              {
                data: [
                  { name: 'HVAC Actual [kW]', value: msum20211Data },
                  { name: 'Chiller Power [kW]', value: msum20212Data },
                  { name: 'Humidifier power [kW]', value: msum20213Data },
                  { name: 'HV light Power [kW]', value: msum20214Data },
                  { name: 'Power[kW]', value: msum20215Data },
                  { name: 'PV panels power [kW]', value: msum20216Data }
                ]
              }
            ]
          },
          
        ]
      };

      option && myChart.setOption(option);
    }
  },
  mounted() {
    this.myEcharts1();
    this.myEcharts2();
    this.myEcharts3();
    this.myEcharts4();
    this.myEcharts5();
    this.myEcharts6();
  },

}
</script>
  
<style scoped>
.chart-container {
  display: flex;
  flex-direction: column;
  /* 设置flex方向为垂直 */
  width: 100%;
  /* 设置容器宽度为100% */
}

.chart {
  width: 100%;
  /* 设置图表宽度为100% */
  height: 800px;
  /* 设置固定的高度或者使用vh单位 */
}

.flex-container {
  display: flex;
}

.flex-container .chart {
  flex: 1;
  /* Flexbox 会使两个图表各占一半宽度 */
}
</style>

