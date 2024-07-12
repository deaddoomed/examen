import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegistrarView from '../views/RegistrarView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/login',
    name: 'login',
    component: HomeView
  },

  {
    path: '/registrar',
    name: 'registrar',
    component: RegistrarView
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})


export default router
