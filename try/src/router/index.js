// router/index.js
import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

// 动态生成年份路由
const createYearRoutes = () => {
  const routes = [];
  for (let year = 2016; year <= 2021; year++) {
    for (let module = 1; module <= 3; module++) { // 假设每年有3个模块
      routes.push({
        path: `${year}/${module}`,
        name: `data-${year}-${module}`,
        component: () => import(`@/components/energy_data/${year}_${module}.vue`),
      });
    }
  }
  return routes;
};

export default new Router({
  mode: 'history',
  routes: [
    // {
    //   path: '/',
    //   name: 'Login',
    //   component: () => import('@/components/Login')
    // },
    {
      path:'/',
      redirect:'/home',
      hidden:true,
    },

    {
      path: '/home',
      component: () => import('@/components/Home'),
      children: createYearRoutes(),
    },
    {
      path: '*',
      name: 'NotFound',
      component: () => import('@/components/NotFound'),
    },
  ],
});

