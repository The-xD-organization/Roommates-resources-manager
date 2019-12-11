<template>
    <default-layout>
        <b-container fluid class="my-2">
            <b-row class="justify-content-sm-center">
                <b-col cols="12 my-1" md="2">
                    <b-card>
                    </b-card>
                </b-col>
                <b-col cols="12 my-1" md="6">
                    <b-card></b-card>
                </b-col>
                <b-col cols="12 my-1" md="2">
                    <b-card>
                    </b-card>
                </b-col>
            </b-row>
        </b-container>
        <button @click="testAuth()">Test Auth</button>
    </default-layout>
</template>

<script>
import axios from 'axios';
import DefaultLayout from '@/components/layouts/DefaultLayout.vue';


export default {
    name: 'home',
    components: {
        DefaultLayout,
    },
    data() {
        return {
        };
    },

    methods: {
        testAuth() {
            axios.post(`${process.env.VUE_APP_API_URL}/auth`, {
                username: 'bob',
                password: '1234',
            })
                .then((response) => {
                    console.log(response);
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },
};
</script>
