<template>
    <login-layout>
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
