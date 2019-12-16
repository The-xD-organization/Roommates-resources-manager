<template>
    <login-layout>
        <h3>Wylogowaliśmy Cię</h3>
        <p>Przeniesiemy Cię do strony głównej za {{ sec }}...</p>
        <router-link to="/">
                Wróć do strony głownej
        </router-link>
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
