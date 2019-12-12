import Vue from 'vue';
import VueRouter from 'vue-router';
import Cookies from 'js-cookie';

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'home',
        component: () => import('../views/Home.vue'),
        meta: {
            title: 'Strona główna',
        },
    },
    {
        path: '/about',
        name: 'about',
        component: () => import('../views/About.vue'),
        meta: {
            title: 'O nas',
        },
    },
    {
        path: '/login',
        name: 'login',
        component: () => import('../views/Login.vue'),
        meta: {
            title: 'Logowanie',
        },
    },
    {
        path: '/logout',
        name: 'logout',
        component: () => import('../views/Logout.vue'),
        meta: {
            title: 'Wylogowano',
        },
    },
    {
        path: '/bills',
        name: 'bills',
        component: () => import('../views/Bills.vue'),
        meta: {
            title: 'Rachunki',
        },
    },
    {
        path: '/tasks',
        name: 'tasks',
        component: () => import('../views/Tasks.vue'),
        meta: {
            title: 'Zadania',
        },
    },
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
});

router.beforeEach((to, from, next) => {
    document.title = `${to.meta.title} | Roommates Resources Manager`;
    const publicPages = ['/login'];
    const authRequired = !publicPages.includes(to.path);
    if (authRequired && Cookies.get('access_token') === undefined) next('/login');
    else next();
});
export default router;
