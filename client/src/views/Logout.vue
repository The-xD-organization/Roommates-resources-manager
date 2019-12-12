<template>
    <login-layout>
        <b-container fluid>
            <b-row class="my-1">
                 <b-col class="col-sm-9 col-md-7 col-lg-4 mx-auto">
                    <h3>Wylogowaliśmy Cię</h3>
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
        };
    },
    methods: {
    },
    mounted() {
        this.$store.dispatch('logout');
    },
};
</script>
