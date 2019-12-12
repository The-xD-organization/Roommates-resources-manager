import Vue from 'vue';
import VueRouter from 'vue-router';
import Cookies from 'js-cookie';

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
        name: 'bills',
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

router.beforeEach((to, from, next) => {
    const publicPages = ['/login'];
    const authRequired = !publicPages.includes(to.path);
    if (authRequired && Cookies.get('access_token') === undefined) next('/login');
    else next();
});
export default router;
