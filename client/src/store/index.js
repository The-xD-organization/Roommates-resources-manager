import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import Cookies from 'js-cookie';

Vue.use(Vuex);
export default new Vuex.Store({
    state: {
        isAuthenticated: false,
        loginStatus: null, // -1 error, 0 pending, 1 success
        errorMesage: null,
    },
    mutations: {
        AuthenticationStatus(state, payload) {
            state.isAuthenticated = payload;
        },
        setLoginStatus(state, payload) {
            state.loginStatus = payload;
        },
        setErrorMesage(state, payload) {
            state.errorMesage = payload;
        },
    },
    actions: {
        login({ commit }, credentials) {
            commit('setLoginStatus', 0);
            axios.post(`${process.env.VUE_APP_API_URL}/auth`, {
                username: credentials.username,
                password: credentials.password,
            })
                .then((response) => {
                    commit('AuthenticationStatus', true);
                    Cookies.set('access_token', response.data.access_token);
                    commit('setLoginStatus', 1);
                })
                .catch((error) => {
                    commit('setErrorMesage', error);
                    commit('setLoginStatus', -1);
                    commit('AuthenticationStatus', false);
                });
        },
    },
    modules: {
    },
    getters: {
    },
});
