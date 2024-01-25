<template>
  <div class="chart-container">
    <div id="chart1" class="chart"></div>
    <div id="chart2" class="chart"></div>
    <div class="flex-container">
      <div id="chart3" class="chart"></div>
      <div id="chart4" class="chart"></div>
    </div>
  </div>
</template>
  
<script>
import * as echarts from 'echarts';
import Data_2016_1 from './2017_1da.json'; // 引入JSON数据
import ecStat from 'echarts-stat';
import anotherData from './2017_1mv.json';
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

    }

  },
  mounted() {
    this.myEcharts1();
    this.myEcharts2();
    this.myEcharts3();
    this.myEcharts4();
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
  height: 700px;
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