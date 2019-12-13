<template>
    <login-layout>
        <body class="login-page">
            <div class="page-header clear-filter">
            <b-navbar  class="navbar-transparent" type="dark" toggleable="lg">
                <b-navbar-brand>
                    <router-link
                        class="navbar-brand pl-5"
                        to="/login">
                            RoomMates Manager
                        </router-link>
                </b-navbar-brand>
            </b-navbar>
        <div>
        <div class="content">
            <div class="container">
                <div class="col-lg-5 ml-auto mr-auto">
                        <b-card class="login">
                            <form @keydown.enter="login()">
                                <!-- nie wiem czego dokladnie uzywasz wiec dalem p
                                    ale zrob tak zeby to bylo ladne kolorwe itp-->
                                <p v-if="loginStatus === -1">
                                    Błąd logowania<br> {{ $store.state.errorMesage }}
                                </p>
                                <p v-if="loginStatus === 0">
                                    Logowanie...
                                </p>
                                <p v-if="inputErrors !== null">
                                    {{ inputErrors }}
                                </p>
                                <b-col>
                                <b-form-input class="input-style"
                                    v-model="credentials.username"
                                    type="email"
                                    placeholder="Wpisz login"
                                ></b-form-input>
                                </b-col>
                                <b-col>
                                <b-form-input class="input-style"
                                    v-model="credentials.password"
                                    type="password"
                                    placeholder="Wpisz hasło"
                                ></b-form-input>
                                </b-col>
                                <b-button class="btn-submit"
                                    @click="login()"
                                >
                                    Zaloguj się
                                </b-button>
                            </form>
                        </b-card>
                        </div>
                        </div>
                    </div>
                    <footer class="footer">
                    <b-container>
                        <b-row class="text-center">
                            <b-col>
                                <span >Copyright © The-xD-organization</span>
                            </b-col>
                        </b-row>
                    </b-container>
                    </footer>
                </div>
            </div>
        </body>
    </login-layout>
</template>

<script>
import Cookies from 'js-cookie';
import LoginLayout from '@/components/layouts/LoginLayout.vue';

export default {
    name: 'login',
    components: {
        LoginLayout,
    },
    data() {
        return {
            credentials: {
                username: '',
                password: '',
            },
            inputErrors: null,
        };
    },
    methods: {
        login() {
            if (this.credentials.username === '' && this.credentials.password === '') {
                this.inputErrors = 'Podaj nazwę użytkownika i hasło';
            } else if (this.credentials.username === '') {
                this.inputErrors = 'Podaj nazwę użytkownika';
            } else if (this.credentials.password === '') {
                this.inputErrors = 'Podaj hasło';
            } else {
                this.inputErrors = '';
                this.$store.dispatch('login', this.credentials);
            }
        },
    },
    computed: {
        loginStatus() {
            return this.$store.state.loginStatus;
        },
    },
    watch: {
        loginStatus(newValue) {
            if (newValue === 1) this.$router.replace('/');
        },
    },
    mounted() {
        if (Cookies.get('access_token') !== undefined) this.$router.replace('/');
    },
};
</script>
<style scoped>
.navbar-transparent{
    background-color: transparent!important;
    box-shadow: none;
    color: #ffffff;
    padding-top:20px;
}
.content{
    margin-top: 12%;
}
.container{
    height: 100%;
    text-align: center;
    position: relative;
}
.clear-filter{
    background: linear-gradient(0deg,#ccffcc,#17a2b8)
}
.login{
    border:0;
    display: inline-block;
    position: relative;
    width: 100%;
    margin-bottom: 30px;
    padding-bottom: .7rem;
    max-width: 400px;
    background: transparent;
    box-shadow: none;
}
.input-style{
    margin-bottom: 40px;
    position: relative;
    align-items: stretch;
    width: 100%;
    background-color: #ffffff54;
    border:0;
    border-radius: 30px;
}
.btn-submit{
    border:0;
    width: 95%;
    border-radius: 30px;
    background-color: #17a2b8;
    padding: 10px 48px;
    margin: 5px 1px;
}
.page-header{
    min-height: 100vh;
    max-height: 999px;
    position: relative;
    overflow: hidden;
}
.footer{
 position: absolute;;
 bottom: 0;
 width: 100%;
 height: 40px;
}
</style>
