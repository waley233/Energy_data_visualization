<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
@import url('./assets/css/reset');

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #02101d;
}
body {
  position: relative;
  margin: 0; /* 确保没有默认的边距 */
  height: 100vh; /* 如果需要，可以设置页面的高度 */
  overflow: hidden; /* 如果内容超出视窗，隐藏滚动条 */
}

body::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url('./illust_99302008_20240103_183427.jpg');
  background-size: cover; /* 或者 'contain' 或 '50% 50%' 等 */
  background-repeat: no-repeat;
  background-position: center center;
  opacity: 0.2; /* 调整这个值来设置透明度 */
  z-index: -1; /* 确保伪元素在内容之下 */
} 
</style>
