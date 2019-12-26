<template>
    <div>
        <p v-show="bill.usage != 0">Zużycie: {{ bill.usage }}</p>
        <p v-show="bill.cash != 0">Koszt: {{ bill.cash }} zł</p>
        <p>Data: {{ bill.date }}</p>
        <p v-show="bill.description!=''">Opis: {{ bill.description }}</p>
        <p @click="showPayerAccount = true">
            Numer konta
            <span v-if="showPayerAccount === true">: {{ bill.payer_account }} lorem ipsum</span>
        </p>
    </div>
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
        };
    },
};

</script>

<style scoped>

</style>
