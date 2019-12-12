import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import Cookies from 'js-cookie';

Vue.use(Vuex);
export default new Vuex.Store({
    state: {
        isAuthenticated: false,
    },
    mutations: {
        AuthenticationStatus(state, payload) {
            state.isAuthenticated = payload;
        },
    },
    actions: {
        login({ commit }, credentials) {
            console.log(credentials);
            axios.post(`${process.env.VUE_APP_API_URL}/auth`, {
                username: credentials.username,
                password: credentials.password,
            })
                .then((response) => {
                    commit('AuthenticationStatus', true);
                    Cookies.set('access_token', response.data.access_token);
                })
                .catch((error) => {
                    console.log(error);
                    commit('AuthenticationStatus', false);
                });
        },
    },
    modules: {
    },
    getters: {
    },
});
