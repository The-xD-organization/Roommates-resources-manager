<template>
    <default-layout>
        <b-container class="my-2">
            <b-row>
                <b-col>
            <div class="pageMenu">
                <h2>Rachunki</h2>
                <button
                    v-show="mode != 1"
                    @click="mode = 1"
                >
                    Dodaj
                </button>
                <button
                    v-show="mode != 0"
                    @click="mode = 0"
                >
                    Wyświetl listę
                </button>
            </div>
            <BillsList
                v-if="mode==0"
            />
            <AddBill
                v-if="mode==1"
            />
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
