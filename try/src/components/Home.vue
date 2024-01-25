<template>
  <div class="home">
    <h1>{{ msg }}</h1>
    <hr>
    <Header :currentYear="activeIndex.split('/')[1]"></Header> <!-- 传递当前年份到 Header -->
    <el-container class='content'>
      <el-aside width="200px">
        <el-menu 
          :default-active="activeIndex" 
          class="el-menu-vertical-demo" 
          background-color="#39C5BB" 
          text-color="#fff"
          active-text-color="#ffd04b" 
          @select="handleSelect"
        >
          <!-- 折叠 Years 菜单 -->
          <el-submenu index="years">
            <template slot="title">
              <i class="el-icon-time"></i>
              <span>Years</span>
            </template>
            <el-menu-item index="years/2016">2016</el-menu-item>
            <el-menu-item index="years/2017">2017</el-menu-item>
            <el-menu-item index="years/2018">2018</el-menu-item>
            <el-menu-item index="years/2019">2019</el-menu-item>
            <el-menu-item index="years/2020">2020</el-menu-item>
            <el-menu-item index="years/2021">2021</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from './common/Header';
import Footer from './common/Footer';

export default {
  components: {
    Header,
    Footer
  },
  data() {
    return {
      msg: 'Welcome to Your Vue.js App',
      // Set default active index to "years" to reflect the submenu for years
      activeIndex: 'years/2021', // 默认情况下选中当前年份
    };
  },
  methods: {
    handleSelect(index) {
      // Update the active index and navigate to the corresponding route
      this.activeIndex = index;
      if (index.startsWith('years/')) {
        const year = index.split('/')[1];
        this.$router.push({ path: `/home/${year}/1` });
      }
    }
  },
  created() {
    // Set the active index based on the current route
    const year = this.$route.params.year || new Date().getFullYear().toString();
    this.activeIndex = `years/${year}`;
  }
};
</script>

<style scoped>
.home .el-aside {
  height: 100%;
}

.home .content {
  position: absolute;
  width: 100%;
  top: 94px;
  bottom: 0;
}

.home .el-aside .el-menu {
  height: 100%;
}

.home .el-aside .el-submenu {
  min-width: 0;
}

.home .el-aside .el-menu-item {
  min-width: 0;
}
.home >>> .el-menu {
  background-color: rgba(57, 197, 187, 0.5) !important;
}
</style>
