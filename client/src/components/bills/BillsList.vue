<template>
    <div>
        <b-spinner
            v-if="$store.state.getBillStatus == 0"
            variant="info"
            label="Spinning"
        ></b-spinner>
        <p v-if="$store.state.getBillStatus == -1">Błąd ładowania</p>
        <div v-else>
            <h5>Wyświetlaj:</h5>
            <label class="container">Niezapłacone
                <input type="checkbox" id="not-paid" value="true" v-model="notPaid">
                <span class="checkmark"></span>
            </label>
            <label class="container">Zapłacone
                <input type="checkbox" id="paid" value="true" v-model="paid">
                <span class="checkmark"></span>
            </label>
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
.container {
  display: block;
  position: relative;
  padding-left: 35px;
  margin-bottom: 12px;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
/*ukrycie domyślnego checkmarka*/
.container input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

.checkmark {
  position: absolute;
  top: 0;
  left: 0;
  height: 25px;
  width: 25px;
  background-color: #eee;
}

.container:hover input ~ .checkmark {
  background-color: #ccc;
}

.container input:checked ~ .checkmark {
  background-color: #17a2b8;
}

.checkmark:after {
  content: "";
  position: absolute;
  display: none;
}

.container input:checked ~ .checkmark:after {
  display: block;
}

.container .checkmark:after {
  left: 10px;
  top: 6px;
  width: 5px;
  height: 10px;
  border: solid white;
  border-width: 0 3px 3px 0;
  -webkit-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  transform: rotate(45deg);
}
</style>
