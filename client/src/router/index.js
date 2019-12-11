import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'home',
        component: () => import('../views/Home.vue'),
    },
    {
        path: '/about',
        name: 'about',
        component: () => import('../views/About.vue'),
    },
    {
        path: '/login',
        name: 'login',
        component: () => import('../views/Login.vue'),
    },
    {
        path: '/bills',
        name: 'lobills',
        component: () => import('../views/Bills.vue'),
    },
    {
        path: '/tasks',
        name: 'tasks',
        component: () => import('../views/Tasks.vue'),
    },
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
});

export default router;
