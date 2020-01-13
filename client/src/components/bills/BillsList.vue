<template>
    <div>
        <b-spinner v-if="$store.state.getBillStatus == 0" variant="info"
        label="Spinning"></b-spinner>
        <p v-if="$store.state.getBillStatus == -1">Błąd ładowania</p>
        <div
            v-for="bill in $store.state.billsList" :key = bill.id
        >
            <ShowBill
                v-bind:bill="bill"
            />
        </div>
    </div>
</template>

<script>
import ShowBill from '@/components/bills/ShowBill.vue';

export default {
    name: 'BillsList',
    components: {
        ShowBill,
    },
    data() {
        return {
        };
    },
    mounted() {
        this.$store.dispatch('getBillCategories');
        this.$store.dispatch('getBills');
    },
};

</script>

<style scoped>

</style>
