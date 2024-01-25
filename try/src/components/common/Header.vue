<template>
  <div class='header'>
    <el-header class="header-bar">
      <div class='title'>Building Energy consumption</div>
      <div class="dropdown-container">
        <el-dropdown class="dropdown-menu" @command="handleCategoryChange">
          <span class="el-dropdown-link">
            {{ selectedCategory }}
            <i class="el-icon-arrow-down el-icon--right"></i>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="1">HVAC Actual and Chiller Power</el-dropdown-item>
            <el-dropdown-item command="2">Humidifier power and HV light Power</el-dropdown-item>
            <el-dropdown-item command="3">Power and PV panels power and Battery system power</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
    </el-header>
  </div>
</template>

  
<script>
export default {
  name: 'Header',
  data() {
    return {
      selectedCategory: '选择能源种类', // 初始文本
    };
  },
  props: {
    currentYear: {
      type: String,
      required: true // currentYear 是必须的
    }
  }, // 接受从父组件传递的当前年份
  methods: {
    handleCategoryChange(moduleNumber) {
      this.$router.push({ path: `/home/${this.currentYear}/${moduleNumber}` });
      const categories = {
        '1': 'HVAC Actual and Chiller Power',
        '2': 'Humidifier power and HV light Power',
        '3': 'Power and PV panels power and Battery system power',
      };
      this.selectedCategory = categories[moduleNumber] || '选择能源种类';

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.title {
  width: 300px;
  font-size: 24px;
}
.dropdown-menu .el-dropdown-link {
  border: 1px solid #2c57bd; 
  padding: 10px 15px;
  border-radius: 4px; /* 圆角边框 */
  transition: border-color .2s; /* 边框颜色过渡效果 */
}

.dropdown-menu .el-dropdown-link:hover {
  border-color: #40ffd2; /* 鼠标悬浮时的边框颜色 */
}

.header-bar {
  background-color: rgba(192, 255, 220,0.8); /* 设置 header 背景色为粉色 */
  display: flex;
  justify-content: space-between; /* 两端对齐 */
  align-items: center;
  
}
</style>
  