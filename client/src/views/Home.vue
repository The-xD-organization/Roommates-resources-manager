<template>
    <default-layout>
        <div>
            <h3>Ostatni rachunek</h3>
                {{ $store.state.homeBill.description }}
            <router-link to="/bills">
                Przejdź do rachunków
            </router-link>
        </div>
        <div>
            <h3>Twoje obowiązki</h3>
            <div
                 v-for="task in $store.state.homeTask" :key = task.id
            >
                {{ task.description }} <br>
            </div>
             <router-link to="/tasks">
                Przejdź do obowiązkóœ
            </router-link>
        </div>
    </default-layout>
</template>

<script>
import DefaultLayout from '@/components/layouts/DefaultLayout.vue';


export default {
    name: 'home',
    components: {
        DefaultLayout,
    },
    data() {
        return {
        };
    },

    methods: {
    },
    mounted() {
        this.$store.dispatch('getHomeBill');
        this.$store.dispatch('getHomeTask');
    },
};
</script>
