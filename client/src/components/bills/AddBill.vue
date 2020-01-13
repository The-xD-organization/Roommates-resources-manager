<template>
    <b-container class="bill-form">
        <b-row align-h="center">
            <b-col>
        <b-card title="Dodaj rachunek"
        border-variant="info">
        <form>
            <!-- <b-form-input class="my-2 form-style"
                v-model="billData.category"
                placeholder="Kategoria"
            ></b-form-input> -->
            <b-form-select
                class="my-2 form-style"
                v-model="billData.category"
            >
                <option :value="null" disabled>Kategoria</option>
                <option
                    v-for="(category, index) in $store.state.categoriesList" :key="index"
                    :value="index"
                >
                    {{ category }}
                </option>
            </b-form-select>
            <b-form-input
                class="my-2 form-style"
                v-model="billData.usage"
                placeholder="Zużycie"
            ></b-form-input>
            <b-form-input
                class="my-2 form-style"
                v-model="billData.cash"
                placeholder="Koszt"
            ></b-form-input>
            <b-form-input
                class="my-2 form-style"
                v-model="billData.description"
                placeholder="Opis"
            ></b-form-input>
            <b-button
                class="my-2 add-bill-btn"
                @click="sendBill()"
                block
            >
                Wyślij
            </b-button>
        </form>
        <b-spinner
            v-if="$store.state.addNewBillStatus === 0"
            variant="info"
            label="Spinning">
        </b-spinner>
        <p v-else-if="$store.state.addNewBillStatus === 1">Wysłano</p>
        <p v-else-if="$store.state.addNewBillStatus === -1">Wysyłanie nie powiodło się</p>
        <p v-else-if="areInputsEmpty">Nie możesz dodać pustego rachunku</p>
        </b-card>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
export default {
    name: 'AddBill',
    data() {
        return {
            billData: {
                category: null,
                usage: null,
                cash: null,
                description: null,
            },
            areInputsEmpty: false,
        };
    },
    beforeDestroy() {
        this.$store.commit('setAddNewBillStatus', null);
    },
    methods: {
        sendBill() {
            if (this.billData.cash !== null
            || this.billData.usage !== null
            || this.billData.description !== null) {
                this.areInputsEmpty = false;
                this.$store.dispatch('addNewBill', this.billData);
            } else {
                this.areInputsEmpty = true;
            }
        },
    },
    mounted() {
        this.$store.dispatch('getBillCategories');
    },
};

</script>

<style scoped>
.bill-form{
    max-width: 400px;
    text-align: center;
    position: relative;
}
.add-bill-btn{
    background-color: #17a2b8;
}
.form-style{
    border-color: #17a2b8;
}
</style>
