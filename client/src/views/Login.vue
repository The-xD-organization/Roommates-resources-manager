<template>
    <login-layout>
        <form @keydown.enter="login()">
            <p v-if="loginStatus === -1">
            </p>
            <b-modal id="modal-1" title="Błąd logowania" ok-only>
                <p class="my-4">Wprowadź login i hasło</p>
            </b-modal>
            <b-modal id="modal-2" title="Błąd logowania" ok-only>
                <p class="my-4">Wprowadź login</p>
            </b-modal>
            <b-modal id="modal-3" title="Błąd logowania" ok-only>
                <p class="my-4">Wprowadź hasło</p>
            </b-modal>
            <b-modal id="modal-4" title="Błąd logowania" ok-only>
                <p class="my-4">safdasd</p>
            </b-modal>
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
                this.$bvModal.show('modal-1');
            } else if (this.credentials.username === '') {
                this.$bvModal.show('modal-2');
            } else if (this.credentials.password === '') {
                this.$bvModal.show('modal-3');
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
