<template>
    <login-layout>
        <b-container fluid>
            <b-row class="my-1">
                 <b-col class="col-sm-9 col-md-7 col-lg-4 mx-auto">
                    <h3>Wylogowaliśmy Cię</h3>
                    <p>Przeniesiemy Cię do strony głównej za {{ sec }}...</p>
                    <router-link to="/">
                            Wróć do strony głownej
                    </router-link>
                 </b-col>
            </b-row>
        </b-container>
    </login-layout>
</template>

<script>
import LoginLayout from '@/components/layouts/LoginLayout.vue';

export default {
    name: 'logout',
    components: {
        LoginLayout,
    },
    data() {
        return {
            sec: 5,
        };
    },
    methods: {
        countdown() {
            const timer = setInterval(() => {
                this.sec = this.sec - 1;
                if (this.sec === 0) {
                    clearInterval(timer);
                    this.$router.replace('/');
                }
            }, 1000);
        },
    },
    mounted() {
        this.$store.dispatch('logout');
        this.countdown();
    },
};
</script>
