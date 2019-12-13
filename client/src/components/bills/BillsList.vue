<template>
    <div>
        <!-- To trzeba ladnie zrobic -->
        <p v-if="$store.state.getBillStatus == 0">Ładownie...</p>
        <p v-if="$store.state.getBillStatus == -1">Błąd ładowania</p>
        <div v-for="bill in $store.state.billsList" :key = bill.id>
            <p>Nazwa kategorii: {{ bill.category_id }}</p>
            <p v-show="bill.usage != 0">Zużycie: {{ bill.usage }}</p>
            <p v-show="bill.cash != 0">Koszt: {{ bill.cash }}</p>
            <p>Data: {{ bill.date }}</p>
            <p>Opis: {{ bill.description }}</p>
            <hr>
        </div>
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
