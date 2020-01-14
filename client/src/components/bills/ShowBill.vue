<template>
    <b-card
        variant="info"
        class="my-2"
        border-variant="info"
        bg-variant="danger"
        :class="{payed: bill.is_payed||payClicked}"
    >
        <h5>{{ $store.state.categoriesList[bill.category_id] }}</h5>
        <b-button
            variant="outline-dark"
            class="mt-1"
            v-show="!bill.is_payed"
            @click="payBill()"
        >
           Zapłać
        </b-button>
        <hr>
        <p v-show="bill.usage != 0">Zużycie: {{ bill.usage }}</p>
        <p v-show="bill.cash != 0">Koszt: {{ bill.cash }} zł</p>
        <p>Data: {{ bill.date }}</p>
        <p v-show="bill.description!=''">Opis: {{ bill.description }}</p>
        <p @click="showPayerAccount = true">
            <span class="acc_number">Numer konta</span>
            <span v-if="showPayerAccount === true">: {{ bill.payer_account }}</span>
        </p>
    </b-card>
</template>

<script>
export default {
    name: 'ShowBill',
    props: {
        bill: Object,
    },
    data() {
        return {
            showPayerAccount: false,
            payClicked: false,
        };
    },
    methods: {
        payBill() {
            this.$store.dispatch('payBill', this.bill.id);
            this.payClicked = true;
        },
    },
};

</script>

<style scoped>
.acc_number{
    color: #17a2b8;
}
.acc_number:hover{
    cursor: pointer;
}
.payed{
    background-color:aquamarine!important;
}
</style>
