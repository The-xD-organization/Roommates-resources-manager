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
        getBillStatus: null,
        billsList: null,
        addNewBillStatus: null,
    },
    mutations: {
        setLoginStatus(state, payload) {
            state.loginStatus = payload;
        },
        setErrorMessage(state, payload) {
            state.errorMesage = payload;
        },
        setGetBillStatus(state, payload) {
            state.getBillStatus = payload;
        },
        setBillsList(state, payload) {
            state.billsList = payload;
        },
        setAddNewBillStatus(state, payload) {
            state.addNewBillStatus = payload;
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
                    Cookies.set('access_token', response.data.access_token);
                    commit('setLoginStatus', 1);
                })
                .catch((error) => {
                    commit('setErrorMessage', error);
                    commit('setLoginStatus', -1);
                });
        },
        logout() {
            Cookies.remove('access_token');
        },
        getBills({ commit }) {
            commit('setGetBillStatus', 0);
            axios.get(`${process.env.VUE_APP_API_URL}/bills`, {
                headers: { Authorization: `JWT ${Cookies.get('access_token')}` },
            })
                .then((response) => {
                    commit('setBillsList', response.data.bills);
                    commit('setGetBillStatus', 1);
                })
                .catch((error) => {
                    commit('setErrorMessage', error);
                    commit('setGetBillStatus', -1);
                });
        },
        addNewBill({ commit }, billData) {
            commit('setAddNewBillStatus', 0);
            axios.post(`${process.env.VUE_APP_API_URL}/bill/${billData.category}`, {
                description: billData.description,
                usage: billData.usage,
                cash: billData.cash,
            },
            {
                headers: {
                    Authorization: `JWT ${Cookies.get('access_token')}`,
                    'Content-Type': 'application/json',
                },
            })
                .then(() => {
                    commit('setAddNewBillStatus', 1);
                })
                .catch((error) => {
                    commit('setErrorMessage', error);
                    commit('setGetBillStatus', -1);
                });
        },
    },
    modules: {
    },
    getters: {
    },
});
