<template>
    <default-layout>
        Numer bankowy:
        <b-form-input
            class="my-2 form-style"
            v-model="num"
        ></b-form-input>
         <b-button
            class="my-2 add-bill-btn"
            @click="sendProfileData()"
            block
        >
            Wyślij
        </b-button>
        <b-spinner
            v-if="$store.state.changeBankAccStatus === 0"
            variant="info"
            label="Spinning">
        </b-spinner>
        <p v-else-if="$store.state.changeBankAccStatus === 1">Wysłano</p>
        <p v-else-if="$store.state.changeBankAccStatus === -1">
            Wysyłanie nie powiodło się {{ $store.state.errorMesage }}
        </p>
    </default-layout>
</template>

<script>
import DefaultLayout from '@/components/layouts/DefaultLayout.vue';

export default {
    name: 'profile',
    components: {
        DefaultLayout,
    },
    data() {
        return {
            num: null,
        };
    },
    mounted() {
        this.$store.dispatch('getUserData');
    },
    beforeDestroy() {
        this.$store.commit('setChangeBankAccStatus', null);
    },
    computed: {
        bankAccNumber() {
            return this.$store.state.userData;
        },
    },
    watch: {
        bankAccNumber(newValue) {
            this.num = newValue.bank_account;
        },
    },
    methods: {
        sendProfileData() {
            this.$store.dispatch('changeBankAcc', this.num);
        },
    },
};
</script>
<style scoped>
</style>
