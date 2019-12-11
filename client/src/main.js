import BootstrapVue from 'bootstrap-vue';
import './registerServiceWorker';
import Vue from 'vue';
import VueCookie from 'vue-cookie';
import App from './App.vue';
import router from './router';
import store from './store';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

Vue.use(VueCookie);
Vue.use(BootstrapVue);

Vue.config.productionTip = false;

new Vue({
    router,
    store,
    render: h => h(App),
}).$mount('#app');
