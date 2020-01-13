<template>
    <div>
        <b-spinner
            v-if="$store.state.getBillStatus == 0"
            variant="info"
            label="Spinning"
        ></b-spinner>
        <p v-if="$store.state.getBillStatus == -1">Błąd ładowania</p>
        <div v-else>
            Wyświetlaj:
            <input type="checkbox" id="not-paid" value="true" v-model="notPaid">
            <label for="not-paid">Niezapłacone</label>
            <input type="checkbox" id="paid" value="true" v-model="paid">
            <label for="paid">Zapłacone</label>
            <div
                v-for="bill in $store.state.billsList" :key = bill.id
            >
                <ShowBill
                    v-if="(paid == bill.is_payed || notPaid == !bill.is_payed)
                        && !(notPaid == false && paid == false)"
                    v-bind:bill="bill"
                />
            </div>
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
            notPaid: true,
            paid: true,
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
