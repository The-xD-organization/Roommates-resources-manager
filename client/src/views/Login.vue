<template>
    <login-layout>
        <form @keydown.enter="login()">
            <p v-if="loginStatus === -1">
                Błąd logowania<br> {{ $store.state.errorMesage }}
            </p>
            <b-spinner v-if="loginStatus === 0" variant="info" label="Spinning"></b-spinner>
            <b-col>
            <b-form-input class="input-style"
                v-model="credentials.username"
                type="email"
                :state="nameState"
                aria-describedby="input-live-help input-live-feedback"
                placeholder="Wpisz login"
            ></b-form-input>
            <b-form-invalid-feedback class="margin" id="input-live-feedback">
            Wprowadź login
            </b-form-invalid-feedback>
            <b-form-valid-feedback class="margin" id="input-live-help">
                <br>
            </b-form-valid-feedback>
            </b-col>
            <b-col>
            <b-form-input class="input-style"
                v-model="credentials.password"
                type="password"
                :state="passwordState"
                aria-describedby="input-live-help2 input-live-feedback2"
                placeholder="Wpisz hasło"
            ></b-form-input>
            <b-form-invalid-feedback class="margin" id="input-live-feedback2">
            Wprowadź hasło
            </b-form-invalid-feedback>
            <b-form-valid-feedback class="margin" id="input-live-help2">
                <br>
            </b-form-valid-feedback>
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
        nameState() {
            return this.credentials.username.length > 0;
        },
        passwordState() {
            return this.credentials.password.length > 0;
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
