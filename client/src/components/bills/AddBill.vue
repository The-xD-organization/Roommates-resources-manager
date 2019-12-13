<template>
    <div>
        <form>
            <!-- Kategorie zmienię na fajnego selecta -->
            <b-form-input
                v-model="billData.category"
                placeholder="Kategoria"
            ></b-form-input>
            <b-form-input
                v-model="billData.usage"
                placeholder="Zużycie"
            ></b-form-input>
            <b-form-input
                v-model="billData.cash"
                placeholder="Koszt"
            ></b-form-input>
            <b-form-input
                v-model="billData.description"
                placeholder="Opis"
            ></b-form-input>
            <b-button
                @click="sendBill()"
                variant="primary"
            >
                Wyślij
            </b-button>
        </form>
        <p v-if="$store.state.addNewBillStatus === 0">Wysyłanie...</p>
        <p v-else-if="$store.state.addNewBillStatus === 1">Wysłano</p>
        <p v-else-if="$store.state.addNewBillStatus === -1">Wysyłanie nie powiodło się</p>
    </div>
</template>

<script>
export default {
    name: 'AddBill',
    data() {
        return {
            billData: {
                category: '',
                usage: null,
                cash: null,
                description: '',
            },
        };
    },
    beforeDestroy() {
        this.$store.commit('setAddNewBillStatus', null);
    },
    methods: {
        sendBill() {
            this.$store.dispatch('addNewBill', this.billData);
        },
    },
};

</script>

<style scoped>

</style>
