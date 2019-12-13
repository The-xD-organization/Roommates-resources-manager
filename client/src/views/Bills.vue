<template>
    <default-layout>
        <div>
            <div>
                <h2>Rachunki</h2>
            </div>
            <BillsList />
        </div>
    </default-layout>
</template>

<script>
import DefaultLayout from '@/components/layouts/DefaultLayout.vue';
import BillsList from '@/components/bills/BillsList.vue';

export default {
    name: 'bills',
    components: {
        DefaultLayout,
        BillsList,
    },
};
</script>
