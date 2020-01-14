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
        categoriesList: [],
        payBillStatus: null,

        tasksList: null,
        getTaskStatus: null,
        addNewTaskStatus: null,
        doTaskStatus: null,

        userData: null,
        userDataStatus: null,
        changeBankAccStatus: null,

        homeBill: null,
        homeTask: null,
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
        setBillCategories(state, payload) {
            Object.keys(payload).forEach((key) => {
                state.categoriesList[payload[key].id] = payload[key].name;
            });
        },
        setPayBIllStatus(state, payload) {
            state.payBillStatus = payload;
        },
        setGetTaskStatus(state, payload) {
            state.getTaskStatus = payload;
        },
        setTasksList(state, payload) {
            state.tasksList = payload;
        },
        setAddNewTaskStatus(state, payload) {
            state.addNewTaskStatus = payload;
        },
        setUserData(state, payload) {
            state.userData = payload;
        },
        setUserDataStatus(state, payload) {
            state.userDataStatus = payload;
        },
        setChangeBankAccStatus(state, payload) {
            state.changeBankAccStatus = payload;
        },
        setHomeBill(state, payload) {
            state.homeBill = payload;
        },
        setHomeTask(state, payload) {
            state.homeTask = payload;
        },
        setDoTaskStatus(state, payload) {
            state.doTaskStatus = payload;
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
            axios.post(`${process.env.VUE_APP_API_URL}/bill`, {
                category_id: billData.category,
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
                    commit('setAddNewBillStatus', -1);
                });
        },
        getBillCategories({ commit }) {
            axios.get(`${process.env.VUE_APP_API_URL}/bill_categories`, {
                headers: { Authorization: `JWT ${Cookies.get('access_token')}` },
            })
                .then((response) => {
                    commit('setBillCategories', response.data.bill_categories);
                })
                .catch((error) => {
                    commit('setErrorMessage', error);
                });
        },
        payBill({ commit }, id) {
            commit('setPayBIllStatus', 0);
            axios.put(`${process.env.VUE_APP_API_URL}/bill/${id}`, {
                is_payed: true,
            },
            {
                headers: {
                    Authorization: `JWT ${Cookies.get('access_token')}`,
                    'Content-Type': 'application/json',
                },
            })
                .then(() => {
                    commit('setPayBIllStatus', 1);
                })
                .catch((error) => {
                    commit('setErrorMessage', error);
                    commit('setPayBIllStatus', -1);
                });
        },

        getTasks({ commit }) {
            commit('setGetTaskStatus', 0);
            axios.get(`${process.env.VUE_APP_API_URL}/tasks`, {
                headers: { Authorization: `JWT ${Cookies.get('access_token')}` },
            })
                .then((response) => {
                    commit('setTasksList', response.data.tasks);
                    commit('setGetTaskStatus', 1);
                })
                .catch((error) => {
                    commit('setErrorMessage', error);
                    commit('setGetTaskStatus', -1);
                });
        },
        addNewTask({ commit }, taskData) {
            commit('setAddNewTaskStatus', 0);
            axios.post(`${process.env.VUE_APP_API_URL}/task`, {
                description: taskData.description,
            },
            {
                headers: {
                    Authorization: `JWT ${Cookies.get('access_token')}`,
                    'Content-Type': 'application/json',
                },
            })
                .then(() => {
                    commit('setAddNewTaskStatus', 1);
                })
                .catch((error) => {
                    commit('setErrorMessage', error);
                    commit('setAddNewTaskStatus', -1);
                });
        },

        changeBankAcc({ commit }, newNumber) {
            commit('setChangeBankAccStatus', 0);
            axios.put(`${process.env.VUE_APP_API_URL}/user`, {
                bank_account: newNumber,
            },
            {
                headers: {
                    Authorization: `JWT ${Cookies.get('access_token')}`,
                    'Content-Type': 'application/json',
                },
            })
                .then(() => {
                    commit('setChangeBankAccStatus', 1);
                })
                .catch((error) => {
                    commit('setErrorMessage', error);
                    commit('setChangeBankAccStatus', -1);
                });
        },
        getUserData({ commit }) {
            commit('setUserDataStatus', 0);
            axios.get(`${process.env.VUE_APP_API_URL}/user`, {
                headers: { Authorization: `JWT ${Cookies.get('access_token')}` },
            })
                .then((response) => {
                    commit('setUserData', response.data);
                    commit('setUserDataStatus', 1);
                })
                .catch((error) => {
                    commit('setErrorMessage', error);
                    commit('setUserDataStatus', -1);
                });
        },

        getHomeBill({ commit }) {
            commit('setGetBillStatus', 0);
            axios.get(`${process.env.VUE_APP_API_URL}/latest_bill`, {
                headers: { Authorization: `JWT ${Cookies.get('access_token')}` },
            })
                .then((response) => {
                    commit('setHomeBill', response.data);
                    commit('setGetBillStatus', 1);
                })
                .catch((error) => {
                    commit('setErrorMessage', error);
                    commit('setGetBillStatus', -1);
                });
        },
        getHomeTask({ commit }) {
            commit('setGetTaskStatus', 0);
            axios.get(`${process.env.VUE_APP_API_URL}/my_tasks`, {
                headers: { Authorization: `JWT ${Cookies.get('access_token')}` },
            })
                .then((response) => {
                    commit('setHomeTask', response.data.tasks);
                    commit('setGetTaskStatus', 1);
                })
                .catch((error) => {
                    commit('setErrorMessage', error);
                    commit('setGetTaskStatus', -1);
                });
        },
        doTask({ commit }, id) {
            commit('setDoTaskStatus', 0);
            axios.put(`${process.env.VUE_APP_API_URL}/task/${id}`, {
                is_done: true,
            },
            {
                headers: {
                    Authorization: `JWT ${Cookies.get('access_token')}`,
                    'Content-Type': 'application/json',
                },
            })
                .then(() => {
                    commit('setDoTaskStatus', 1);
                })
                .catch((error) => {
                    commit('setErrorMessage', error);
                    commit('setDoTaskStatus', -1);
                });
        },
        asigneeToTask({ commit }, id, name) {
            commit('setDoTaskStatus', 0);
            axios.put(`${process.env.VUE_APP_API_URL}/task/${id}`, {
                assignee_name: name,
            },
            {
                headers: {
                    Authorization: `JWT ${Cookies.get('access_token')}`,
                    'Content-Type': 'application/json',
                },
            })
                .then(() => {
                    commit('setDoTaskStatus', 1);
                })
                .catch((error) => {
                    commit('setErrorMessage', error);
                    commit('setDoTaskStatus', -1);
                });
        },
    },
    modules: {
    },
    getters: {
    },
});
