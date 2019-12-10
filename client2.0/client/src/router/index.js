import Vue from 'vue'
import VueRouter from 'vue-router'
// import home from '../components/home.vue'
import Index from '../components/Index.vue'
import Login from "../views/Login.vue"
import newhome from "../views/newhome";
import chart1 from "../views/chart1";
import chart2 from "../views/chart2";
import chart3bmap from "../views/chart3bmap";
import chart4 from "../views/chart4";
import user from "../views/user";
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'login',
    component: Login
  },

  // {
  //   path: '/admin',
  //   name: 'admin',
  //   component: home,
  //   children:[
  //     {path: 'index',name: 'index', component: Index},
  //   ]
  // }
  // {
  //   path: '/',
  //   name: 'index',
  //   component: Index
  // },
  //     {
  //   path: '/',
  //   name: 'chart4',
  //   component: chart4
  // },
    {
      path: '/com',
      name: 'newhome',
      component: newhome,
      children: [
        {path: '/Index', name: 'Index', component:  Index},
        {path: '/chart1', name: 'chart1', component:  chart1},
        {path: '/chart1', name: 'chart1', component:  chart1},
        {path: '/chart2', name: 'chart2', component:  chart2},
         {path: '/chart3bmap', name: 'chart3', component:  chart3bmap},
         {path: '/chart4', name: 'chart4', component:  chart4},
         {path: '/user', name: 'user', component:  user},

      ]
    },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  let login = localStorage.getItem("login");
  if (login) {
    if (to.name == 'login') {
      next({ name: 'newhome' });
    } else {
      next();
    }
  } else {
    if (to.name == 'login') {
      next();
    } else {
      next({ name: 'login' });
    }
  }
});

export default router
