import { useAuthStore } from './stores/auth'
import {createRouter, createWebHistory} from 'vue-router'
import  Login  from './components/Login.vue'
import  Home from './components/Home.vue'

const routes = [
    {path: '/', component: Home},
    {path: '/home', component: Home},
    {path: '/login', component: Login},
]

export const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach((to) => {
    const authStore = useAuthStore()
    if (to.path != '/login' && !authStore.isAuthenticated) return '/login'
})