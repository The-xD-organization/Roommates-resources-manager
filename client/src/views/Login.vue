<template>
    <login-layout>
        <b-container fluid>
            <b-row class="my-1">
                 <b-col class="col-sm-9 col-md-7 col-lg-4 mx-auto">
                     <b-card title="Logowanie">
                        <form>
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
    mounted() {
        if (Cookies.get('access_token') !== undefined) this.$router.replace('/');
    },
};
</script>
