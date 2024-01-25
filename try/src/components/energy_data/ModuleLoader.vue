<!-- ModuleLoader.vue -->
<template>
    <component :is="currentComponent" />
  </template>
  
  <script>
  export default {
    computed: {
      currentComponent() {
        const year = this.$route.params.year;
        const module = this.$route.params.module || '1';
        return () => import(`@/components/energy_data/${year}_${module}.vue`)
          .catch(error => {
            // 错误处理，例如跳转到404页面
            console.error(error);
            this.$router.replace({ name: 'NotFound' });
          });
      }
    }
  }
  </script>
  
  