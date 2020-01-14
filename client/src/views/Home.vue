<template>
    <default-layout>
        <b-container fluid>
            <b-row class="p-2 justify-content-sm-center">
                <h2>Witaj, {{ $store.state.userData.username }}!</h2>
                <b-col cols="12" md="5" class="m-2">
                    <b-container>
                    <h3 class="text-center">Skróty</h3>
                    <b-card-group columns class=" text-center">
                    <b-card
                    class="my-2"
                    variant="info"
                    border-variant="info">
                    <router-link to="/profile">
                    <b-img
                        src="https://image.flaticon.com/icons/png/512/149/149452.png"
                    class="utility_img" alt="Responsive image"></b-img>
                        <p>Profil</p>
                    </router-link>
                    </b-card>
                    <b-card
                    class="my-2"
                    variant="info"
                    border-variant="info">
                    <router-link to="/bills">
                    <b-img
                    src="https://image.flaticon.com/icons/png/512/313/313434.png"
                    class="utility_img" alt="Responsive image"></b-img>
                        <p>Rachunki</p>
                    </router-link>
                    </b-card>
                    <b-card
                    class="my-2"
                    variant="info"
                    border-variant="info">
                    <router-link to="/tasks">
                    <b-img
                        src="https://image.flaticon.com/icons/png/512/839/839860.png"
                    class="utility_img" alt="Responsive image"></b-img>
                        <p>Obowiązki</p>
                    </router-link>
                    </b-card>
                    </b-card-group>
                    <h3 class="text-center">Ostatni rachunek</h3>
                    <b-card
                    variant="info"
                    border-variant="info">
                    <div class="text-center">
                    </div>
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
                    </b-container>
                </b-col>
                <b-col cols="12" md="5" class="m-2">
                    <b-container>
                        <h3 class="text-center">Twoje obowiązki</h3>
                    <div class="text-center">
                    </div>
                    <div
                    v-for="task in $store.state.homeTask" :key = task.id>
                    <ShowTask
                        v-bind:task="task"
                    />
                    </div>
                    </b-container>
                </b-col>
            </b-row>
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
        if (this.$store.state.userData === null) {
            this.$store.dispatch('getUserData');
        }
    },
};
</script>
<style scoped>
.utility_img{
    max-height: 128px;
    max-width: 128px;
}
</style>
