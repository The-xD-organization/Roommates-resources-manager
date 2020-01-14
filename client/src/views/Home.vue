<template>
    <default-layout>
        <b-container class="my-2">
            <b-container>
                <h3 class="py-2">Ostatni rachunek</h3>
             <b-card
            variant="info"
            class="my-2"
            border-variant="info"
        >
        <h5>{{ $store.state.categoriesList[$store.state.homeBill.category_id] }}</h5>
        <hr>
        <p v-show="$store.state.homeBill.usage != 0">
            Zużycie: {{ $store.state.homeBill.usage }}</p>
        <p v-show="$store.state.homeBill.cash != 0">
            Koszt: {{ $store.state.homeBill.cash }} zł</p>
        <p>Data: {{ $store.state.homeBill.date }}</p>
        <p v-show="$store.state.homeBill.description!=''">
            Opis: {{ $store.state.homeBill.description }}</p>
        </b-card>
            <router-link to="/bills">
                Przejdź do rachunków
            </router-link>
            </b-container>
        <b-container class="mb-4">
            <h3 class="py-2">Twoje obowiązki</h3>
            <div>
        <b-card
            variant="info"
            class="my-2"
            border-variant="info"
            v-for="task in $store.state.homeTask" :key = task.id
        >
            <ShowTask
                v-bind:task="task"
            />
        </b-card>
    </div>
             <router-link to="/tasks">
                Przejdź do obowiązków
            </router-link>
        </b-container>
        </b-container>
    </default-layout>
</template>

<script>
import DefaultLayout from '@/components/layouts/DefaultLayout.vue';
import ShowTask from '@/components/tasks/ShowTask.vue';

export default {
    name: 'home',
    components: {
        DefaultLayout,
        ShowTask,
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
