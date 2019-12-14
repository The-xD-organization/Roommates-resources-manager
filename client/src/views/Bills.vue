<template>
    <default-layout>
        <b-container class="my-2">
            <b-row>
                <b-col>
            <b-card text-black border-variant="0">
                <b-row align-h="start">
                    <b-col sm="4" md="3" xl="2">
                <h2>Rachunki</h2>
                    </b-col>
                    <b-col sm="4" md="2">
                <b-button variant="btn" class="mt-1"
                    v-show="mode != 1"
                    @click="mode = 1"
                >
                    Dodaj
                </b-button>
                <b-button variant="btn" class="mt-1"
                    v-show="mode != 0"
                    @click="mode = 0"
                >
                    Wyświetl listę
                </b-button>
                    </b-col>
                </b-row>
            </b-card>
            <b-card border-variant="0">
            <BillsList
                v-if="mode==0"
            />
            <AddBill
                v-if="mode==1"
            />
            </b-card>
                </b-col>
            </b-row>
        </b-container>
    </default-layout>
</template>

<script>
import DefaultLayout from '@/components/layouts/DefaultLayout.vue';
import BillsList from '@/components/bills/BillsList.vue';
import AddBill from '@/components/bills/AddBill.vue';

export default {
    name: 'bills',
    components: {
        DefaultLayout,
        BillsList,
        AddBill,
    },
    data() {
        return {
            mode: 0,
        };
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
