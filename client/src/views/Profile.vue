<template>
    <default-layout>
        <b-container class="mt-2">
            <b-card
            variant="info"
            title="Numer bankowy:"
            class="my-2"
            border-variant="info">
            <b-form-input
                class="my-2 form-style"
                v-model="num"
            ></b-form-input>
            <b-button
                class="my-2 btn"
                @click="sendProfileData()"
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
            </b-card>
        </b-container>
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
.btn{
    background-color:white;
    border-color: #17a2b8;
    color:#17a2b8;
}
.btn:hover{
    background-color: #17a2b8;
    color:white;
}
</style>
