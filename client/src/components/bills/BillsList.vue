<template>
    <div>
        <!-- To trzeba ladnie zrobic -->
        <b-spinner v-if="$store.state.getBillStatus == 0" variant="info"
        label="Spinning"></b-spinner>
        <p v-if="$store.state.getBillStatus == -1">Błąd ładowania</p>
        <b-card
        variant="info"
        class="my-2"
        border-variant="info"
        v-for="bill in $store.state.billsList" :key = bill.id>
            <h5>Nazwa kategorii: {{ bill.category_id }}</h5>
            <hr>
            <p v-show="bill.usage != 0">Zużycie: {{ bill.usage }}</p>
            <p v-show="bill.cash != 0">Koszt: {{ bill.cash }}</p>
            <p>Data: {{ bill.date }}</p>
            <p>Opis: {{ bill.description }}</p>
        </b-card>
    </div>
</template>

<script>
export default {
    name: 'BillsList',
    data() {
        return {
        };
    },
    mounted() {
        this.$store.dispatch('getBills');
    },
};

</script>

<style scoped>

</style>
