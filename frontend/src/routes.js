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