<template>
    <login-layout>
        <b-container fluid>
            <b-row class="my-1">
                 <b-col class="col-sm-9 col-md-7 col-lg-4 mx-auto">
                     <b-card title="Logowanie">
                        <form>
                            <!-- nie wiem czego dokladnie uzywasz wiec dalem p
                                ale zrob tak zeby to bylo ladne kolorwe itp-->
                            <p v-if="loginStatus === -1">
                                Błąd logowania<br> {{ $store.state.errorMesage }}
                            </p>
                            <p v-if="loginStatus === 0">
                                Logowanie...
                            </p>
                            <b-col class="my-2">
                            <b-form-input
                                v-model="credentials.username"
                                type="email"
                                placeholder="Wpisz e-mail"
                            ></b-form-input>
                            </b-col>
                            <b-col class="my-2">
                            <b-form-input
                                v-model="credentials.password"
                                type="password"
                                placeholder="Wpisz hasło"
                            ></b-form-input>
                            </b-col>
                            <b-button @click="login()" variant="primary">Zaloguj się</b-button>
                        </form>
                     </b-card>
                 </b-col>
            </b-row>
        </b-container>
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
        };
    },
    methods: {
        login() {
            this.$store.dispatch('login', this.credentials);
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
